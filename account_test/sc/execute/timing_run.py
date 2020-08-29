import time,os
from account_test.sc.common.read_config import return_config
"""定时执行脚本"""
start_time=input('请输入用例开始执行时间，例如12:00\n')
while True:
    #获取系统时间
    path=return_config().path()
    now=time.strftime("%H:%M",time.localtime())
    if now==start_time:
        print('___开始执行测试用例___')
        #切换到python.exe所在目录
        os.chdir(r'D:/Anaconda3/envs/case_auto_test')
        #使用python命令调用总执行脚本
        for i in range(1):
            os.system('python {}\sc\execute\\run_case.py'.format(path))
        print('--用例执行结束--')
        break
    else:
        time.sleep(10)
        print(now)
if __name__ == '__main__':
    pass

