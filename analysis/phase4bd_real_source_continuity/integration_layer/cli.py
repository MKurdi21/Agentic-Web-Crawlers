"""Fresh-process recovery; prints metadata only, never extracted source values."""
from bridge import *
import argparse
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('operation',choices=['recover','verify']);p.add_argument('run');args=p.parse_args()
 a=RealContinuity(args.run);context='coordinator-'+uuid.uuid4().hex
 s=a.recover(context)
 if args.operation=='verify':a.unit('VERIFICATION','VERIFY')
 a.close_worker()
 print(json.dumps({'coordinator_context_id':context,'pid':os.getpid(),'consumed':a.e.state()['active_holdout_state']=='CONSUMED_VALIDATION_EVIDENCE','packet_sha256':a.cfg['packet_sha256'],'committed_units':[r['atomic_unit_id'] for _,r in a.e.receipts()]}))
