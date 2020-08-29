import yaml
import os,json
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from case_test.common import start_login
from case_test.common.read_config import read_config
from case_test.page.login import Login
from case_test.common.public import Common

class   App(Common):
    _path=read_config().casePath()
    _case_conf=_path+'run_case_conf\\'
    _case_run=Common().get_publicurlandruntype(_case_conf+'testrun.yml')
    _case_url=Common().get_publicurlandruntype(_case_conf+'caseurl.yml')
    _case_login=Common().get_publicurlandruntype(_case_conf+'caseurl.yml',params='login')

    def start(self,cookie:bool=True):
        if self._driver==None:
            if self._case_run=='debugging':
                #本地复用调试
                _options=Options()
                _options.debugger_address='127.0.0.1:9999'
                self._driver=webdriver.Chrome(options=_options)
                self._driver.get(self._case_login)
            elif self._case_run in ['local','docker']:
                #复用本地登录的浏览器使用token cookie跳过登录
                files=os.listdir(self._path)
                file_cookies='cookies.bat'
                file_js='js.yml'
                if file_cookies in files and file_js in files:
                    pass
                else:
                    start_login.start_login()
                    _options=Options()
                    _options.debugger_address='127.0.0.1:8000'
                    self._driver=webdriver.Chrome(options=_options)
                    self._driver.get(self._case_login)
                    sleep(1)
                    while True:
                        try:
                            _case=Login(driver=self._driver).loginl().getcase()
                            if '前往智能案件管理 >>'==_case:
                                sleep(1)
                                break
                        except:
                            pass
                    db=shelve.open('cookies')
                    db['cookie']=self._driver.get_cookies()

                    def get_local(params):
                        return self._driver.execute_script(
                            "return JSON.parse(window.localStorage.getItem('userObjStr'))"
                        )[params]

                    #获取localStorage值
                    self.locas1=get_local('userTokenId')
                    self.userid=get_local('userId')
                    self.userType=get_local('userType')
                    self.um=get_local('um')
                    self.setId=get_local('setId')
                    self.roleList=get_local('roleList')
                    self.names=get_local('name')
                    self.orgCode=get_local('orgCode')

                    #获取储存的token
                    self.roleList=json.dumps(self.roleList,ensure_ascii=False)
                    self.name=json.dumps(self.names,ensure_ascii=False)
                    js=f'''localStorage.setItem("userObjStr",'{{"um":"{self.um}","userId":"{self.userid}",\
                    "roleList":"{self.roleList}","setId":"{self.setId}","userType":"{self.userType}","name":"{self.name}"\
                    "orgCode":"{self.orgCode}"}}')'''
                    js_path=self._path+"js.yml"
                    with open(js_path,'w',encoding='utf-8')as f:
                        yaml.dump(js,f)
                    os.system('taskkill /IM chrome.exe')
                    if self._case_run=='docker':
                        _start_docker=self.getProjectPath()+"docker"
                        os.system(f'cd{_start_docker} & start.bat')
                        sleep(3)
            if self._case_run=='local':
                #本地跑脚本
                if cookie==True:
                    _options=Options()
                    _options.add_argument('--proxy-server=127.0.0.1:50000')
                    self._driver=webdriver.Chrome(options=_options)
                    _pj=self.getProjectPath()+'proxy'
                    os.system(f'cd {_pj} & charles.bat')
                    sleep(10)
                else:
                    self._driver=webdriver.Chrome()
            elif self._case_run=='docker':
                #容器跑脚本
                self._driver=webdriver.Remote('http://127.0.0.1:5001/wd/hub')
            if cookie==True:
                #获取储存的cookies
                self._driver.get(self._case_url)
                db=shelve.open('cookies')
                cookies=db['cookie']
                for cookie in cookies:
                    if 'expiry' in cookie.keys():
                        cookie.pop('expiry')
                    #向浏览器中注入cookies
                    self._driver.add_cookie(cookie)
                #获取储存的token
                js=yaml.safe_load(open(self._path+'js.yml'))
                #向浏览器中注入token
                self._driver.execute_script(js)
                self._driver.get(self._case_url)
                self._driver.refresh()
                self._driver.maximize_window()
            else:
                self._driver.get(self._case_login)
                self._driver.maximize_window()
        return self

    def back(self):
        #返回列表
        self._driver.get(self._case_url)

    def colse(self):
        #关闭浏览器
        self._driver.quit()

    def main_strat(self):
        #登录
        return Login(self._driver)

    def main(self,debugging:bool=False,types:str='staff'):
        #主入口
        if debugging==True:
            from case_test.lawyerpage.lawyers import Lawyerlogin
            return Lawyerlogin(self._driver)
        else:
            if types=="staff":
                from case_test.page.main import Main
                return Main(self._driver)
            elif types=='lawyer':
                self._driver.get(self._case_login)
                from case_test.lawyerpage.lawyers import Lawyerlogin
                return Lawyerlogin(self._driver)
            elif types=="discussion":
                self._driver.get(self._case_login)
                return Login(self._driver)
