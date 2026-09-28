"""Real-report transport, consumption and recovery; no scientific authority.

All source/report authorization is supplied by a pinned explicit registry entry.
No source is parsed by this coordinator. Delivery is restricted to fresh workers.
"""
from pathlib import Path
import sys,os,json,hashlib,uuid,subprocess
O=Path(__file__).resolve().parents[1];R=O.parents[1]
P=R/'analysis/phase4bc_path_containment';C=R/'analysis/phase4bc_context_isolation';S=R/'analysis/phase4bc_supplement';BR=R/'analysis/phase4br_remediation'
sys.path.insert(0,str(P/'path_containment'))
from parent_adapter import build_parent_packet
from guard import context as c
sys.path.insert(0,str(S/'recovery_protocol'))
from engine import Engine,Blocked,exclusive,canonical,read,filehash,replace,now,PIN_KEYS
sys.path.insert(0,str(BR/'candidate_v4br/hardened/scripts'))
import pre_access as helper
sys.path.insert(0,str(BR/'candidate_v4br/_deps'))
VERSION='phase4bd-real-source-continuity-v1.0.0'
METHOD='ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f'
class Crash(RuntimeError):pass
def fail(x,reason):
    if not x:raise Blocked(reason)
def digest(b):return hashlib.sha256(b).hexdigest()
def schema(name,obj):
    if 'jsonschema' not in sys.modules:runtime_integrity()
    import jsonschema
    jsonschema.Draft202012Validator(read(O/(name+'.schema.json'))).validate(obj)
