from selenium import webdriver
from selenium.webdriver.chrome.options import Options as co
from selenium.webdriver.firefox.options import Options as fo
from selenium.webdriver.ie.options import Options as io
from account_test.sc.common.read_config import return_config
import os

class web_driver(return_config):
    """关于浏览器操作的类"""
    def return_driver(self):
        #浏览器选择
        browerType=self.browser_Type()
        options=self.setChrome()
        if browerType=='Chrome':
            return webdriver.Chrome(chrome_options=options)
        elif browerType=='Firefox':
            return webdriver.Firefox(firefox_options=options)
        elif browerType=='IE':
            return webdriver.Ie(ie_options=options)
    def setChrome(self):
        #创建浏览器配置对象实例--chrome自定义路径
        def checkopthions():
            browserType=self.browser_Type()
            if browserType=='Chrome':
                opthons=co()
                return opthons
            elif browserType=='Firefox':
                opthons=fo()
                return opthons
            elif browserType=='IE':
                opthons=io()
                return opthons
        options=checkopthions()
        download_path=self.setdownloadPath()
        options.add_experimental_option("prefs",{
            "download.default_directory":download_path,
            "download.prompt_for_download":False,
            "download.directory_upgrade":True,
            "safebrowsingenabled":True
        })
        return options

    def openBrower(self,driver):
        #打开浏览器
        url=self.test_url()
        driver.get(url)
        driver.maximize_window()
    def closBrowser(self,dirver):
        #关闭浏览器
        dirver.quit()
        os.system('taskkill /f /im chromedirver.exe')
        os.system('taskkill /f /im chrome.exe')

    def forward(self,driver):
        #浏览器前进
        driver.forward()

    def back(self,driver):
        #浏览器后退
        driver.back()

    def refresh(self,driver):
        #刷新
        driver.refresh()

    def downscrollbar(self,driver,no):
        #上下滚动条，no为目标位置离顶部的距离
        js='var q=document.documentElement.scrollTop={}'.format(no)
        driver.execute_script(js)
    def rightscrollbar(self,driver,no):
        #左右滚动条，no为目标位置离左端的距离
        js='var q=document.documentElement.scrollLeft={}'.format(no)
        driver.execute_script(js)

if __name__ == '__main__':
    driver=web_driver()