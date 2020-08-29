import yaml,os
from inspect import stack
from time import sleep
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from account_test.sc.excel_data_case.auto_data import auto_name
from case_test.common.log import log
from case_test.common.read_config import read_config

def getYml(parames,types,):
    '''
    ('casep',yaml.salf_load(open('../data/createoinedata.yml',encoding='utf-8))['caseP'])
    params is parame eg. name
    types is yaml fiel name
    '''
    outer_path=r'../data/'
    folderlist=os.listdir(outer_path)
    for folder in folderlist:
        inner_path=os.path.join(outer_path,folder)
        filelist=os.listdir(inner_path)
        for file in filelist:
            if types in file:
                path:str=inner_path+"/"+file
                return pytest.mark.parametrize(parames,
                                               yaml.safe_load(open(path.format(types),encoding='utf-8'))[parames])

class Common(log,read_config):
    _param2={} #输入集合
    _param1={} #定位元素值中集合

    def __init__(self,driver=None):
        self._driver=driver

    def get_publicurlandruntype(self,file,params='params'):
        #获取url等case运行的参数
        f=yaml.safe_load(open(file,encoding='utf-8'))
        case_url=f[params][f['default'][0]]
        return case_url
    def remove(self,file):
        #移除文件
        os.remove(file)

    def action(self,action,element,name,step_loctator,value=None):
        #操作点击，清除，输入错误，输入日志并截图
        times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        try:
            if action=='click':
                element.click()
            elif action=="clear":
                element.clear()
            elif action=="send":
                element.send_keys(value)
            self.info('click info:'+name+":"+step_loctator)
        except:
            self.error('click error:'+name+":"+step_loctator)
            self._driver.save_screenshot(self.screenshotpath()+name+step_loctator+times+".png")

    def getParamVlaue(self,param,filename,no=0):
        '''get param value'''
        with open(f'../data/data_yml/{filename}.yml',encoding='uft-8') as f:
            paramvlue=yaml.safe_load(f)[param][no]
        return paramvlue

    def setparamVlue(self,paramlist:list,filename:str):
        self._param2={}
        for param in paramlist:
            paramvlue=self.getParamVlaue(param,filename)
            self._param2[param]=paramvlue

    def sleep(self,no):
        self._driver.implicitly_wait(no)

    def checkelement(self,sgrl:str,val:dict=None):
        #处理字符串中的参数
        if len(val)>0:
            for r in val.values():
                sgrl=sgrl.replace('{}',r,1)
            return sgrl
        else:
            return sgrl

    def steps(self,path):
        #操作步骤
        with open(path,encoding='utf-8')as f:
            name=stack()[1].function
            steps=yaml.safe_load(f)[name]
            for step in steps:
                step:dict
                if 'locator' in step.keys():
                    step_loctator=self.checkelement(step['locator'],self._param1)
                if 'By' in step.keys():
                    keys=(step['By'],step_loctator)
                    element=WebDriverWait(self._driver,8,1).until(ec.presence_of_element_located(keys))
                if 'action' in step.keys():
                    action=step['action']
                    if 'click'==action:
                        element=WebDriverWait(self._driver,8,1).until(ec.element_to_be_clickable((step["By"],step_loctator)))
                        self.action('click',element,name,step_loctator)
                    elif action in ["send","upload"]:
                        if "{" in step['value']:
                            value:str=step['value']
                            for key in self._param2.keys():
                                if key in value:
                                    value=value.replace('{%s}'%key,self._param2[key])
                                    if action=="send":
                                        self.action('clear',element,name,step_loctator)
                                    self.action('send',element,name,step_loctator,value=value)
                        elif 'auto' in step['vallue']:
                            value=auto_name()
                            self.action('clear',element,name,step_loctator)
                            self.action('send',element,name,step_loctator,value=value)
                        else:
                            if action=='send':
                                self.action('clear',element,name,step_loctator)
                            self.action('send',element,name,step_loctator,value=step['value'])
                    elif 'clear'==action:
                        self.action('clear',element,name,step_loctator)
                    elif 'sleep' ==action:
                        sleep(1.6)
                    elif 'text'==action:
                        return element.text
                    elif 'selectorlist'==action:
                        element=WebDriverWait(self._driver,8,1).until(
                            ec.element_to_be_clickable((step['By'],step_loctator))
                        )
                        self.action('click',element,name,step_loctator)
                        self._driver.find_element('css selector','body>div:last-child li').click()
                    else:
                        raise ('action not in action-list')
                else:
                    raise ('error')

if __name__ == '__main__':
    pass
