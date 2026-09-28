"""Record actual unittest outcomes; no model calls or live-data mutations."""
import unittest
from common import *
class Results(unittest.TextTestResult):
 def startTestRun(self):self.rows=[];super().startTestRun()
 def addSuccess(self,test):super().addSuccess(test);self.rows.append({'test':test.id(),'status':'PASS'})
 def addFailure(self,test,err):super().addFailure(test,err);self.rows.append({'test':test.id(),'status':'FAIL','detail':self._exc_info_to_string(err,test)})
 def addError(self,test,err):super().addError(test,err);self.rows.append({'test':test.id(),'status':'ERROR','detail':self._exc_info_to_string(err,test)})
 def addSkip(self,test,reason):super().addSkip(test,reason);self.rows.append({'test':test.id(),'status':'SKIP','reason':reason})
if __name__=='__main__':
 suite=unittest.defaultTestLoader.discover(str(DESIGN/'hardened/tests'))
 result=unittest.TextTestRunner(verbosity=2,resultclass=Results).run(suite)
 write_json(DESIGN/'test_results/UNIT_INTEGRATION_RESULTS.json',{'run_at':stamp(),'tests_run':result.testsRun,'passed':sum(x['status']=='PASS' for x in result.rows),'failed':len(result.failures)+len(result.errors),'skipped':len(result.skipped),'tests':result.rows})
 sys.exit(not result.wasSuccessful())
