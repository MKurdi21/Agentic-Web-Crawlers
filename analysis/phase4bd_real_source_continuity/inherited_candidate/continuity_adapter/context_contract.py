"""Report-agnostic context reconstruction; no source opening or transport.

Caller supplies verified durable artifacts and an exact frozen binding. The
returned bytes are the complete worker input. Session/history arguments do not
exist. Source access and authoritative receipt-chain checks precede this API.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'vendor'))
import context_engine as c
def reconstruct_worker_context(*,packet,expected_binding,source_bytes,stage,
                               primary_item,approved_packet_sha256,source_consumed,
                               preaccess,ack,access,release_decision,expected_release_sha256,
                               expected_code_sha256,expected_policy_sha256,
                               expected_template_sha256,expected_access_namespace,
                               registered_primary_sha256=None):
    c.require(stage in ['primary','verifier'],'worker stage')
    body=c.validate_packet(packet)
    c.require(body['role']==stage and body['binding']==c.validate_binding(expected_binding),'current-report binding')
    c.require(c.digest(packet)==approved_packet_sha256 and c.digest(source_bytes)==expected_binding['source_sha256'],'packet/source identity')
    c.require(source_consumed is True,'source access not committed')
    c.require(preaccess['binding']==expected_binding and preaccess['source_sha256']==expected_binding['source_sha256'],'preaccess source binding')
    c.require(c.fingerprint(release_decision)==expected_release_sha256 and release_decision['binding_sha256']==c.fingerprint(expected_binding) and release_decision['packet_sha256']==preaccess['packet_sha256'] and release_decision['status']=='PACKET_DRY_RUN_APPROVED','release identity')
    c.require(preaccess['release_sha256']==expected_release_sha256 and preaccess['immutable_code_sha256']==expected_code_sha256 and preaccess['policy_sha256']==expected_policy_sha256 and preaccess['template_sha256']==expected_template_sha256,'preaccess pins')
    c.require(ack['previous_sha256']==c.fingerprint(preaccess) and access['previous_sha256']==c.fingerprint(ack),'receipt-chain continuity')
    c.require(ack['packet_sha256']==preaccess['packet_sha256'] and ack['fork_history']=='none' and ack['context_id'],'acknowledgement')
    c.require(access['source_sha256']==expected_binding['source_sha256'] and access['namespace']==expected_access_namespace,'source-access record')
    if stage=='primary':
        c.require(primary_item is None,'unexpected primary context')
        c.require(c.digest(packet)==preaccess['packet_sha256'],'primary preaccess packet mismatch')
    else:c.require(primary_item is not None and c.fingerprint(primary_item)==registered_primary_sha256,'uncommitted verification candidate')
    return c.canonical({'packet':packet.decode('utf-8'),'source':source_bytes.decode('utf-8'),'stage':stage,'primary_item':primary_item})
