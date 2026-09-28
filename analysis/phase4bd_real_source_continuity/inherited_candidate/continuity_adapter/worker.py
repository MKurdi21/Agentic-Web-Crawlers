"""Isolated deterministic synthetic scientific worker; reads stdin, never paths."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'vendor'))
import context_engine as c
def execute(envelope):
    c.require(set(envelope)=={'packet','source','stage','primary_item'},'worker envelope scope')
    packet=envelope['packet'].encode('utf-8');body=c.validate_packet(packet)
    c.require(body['binding']['phase']=='SYNTHETIC_TEST' and body['binding']['paper_id']=='SYNTHETIC_REPORT_X','synthetic only')
    source=envelope['source'].encode('utf-8');c.require(c.digest(source)==body['binding']['source_sha256'],'source identity')
    report=c.loads(source)
    c.require(set(report)=={'report_id','synthetic','trials','successes'} and report['synthetic'] is True and report['report_id']=='SYNTHETIC_REPORT_X','source schema')
    n,k=report['trials'],report['successes'];c.require(type(n) is int and type(k) is int and n>0 and 0<=k<=n,'numeric operands')
    item={'report_id':report['report_id'],'source_sha256':c.digest(source),'field_id':'success_fraction','numerator':k,'denominator':n,'value':k/n,'support_locator':{'type':'TEXT_SPAN','artifact_sha256':c.digest(source),'start':0,'end':len(source),'offset_convention':'UTF8_BYTES'},'scientific_namespace':'SYNTHETIC_MECHANICS_ONLY'}
    if envelope['stage']=='primary':
        c.require(envelope['primary_item'] is None and body['role']=='primary','primary inputs')
        return item
    c.require(envelope['stage']=='verifier' and body['role']=='verifier','verification role')
    c.require(envelope['primary_item']==item,'candidate differs from exact source arithmetic')
    return {'source_sha256':c.digest(source),'reviewed_item_sha256':c.fingerprint(item),'outcome':'SUPPORTED','namespace':'SYNTHETIC_MECHANICS_ONLY','verification_mode':'DETERMINISTIC_SOURCE_CHECK_NOT_HUMAN'}
if __name__=='__main__':
    request=c.loads(sys.stdin.buffer.read());sys.stdout.buffer.write(c.canonical(execute(request)))
