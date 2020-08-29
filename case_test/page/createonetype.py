from case_test.common.public import Common
from case_test.page.createtwotype import CreateTWOTpye

class CreateOneTpye(Common):
    #填写案件基本信息
    def onetype(self,no='1',status:str='Y'):
        #下一步
        self.casepany()
        self.comloance()
        pass
        return CreateTWOTpye(self._driver)

    def casepany(self):
        #选择发案单位
        self.setparamVlue(['Units'],'createonedata')
        self.steps('../data/yml/createonetype.yml')

    def comloance(self):
        pass