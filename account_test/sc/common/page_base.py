from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from account_test.sc.common.log import log
from account_test.sc.common.read_config import return_config
from account_test.sc.excel_data_case.get_data import get_data
from unittest import TestCase
import os,time



class page_base(log,return_config):
    """页面基础操作"""
    def findElement(self,driver,xpath,s='By.XPATH'):
        """元素显示等待的方法
        """
        try:
            d=xpath
            if s=='By.XPATH':
                s=By.XPATH
                ss= WebDriverWait(driver,12,0.5).until(
                ec.presence_of_element_located((s,d)))
                return ss
            elif s=="By.ID":
                s=By.ID
                ss= WebDriverWait(driver,12,0.5).until(
                ec.presence_of_element_located((s,d)))
                return ss
            elif s=="By.CLASS_NAME":
                s=By.CLASS_NAME
                ss= WebDriverWait(driver,12,0.5).until(
                ec.presence_of_element_located((s,d)))
                return ss
            elif s=="By.NAME":
                s=By.NAME
                ss= WebDriverWait(driver,12,0.5).until(
                ec.presence_of_element_located((s,d)))
                return ss
            elif s=="By.CSS_SELECTOR":
                s=By.CSS_SELECTOR
                ss=WebDriverWait(driver,12,0.5).until(
                ec.presence_of_element_located((s,d)))
                return ss
        except:
            self.screenshot(driver)
            self.error('not find element, %s'%xpath)
            raise ('not find element, %s'%xpath)

    #点击
    def waitandClick(self,driver,xpath,s='By.XPATH'):
        try:
            self.findElement(driver,xpath,s).click()
            self.info('click element, success, %s' % xpath)

        except :
            self.screenshot(driver)
            self.error('click element, failed, %s' % xpath)
            raise('click element, failed, %s' % xpath)


    #填写表单
    def waitandSendkeys(self,driver,xpath, keys,s='By.XPATH'):
        try:
            self.findElement(driver, xpath,s).send_keys("")
            self.findElement(driver,xpath,s).clear()
            self.findElement(driver,xpath,s).send_keys(keys)
            self.info("input element, success, {}" .format(xpath))
        except :
            self.screenshot(driver)
            self.error('input element, failed, %s' % xpath)
            raise('input element, failed, %s' % xpath)

    #获取文本
    def getText(self,driver,xpath,s='By.XPATH'):
        try:
            text=self.findElement(driver,xpath,s).text
            self.info('getText element, success, %s' % xpath)
            return text
        except:
            self.screenshot(driver)
            self.error('getText element, failed, %s'%xpath)
            raise('getText element, failed, %s'%xpath)

    def assertEqual(self,driver,test1,test2):
        #断言
        try:
            TestCase().assertEqual(test1, test2)
            self.info('assertEqual success,{}=={}'.format(test1,test2))
        except:
            self.screenshot(driver)
            self.error('assertEqual failed,{}!={}'.format(test1,test2))
            raise('assertEqual failed,{}!={}'.format(test1,test2))


    #截图
    def screenshot(self,driver):
        path=self.screenshotpath()
        screen_dir=os.path.abspath(path+'lawyer')
        rq=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name=screen_dir+rq+'.png'
        driver.get_screenshot_as_file(screen_name)

    def enter(self,driver,xpath):
        #回车键
        element=self.findElement(driver,xpath)
        element.send_keys(Keys.ENTER)

    def leftclick(self,driver,xpath,s='By.XPATH'):
        #鼠标左击
        element = self.findElement(driver, xpath,s)
        ActionChains(driver).click(element).perform()
        self.info('chlck element, success, %s' % xpath)

    def defaultframe(self,driver):
        driver.switch_to_default_content()

    def uploadFiles(self,driver,xpath,filename):
        #上传文件
        try:
            self.findElement(driver,xpath).send_keys(filename)
            self.info('uploadfile element, success, %s' % xpath)
        except:
            self.screenshot(driver)
            self.error('uploadfile element, failed, %s'%xpath)
            raise ('uploadfile element, failed, %s'%xpath)
    def alertAccept(self,driver):
        alert=driver.switch_to.alert()
        alert.accept()
    def alertDismiss(self,driver):
        alert=driver.switch_to_alert()
        alert.dismiss()
    def ifrem(self,driver,s):
        driver.switch_to_frame(s)

    def equalfile(self,name):
        #判断本地有无下载的文件
        name_path=self.setdownloadPath()+name
        if os.path.exists(name_path):
            self.info("本地文件夹中有文件：'{}!".format(name))
            os.remove(name_path)
            self.info("已经删除该文件！")
        else:
            self.info('本地文件夹中没有文件："{}"！'.format(name))
    def equaldownload(self,name):
        #验证下载
        name_path=self.setdownloadPath()+name
        if (os.path.exists(name_path)):
            self.info("下载文件：'{}'成功！".format(name))
        else:
            self.error("下载文件：'{}'失败！".format(name))
            raise ("下载文件：'{}'失败！".format(name))

    def get_elementName(self,no):
        #获取参数名称
        element_name=self.getLoginParameter()[no-1]
        return element_name
    def elementVlue(self,section,no,sheet):
        #获取元素表元素值
        element_name=section[no-1]
        return get_data().auto_get_element_data(sheet,element_name)



if __name__ == '__main__':
    page_base().findElement(1,1)