def code_manifest():
    files=list((O/'integration_layer').glob('*.py'))+list(O.glob('*.schema.json'))
    files += [P/'path_containment/guard.py',P/'path_containment/parent_adapter.py',P/'vendor/context_engine.py',S/'recovery_protocol/engine.py',S/'RECOVERY_STATE.schema.json',S/'RECOVERY_EVENTS.schema.json',S/'MILESTONE_RECEIPT.schema.json',BR/'candidate_v4br/hardened/scripts/pre_access.py',BR/'DEPENDENCY_MANIFEST.json',BR/'REMEDIATED_WORKFLOW_CONFIGURATION.json',C/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json',O/'integration_layer/worker_contract.json']
    files += [C/'context_architecture'/x['relative_path'] for x in read(C/'IMMUTABLE_EXECUTION_MANIFEST.json')['files']]
    return [{'path':str(p.relative_to(R)).replace('\\','/'),'size':p.stat().st_size,'sha256':filehash(p)} for p in sorted(files)]
def codehash():return digest(canonical(code_manifest()))
def runtime_integrity():
    from runtime_guard import verify
    manifest=read(BR/'DEPENDENCY_MANIFEST.json')['files'];root=BR/'candidate_v4br/_deps'
    try:verify(root,manifest,filehash)
    except RuntimeError as ex:raise Blocked(str(ex)) from ex
    return digest(canonical(manifest))
def packet_binding(entry):
    return {'phase':'PHASE4BD_DEVELOPMENT','holdout_id':entry['development_id'],'paper_id':entry['report_id'],'source_sha256':entry['source_sha256'],'methodology_sha256':METHOD,'context_protocol_version':c.VERSION,'current_report_source':'NOT_YET_OPENED'}
def packet(entry):
    root=C/'context_architecture'
    return build_parent_packet(root,c.load(root/'registry.json'),c.load(root/'allowlists.json'),packet_binding(entry),'primary')
def scan(data,entry):
    """Exact structural current-identity exception, never broad deny suppression."""
    body=c.validate_packet(data);fail(body['binding']==packet_binding(entry),'PACKET_BINDING')
    deny=c.load(C/'context_architecture/deny_rules/denylist.json');raw=c.scan_packet(data,deny)
    sanitized=c.loads(data)
    # Only two known schema fields are masked for scanner comparison. All original
    # bytes and exact identity exceptions remain recorded and separately reviewed.
    sanitized['binding']['holdout_id']='CURRENT_REPORT_ID'
    sanitized['binding']['paper_id']='CURRENT_PAPER_ID'
    checked=c.scan_packet(c.canonical(sanitized),deny)
    fail(checked['status']=='STATIC_CONTEXT_CLEAN','CONTEXT_CONTAMINATION')
    return {'packet_sha256':digest(data),'raw_scan':raw,'nonidentity_scan':checked,'exception_scope':['/binding/holdout_id','/binding/paper_id'],'exact_allowed_values':[entry['development_id'],entry['report_id']],'status':'CLEAN_WITH_EXACT_CURRENT_IDENTITY_EXCEPTION' if raw['hits'] else 'STATIC_CONTEXT_CLEAN','deny_sha256':c.fingerprint(deny)}
def review_valid(data,review,entry):
    scan(data,entry)
    fail(review['packet_sha256']==digest(data) and review['status']=='SEMANTIC_CONTEXT_CLEAN','SEMANTIC_REVIEW')
    fail(review['reviewer_context_id'] and review['reviewer_context_id']!='/root' and review['current_identity_exception_approved'] is True,'SEPARATE_REVIEW_REQUIRED')
    fail(review['wrapper_sha256']==filehash(O/'integration_layer/worker_contract.json'),'WRAPPER_REVIEW_STALE')
    fail(review.get('review_mode')=='SEPARATE_CONTEXT_MODEL_VERIFICATION' and isinstance(review.get('rationale'),str) and review['rationale'].strip(),'REVIEW_PROVENANCE')
    fail(review.get('review_protocol_sha256')==read(C/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json')['semantic_review_protocol_sha256'],'REVIEW_PROTOCOL_DRIFT')
    fail(review.get('exception_scope')=={'/binding/holdout_id':entry['development_id'],'/binding/paper_id':entry['report_id']},'IDENTITY_EXCEPTION_SCOPE')

class RealContinuity:
    def __init__(self,root):
        self.root=Path(root);self.e=Engine(self.root/'durable');self.proc=None
    @property
    def cfg(self):return read(self.root/'configuration.json')
    @property
    def entry(self):return self.cfg['entry']
    def create(self,authorization_path,entry_id,review_path):
        runtime_integrity()
        auth=read(authorization_path);fail(entry_id in auth['reports'],'REPORT_NOT_AUTHORIZED')
        entry=auth['reports'][entry_id]
        fail(entry_id==entry['report_id'] and entry['source_file_id']=='sha256:'+entry['source_sha256'],'REGISTRY_IDENTITY')
        fail(entry['report_id'] not in auth['reserved_denied_report_ids'],'RESERVED_REPORT_DENIED')
        fail(entry['source_role'] in auth['permitted_source_roles'],'SOURCE_ROLE_DENIED')
        fail(entry['prior_consumption_state'] in ['CONSUMED_VALIDATION_EVIDENCE','UNTOUCHED_RESERVED_VALIDATION_EVIDENCE'],'PRIOR_STATE')
        path=Path(entry['source_path']);fail(path.is_file() and not path.is_symlink(),'SOURCE_PATH')
        fail(filehash(path)==entry['source_sha256'],'SOURCE_HASH')
        data,meta=packet(entry);review=read(review_path);review_valid(data,review,entry)
        self.root.mkdir(parents=True,exist_ok=False)
        cfg={'version':VERSION,'run_id':'real-'+uuid.uuid4().hex,'entry':entry,'binding':packet_binding(entry),'packet_sha256':digest(data),'packet_meta':meta,'packet_template_sha256':filehash(C/'context_architecture/packet_templates/PRIMARY_CONTEXT_PACKET_TEMPLATE.json'),'policy_sha256':c.fingerprint(c.load(C/'context_architecture/deny_rules/denylist.json')),'code_sha256':codehash(),'authorization_path':str(Path(authorization_path).resolve()),'authorization_sha256':filehash(authorization_path),'review_path':str(Path(review_path).resolve()),'review_sha256':filehash(review_path),'context_sha256':'63927844eaac94765a7a804ab128076a88cad6eac2f534b715b08b17c4e21606','path_sha256':'41fa409998ec492286c81e01efb8484a4805074f97093ae795b0c11911ce43dd','recovery_sha256':'5f5adf341fac45c68cb23d6e97714ec7324625ca1ee9b3bfa6b8fbe5ab2ac0d0'}
        exclusive(self.root/'configuration.json',canonical(cfg));exclusive(self.root/'packet.json',data)
        pins={'methodology_sha256':METHOD,'context_architecture_sha256':cfg['context_sha256'],'immutable_code_sha256':cfg['code_sha256'],'protected_file_manifest_sha256':cfg['authorization_sha256'],'source_sha256':entry['source_sha256'],'current_packet_sha256':cfg['packet_sha256']}
        with self.e.lock('init'):
            self.e.init(cfg['run_id'],pins,phase='PHASE4BD_REAL_DEVELOPMENT',bindings=[{'path':str(self.root/'configuration.json'),'sha256':filehash(self.root/'configuration.json')}])
            s=self.e.state();s.update(active_holdout_id=entry['development_id'],active_holdout_state=entry['prior_consumption_state']);self.e.save(s)
        return self
    def check(self):
        cfg=self.cfg;e=cfg['entry'];fail(codehash()==cfg['code_sha256'],'CODE_DRIFT')
        fail(filehash(cfg['authorization_path'])==cfg['authorization_sha256'],'AUTHORIZATION_DRIFT')
        auth=read(cfg['authorization_path']);fail(auth['reports'].get(e['report_id'])==e and e['report_id'] not in auth['reserved_denied_report_ids'],'REPORT_AUTHORITY')
        fail(filehash(cfg['review_path'])==cfg['review_sha256'],'REVIEW_DRIFT')
        fail(filehash(e['source_path'])==e['source_sha256'],'SOURCE_HASH')
        data,meta=packet(e);fail(digest(data)==cfg['packet_sha256']==filehash(self.root/'packet.json'),'PACKET_DRIFT')
        review_valid(data,read(cfg['review_path']),e)
        return cfg,data
    def _commit(self,unit,obj):
        path='outputs/'+unit.lower()+'.json';start=self.e.begin(unit,{'configuration':filehash(self.root/'configuration.json')},[path])
        if not start.get('already_committed'):self.e.commit({path:canonical(obj)},next_operation='REAL_CONTINUITY_GATE')
        else:fail(read(self.e.root/path)==obj,'REPLAY_CONFLICT')
        return read(self.e.root/path)
    def _worker_start(self,stage):
        runtime_integrity()
        cfg,data=self.check();context_id='worker-'+uuid.uuid4().hex
        header={'packet':data.decode(),'source_sha256':cfg['entry']['source_sha256'],'report_id':cfg['entry']['report_id'],'source_size':Path(cfg['entry']['source_path']).stat().st_size,'context_id':context_id,'stage':stage,'wrapper_sha256':filehash(O/'integration_layer/worker_contract.json')}
        p=subprocess.Popen([sys.executable,'-B',str(O/'integration_layer/worker.py')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        p.stdin.write(canonical(header)+b'\n');p.stdin.flush();ack=json.loads(p.stdout.readline())
        fail(ack=={'context_id':context_id,'packet_sha256':cfg['packet_sha256'],'status':'ACKNOWLEDGED','fork_history':'none'},'WORKER_ACK')
        self.proc=p;self.context_id=context_id;self.worker_stage=stage
        return ack
    def close_worker(self):
        if self.proc is not None:
            if self.proc.poll() is None:self.proc.kill()
            self.proc.communicate(timeout=30);self.proc=None
    def prepare(self):
        if (self.e.root/'outputs/packet_ack.json').exists():
            self.check();self.e.receipts();return read(self.e.root/'outputs/packet_ack.json')
        cfg,data=self.check();ack=self._worker_start('EXTRACT')
        obj={'acknowledgement_id':self.context_id,'run_id':cfg['run_id'],'report_id':cfg['entry']['report_id'],'source_sha256':cfg['entry']['source_sha256'],'methodology_sha256':METHOD,'context_architecture_sha256':cfg['context_sha256'],'path_containment_sha256':cfg['path_sha256'],'recovery_protocol_sha256':cfg['recovery_sha256'],'packet_template_sha256':cfg['packet_template_sha256'],'packet_sha256':cfg['packet_sha256'],'primary_context_id':self.context_id,'timestamp':now(),'status':'ACKNOWLEDGED','fork_history':'none'}
        schema('PACKET_ACKNOWLEDGEMENT',obj)
        with self.e.lock(self.context_id):self._commit('PACKET_ACK',obj)
        return obj
    def preaccess(self):
        if (self.e.root/'outputs/pre_access.json').exists():
            self.chain();return read(self.e.root/'outputs/pre_access.json')
        cfg,data=self.check();self.e.receipts();ack=read(self.e.root/'outputs/packet_ack.json')
        b={'phase':'PHASE4BD_REAL_DEVELOPMENT','holdout_id':cfg['entry']['development_id'],'paper_id':cfg['entry']['report_id'],'source_file_id':cfg['entry']['source_file_id'],'source_sha256':cfg['entry']['source_sha256'],'candidate_manifest_sha256':cfg['code_sha256'],'methodology_sha256':METHOD,'protocol_hashes':{'context':cfg['context_sha256'],'path':cfg['path_sha256'],'recovery':cfg['recovery_sha256'],'template':cfg['packet_template_sha256']},'field_catalog_sha256':filehash(C/'context_architecture/methodology_generic/FIELD_CATALOG.json'),'holdout_state':cfg['entry']['prior_consumption_state'],'context_protocol_version':c.VERSION}
        helper_dir=self.root/'real_helper'
        if not (helper_dir/'PRE_ACCESS_RECEIPT.json').exists():helper.commit_preaccess(helper_dir,b,allowed_reports={b['holdout_id']})
        raw=read(helper_dir/'PRE_ACCESS_RECEIPT.json');fail(all(raw[k]==v for k,v in b.items()),'HELPER_PREACCESS_BINDING')
        obj={'run_id':cfg['run_id'],'atomic_unit_id':'SOURCE_ACCESS','report_id':b['paper_id'],'source_file_id':b['source_file_id'],'source_sha256':b['source_sha256'],'packet_sha256':cfg['packet_sha256'],'packet_acknowledgement_id':ack['acknowledgement_id'],'ack_sha256':filehash(self.e.root/'outputs/packet_ack.json'),'immutable_fingerprints':{'methodology':METHOD,'context':cfg['context_sha256'],'path':cfg['path_sha256'],'recovery':cfg['recovery_sha256'],'integration':cfg['code_sha256']},'static_status':scan(data,cfg['entry'])['status'],'semantic_status':'SEMANTIC_CONTEXT_CLEAN','role':cfg['entry']['source_role'],'prior_consumption_state':b['holdout_state'],'source_access_started':False,'commit_timestamp':now(),'helper_receipt_sha256':filehash(helper_dir/'PRE_ACCESS_RECEIPT.json')}
        schema('PRE_ACCESS_RECEIPT',obj)
        with self.e.lock('preaccess'):self._commit('PRE_ACCESS',obj)
        return obj
    def chain(self,require_access=False,partial=False):
        cfg,data=self.check();chain=self.e.receipts();by={r['atomic_unit_id']:r for _,r in chain}
        accesses=[x for x in self.e.journal() if x['event_type']=='SOURCE_ACCESS_BEGAN'];fail(len(accesses)<=1,'DUPLICATE_CONSUMPTION')
        if partial and 'PRE_ACCESS' not in by:
            fail(not accesses,'ACCESS_WITHOUT_PREACCESS')
            if 'PACKET_ACK' in by:
                ack=read(self.e.root/'outputs/packet_ack.json');schema('PACKET_ACKNOWLEDGEMENT',ack)
                fail(ack['run_id']==cfg['run_id'] and ack['report_id']==cfg['entry']['report_id'] and ack['packet_sha256']==cfg['packet_sha256'] and ack['source_sha256']==cfg['entry']['source_sha256'],'ACK_BINDING')
            return by,accesses
        fail('PACKET_ACK' in by and 'PRE_ACCESS' in by,'PREACCESS_CHAIN_MISSING')
        ack=read(self.e.root/'outputs/packet_ack.json');pre=read(self.e.root/'outputs/pre_access.json')
        schema('PACKET_ACKNOWLEDGEMENT',ack);schema('PRE_ACCESS_RECEIPT',pre)
        for obj in [ack,pre]:fail(obj['run_id']==cfg['run_id'] and obj['report_id']==cfg['entry']['report_id'] and obj['source_sha256']==cfg['entry']['source_sha256'] and obj['packet_sha256']==cfg['packet_sha256'],'CHAIN_IDENTITY')
        expected_ack={'methodology_sha256':METHOD,'context_architecture_sha256':cfg['context_sha256'],'path_containment_sha256':cfg['path_sha256'],'recovery_protocol_sha256':cfg['recovery_sha256'],'packet_template_sha256':cfg['packet_template_sha256'],'fork_history':'none','status':'ACKNOWLEDGED'}
        fail(all(ack[k]==v for k,v in expected_ack.items()),'ACK_PROTOCOL_PINS')
        fail(ack['acknowledgement_id']==ack['primary_context_id'],'ACK_CONTEXT_ID')
        fail(pre['source_file_id']==cfg['entry']['source_file_id'] and pre['role']==cfg['entry']['source_role'] and pre['prior_consumption_state']==cfg['entry']['prior_consumption_state'],'PREACCESS_ROLE_IDENTITY')
        fail(pre['immutable_fingerprints']=={'methodology':METHOD,'context':cfg['context_sha256'],'path':cfg['path_sha256'],'recovery':cfg['recovery_sha256'],'integration':cfg['code_sha256']},'PREACCESS_PROTOCOL_PINS')
        fail(pre['ack_sha256']==filehash(self.e.root/'outputs/packet_ack.json') and pre['packet_acknowledgement_id']==ack['acknowledgement_id'],'ACK_LINK')
        fail(pre['helper_receipt_sha256']==filehash(self.root/'real_helper/PRE_ACCESS_RECEIPT.json'),'HELPER_RECEIPT_DRIFT')
        raw=read(self.root/'real_helper/PRE_ACCESS_RECEIPT.json')
        expected_helper={'phase':'PHASE4BD_REAL_DEVELOPMENT','holdout_id':cfg['entry']['development_id'],'paper_id':cfg['entry']['report_id'],'source_file_id':cfg['entry']['source_file_id'],'source_sha256':cfg['entry']['source_sha256'],'candidate_manifest_sha256':cfg['code_sha256'],'methodology_sha256':METHOD,'protocol_hashes':{'context':cfg['context_sha256'],'path':cfg['path_sha256'],'recovery':cfg['recovery_sha256'],'template':cfg['packet_template_sha256']},'field_catalog_sha256':filehash(C/'context_architecture/methodology_generic/FIELD_CATALOG.json'),'holdout_state':cfg['entry']['prior_consumption_state'],'context_protocol_version':c.VERSION}
        fail(all(raw.get(k)==v for k,v in expected_helper.items()),'HELPER_BINDING')
        if require_access:fail(len(accesses)==1,'NO_DURABLE_ACCESS')
        if accesses:
            fail('SOURCE_INTENT' in by,'ACCESS_WITHOUT_INTENT')
            fail(read(self.e.root/'outputs/source_intent.json')=={'report_id':cfg['entry']['report_id'],'source_sha256':cfg['entry']['source_sha256'],'preaccess_sha256':filehash(self.e.root/'outputs/pre_access.json')},'SOURCE_INTENT_BINDING')
            a=accesses[0];schema('SOURCE_ACCESS_EVENT',a)
            fail(a['run_id']==cfg['run_id'] and a['report_id']==cfg['entry']['report_id'] and a['source_sha256']==cfg['entry']['source_sha256'] and a['packet_sha256']==cfg['packet_sha256'],'ACCESS_IDENTITY')
            fail(a['triggering_receipt_sha256']==filehash(self.e.root/'outputs/pre_access.json') and a['context_id']==ack['primary_context_id'] and a['new_state']=='CONSUMED_VALIDATION_EVIDENCE' and a['prior_state']==cfg['entry']['prior_consumption_state'],'ACCESS_LINK')
            if 'CONSUMPTION' in by:
                state=read(self.e.root/'outputs/consumption.json');schema('CONSUMPTION_STATE',state)
                fail(state=={'run_id':cfg['run_id'],'report_id':cfg['entry']['report_id'],'source_sha256':cfg['entry']['source_sha256'],'source_access_event_id':a['event_id'],'state':'CONSUMED_VALIDATION_EVIDENCE','prior_state':cfg['entry']['prior_consumption_state'],'irreversible':True},'CONSUMPTION_LINK')
            if 'DELIVERY_AUTHORITY' in by:
                gate=read(self.e.root/'outputs/delivery_authority.json');d=self.root/'real_helper'
                fail(gate['helper_event_sha256']==filehash(d/'SOURCE_ACCESS_BEGAN.json') and gate['consumption_sha256']==filehash(self.e.root/'outputs/consumption.json') and gate['access_event_id']==a['event_id'] and gate['source_sha256']==cfg['entry']['source_sha256'],'DELIVERY_CHAIN')
                helper.verify_order(read(d/'PRE_ACCESS_RECEIPT.json'),read(d/'SOURCE_ACCESS_BEGAN.json'))
                he=read(d/'SOURCE_ACCESS_BEGAN.json');fail(he['holdout_id']==cfg['entry']['development_id'] and he['source_sha256']==cfg['entry']['source_sha256'],'HELPER_EVENT_IDENTITY')
        return by,accesses
    def _source_bytes(self,crash=None):
        cfg,data=self.check();self.chain();entry=cfg['entry']
        with self.e.lock('source-transaction'):
            self._commit('SOURCE_INTENT',{'report_id':entry['report_id'],'source_sha256':entry['source_sha256'],'preaccess_sha256':filehash(self.e.root/'outputs/pre_access.json')})
            _,events=self.chain()
            if not events:
                ack=read(self.e.root/'outputs/packet_ack.json')
                a=self.e.event('SOURCE_ACCESS_BEGAN',run_id=cfg['run_id'],report_id=entry['report_id'],source_sha256=entry['source_sha256'],packet_sha256=cfg['packet_sha256'],context_id=ack['primary_context_id'],prior_state=entry['prior_consumption_state'],new_state='CONSUMED_VALIDATION_EVIDENCE',triggering_receipt_sha256=filehash(self.e.root/'outputs/pre_access.json'))
            else:a=events[0]
            if crash=='event_before_state':raise Crash(crash)
            s=self.e.state();s.update(source_access_started=True,source_access_event_id=a['event_id'],active_holdout_state='CONSUMED_VALIDATION_EVIDENCE');self.e.save(s)
            consumption={'run_id':cfg['run_id'],'report_id':entry['report_id'],'source_sha256':entry['source_sha256'],'source_access_event_id':a['event_id'],'state':'CONSUMED_VALIDATION_EVIDENCE','prior_state':entry['prior_consumption_state'],'irreversible':True}
            schema('CONSUMPTION_STATE',consumption);self._commit('CONSUMPTION',consumption)
            if crash=='after_consumption':raise Crash(crash)
            d=self.root/'real_helper';b=read(d/'PRE_ACCESS_RECEIPT.json')
            if not (d/'SOURCE_ACCESS_BEGAN.json').exists():
                source=helper.open_source(d,entry['source_path'],b,allowed_reports={entry['development_id']})
            else:
                he=read(d/'SOURCE_ACCESS_BEGAN.json');helper.verify_order(b,he)
                fail(he['source_sha256']==entry['source_sha256'] and he['holdout_id']==entry['development_id'],'HELPER_ACCESS_IDENTITY')
                source=Path(entry['source_path']).read_bytes()
            fail(digest(source)==entry['source_sha256'],'SOURCE_READ_HASH')
            self._commit('DELIVERY_AUTHORITY',{'helper_event_sha256':filehash(d/'SOURCE_ACCESS_BEGAN.json'),'consumption_sha256':filehash(self.e.root/'outputs/consumption.json'),'source_sha256':digest(source),'access_event_id':a['event_id']})
            self.chain(require_access=True)
            fail(self.e.state()['source_access_started'] and self.e.state()['active_holdout_state']=='CONSUMED_VALIDATION_EVIDENCE','DELIVERY_BEFORE_COMMIT')
        return source
    def unit(self,unit_id,stage='EXTRACT',crash=None):
        runtime_integrity()
        fail(unit_id in ['EXTRACTION','VERIFICATION'],'UNIT_ID')
        fail(stage==('EXTRACT' if unit_id=='EXTRACTION' else 'VERIFY'),'UNIT_STAGE_MISMATCH')
        self.check();by,events=self.chain()
        if stage=='VERIFY':fail('EXTRACTION' in by,'VERIFICATION_WITHOUT_EXTRACTION')
        if unit_id in by:
            self.chain(require_access=True);fail(self.e.state()['source_access_started'] and self.e.state()['active_holdout_state']=='CONSUMED_VALIDATION_EVIDENCE','CONSUMPTION_PROJECTION_REQUIRES_RECOVERY');return read(self.e.root/('outputs/'+unit_id.lower()+'.json'))
        source=self._source_bytes(crash=crash)
        if self.proc is not None and self.worker_stage!=stage:self.close_worker()
        if self.proc is None or self.proc.poll() is not None:
            ack=self._worker_start(stage)
            with self.e.lock('fresh-context'):
                self._commit('CONTEXT_'+self.context_id.replace('-','_').upper(),{'context_id':self.context_id,'packet_sha256':ack['packet_sha256'],'fork_history':'none','source_sha256':self.entry['source_sha256']})
        with self.e.lock(self.context_id):
            start=self.e.begin(unit_id,{'configuration':filehash(self.root/'configuration.json'),'stage':stage},['outputs/'+unit_id.lower()+'.json'])
            if crash=='during_unit':self.e.preempt();self.close_worker();return None
            if crash=='during_delivery':
                self.proc.stdin.write(source[:100]);self.proc.stdin.flush();self.close_worker();self.e.preempt();return None
            out,err=self.proc.communicate(input=source,timeout=120);status=self.proc.returncode;self.proc=None
            fail(status==0,'WORKER_FAILED:'+err.decode(errors='replace')[:200])
            result=c.loads(out);fail(result['source_sha256']==self.entry['source_sha256'] and result['report_id']==self.entry['report_id'] and result['stage']==stage,'WORKER_RESULT_BINDING')
            if crash=='before_unit_commit':
                exclusive(self.e.root/'staging'/start['attempt_id']/'uncommitted.json',canonical(result));self.e.preempt();return None
            self.e.commit({'outputs/'+unit_id.lower()+'.json':canonical(result)},next_operation='NEXT_SCIENTIFIC_UNIT' if unit_id=='EXTRACTION' else 'DEVELOPMENT_GATE')
            return result
    def recover(self,context_id):
        runtime_integrity()
        cfg,data=self.check()
        with self.e.lock(context_id):
            self.e.journal(repair=True);by,access=self.chain(partial=True)
            # All booleans are derived from verified current bytes and receipt links.
            review=read(cfg['review_path'])
            continuity={'same_report':cfg['binding']==packet_binding(cfg['entry']),'unchanged_pins':cfg['code_sha256']==codehash(),'clean_context':scan(data,cfg['entry'])['status'] in ['STATIC_CONTEXT_CLEAN','CLEAN_WITH_EXACT_CURRENT_IDENTITY_EXCEPTION'],'known_scientific_milestone':all(k in by for k in ['PACKET_ACK','PRE_ACCESS']) if access else False,'unambiguous_acceptance':len(access)<=1,'fresh_packet_review':review['packet_sha256']==digest(data) and review['status']=='SEMANTIC_CONTEXT_CLEAN'}
            # Parent key names are retained for compatibility: before an extraction
            # commit, known milestone means known PRE_ACCESS transport checkpoint;
            # fresh review means still-valid exact-byte review, not a new model pass.
            pins={'methodology_sha256':METHOD,'context_architecture_sha256':cfg['context_sha256'],'immutable_code_sha256':cfg['code_sha256'],'protected_file_manifest_sha256':cfg['authorization_sha256'],'source_sha256':cfg['entry']['source_sha256'],'current_packet_sha256':digest(data)}
            s=self.e.recover(pins,continuity=continuity if access else None,session_mode='NEW_SESSION')
            if access or cfg['entry']['prior_consumption_state']=='CONSUMED_VALIDATION_EVIDENCE':
                s['active_holdout_state']='CONSUMED_VALIDATION_EVIDENCE';self.e.save(s)
            return s
