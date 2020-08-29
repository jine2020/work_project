from time import sleep

from case_test.common.public import Common


class Lawyerlogin(Common):
    #律师端登录
    def lawyer_recruitment(self,no):
        self.quecklawyer().login2(no).clickRrcruitment().creationtimeDESC().clickrecruitment().declarations().recruitment()
        return self

    def quecklawyer(self):
        #选择律师登录入口
        self.steps('../data/yml/login1.yml')
        return self
    def login2(self,no):
        #律师端登录
        sleep(8)
        self._params2={}
        user,pwd=self.getParamVlaue('user,pwd','logindata1',no)
        self._params2['user']=user
        self._params2['pwd']=pwd
        self.steps('../data/yml/login1.yml')
        return self
    def clickRrcruitment(self):
        #点击我要应聘
        self.steps('../data/yml/login1.yml')
        return self

    def creationtimeDESC(self):
        sleep(3)
        windowshands=self._driver.window_handles
        self._driver.switc_to.window(windowshands[-1])
        self.steps('../data/yml/login1.yml')
        return self
    def clickrecruitment(self):
        pass