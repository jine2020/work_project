import configparser,json,os

"""获取各类配置"""
def get_path():
    #获取项目地址
    namepath=os.path.abspath(os.path.dirname(__file__))
    projectpath=namepath[:namepath.find("account_test\\")]+"account_test\\"
    return projectpath

class return_config():
    #读取配置文件
    config=configparser.ConfigParser()
    config_path=get_path()+'\config\config.ini'
    config.read(config_path,encoding='utf8')

    #项目路径
    getProjectPath=get_path()
    """常规设置"""
    def browser_Type(self):
        #浏览器选择
        browserType=self.config.get('browserType','browserName')
        return browserType
    def test_url(self):
        #项目地址
        url=self.config.get('testUrl','URL')
        return url
    def elementTable(self,sheetname):
        #元素表页签
        elementnum=self.config.getint('elementVlue',sheetname)
        return elementnum
    def getElementPath(self):
        #元素表路径
        get_element_path=self.config.get('getData','element_path')
        return self.getProjectPath+get_element_path
    def logName(self):
        #日志名称
        logname=self.config.get('log','logName')
        return logname
    def uploadfiles(self):
        #上传文件源地址
        get_uploadfile_path=self.config.get('other_path','uploadFiles_path')
        return self.getProjectPath+get_uploadfile_path
    def setdownloadPath(self):
        #下载文件储存路径
        download_path=self.config.get('other_path','download_path')
        return self.getProjectPath+download_path
    def logPath(self):
        #日志存放路径
        logpath=self.config.get('log','logPath')
        return self.getProjectPath+logpath
    def screenshotpath(self):
        #截图存放路径
        get_screenshotpath=self.config.get('other_path','screenshotpath')
        return self.getProjectPath+get_screenshotpath
    def casePath(self):
        #案例存放路径
        get_case_path=self.config.get('other_path','case_path')
        return self.getProjectPath+get_case_path
    def reportPath(self):
        #测试报错存放路径
        get_report_path=self.config.get('other_path','report_path')
        return self.getProjectPath+get_report_path
    def path(self):
        return self.getProjectPath
    def getErrorTxt(self):
        #error字段信息
        get_error_txt=self.config.get('getData','error_txt')
        get_error_txt1=json.loads(get_error_txt)
        return get_error_txt1
    def getInfoTxt(self):
        #info字段信息
        get_info_txt=self.config.get('getData','info_txt')
        get_info_txt1=json.loads(get_info_txt)
        return get_info_txt1
    def testDataTable(self,sheetname):
        #测试数据页签
        testtalenum=self.config.getint('testData',sheetname)
        return testtalenum
    def getTestDataPath(self):
        #测试数据表路径
        get_test_data_path=self.config.get('getData','test_data_path')
        return self.getProjectPath+get_test_data_path

    def getBugListPath(self):
        #bug表路径
        get_bug_list_path=self.config.get('test_report','buglist_path')
        return self.getProjectPath+get_bug_list_path

    def getTestReportPath(self):
        #report表路径
        get_test_report_path=self.config.get('test_report','testreport_path')
        return self.getProjectPath+get_test_report_path

    """参数"""
    def public(self,section):
        #读取参数方法
        list=self.config.items(section)
        Parameter=[]
        for i in list:
            Parameter.append(i[1])
        return Parameter

    def getLoginParameter(self):
        return self.public('login_parameter')

if __name__ == '__main__':
    ss=return_config().getBugListPath()
    print(ss)