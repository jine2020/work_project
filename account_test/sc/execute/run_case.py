import unittest,time,HTMLTestRunner
from account_test.sc.common.read_config import return_config
path=return_config()
case_path=path.casePath()
report_path=path.reportPath()
now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
report_name=report_path+'自动化测试报告%s.html'%now
fp=open(report_name,'wb')
def run_test(filename='account_test_*.py'):
    """批量运行脚本"""
    suite=unittest.defaultTestLoader.discover(case_path,filename)
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,title='XXX系统回归测试报告',tester='test_team'
    )
    runner.run(suite)#执行测试套件

if __name__ == '__main__':
    run_test()