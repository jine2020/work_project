from account_test.sc.common.page_base import page_base
from time import sleep

class Public(page_base):
    def __init__(self,driver,sheet,section):
        self.driver=driver
        self.sheet=sheet
        self.section=section

    def publicFindElement(self,no,types="By.XPATH"):
        #元素显示等待
        self.findElement(self.driver,self.publicElementValue(no),types)
    def publicElementValue(self,no):
        #获取元素表元素值
        elementvalue=self.elementVlue(self.section,no,self.sheet)
        return elementvalue
    def publicClick(self,no,types='By.XPATH'):
        #点击
        self.waitandClick(self.driver,self.publicElementValue(no),types)
    def publicInput(self,no,text,types='By.XPATH'):
        #输入
        self.waitandSendkeys(self.driver,self.publicElementValue(no),text,types)
    def publicGetText(self,no,types='By.XPATH'):
        #获取文本
        text=self.getText(self.driver,self.publicElementValue(no),types)
        return text
    def publicEqual(self,no,text,types='By.XPATH'):
        #断言
        sleep(1)
        self.assertEqual(self.driver,self.publicGetText(no,types),text)
    def publicLeftClick(self,no,types='By.XPATH'):
        #鼠标左击
        self.leftclick(self.driver,self.publicElementValue(no),types)
