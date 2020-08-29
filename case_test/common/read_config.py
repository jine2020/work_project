import configparser,os
"""获取各类配置"""
def _get_path():
    """获取项目地址"""
    namepath=os.path.abspath(os.path.dirname(__file__))
    projectpath=namepath[:namepath.find("case_test\\")]+"case_test\\"
    return projectpath

class read_config():
    """读取配置文件config.ini"""
    config=configparser.ConfigParser()
    config_path=_get_path()+"\config\config.ini"
    config.read(config_path,encoding='utf8')


    #x项目路径
    _getProjectPath=_get_path()
    '''常规设置'''
    def logName(self):
        #日志名称
        logname=self.config.get('log','logName')
        return logname

    def logPath(self):
        #日志存放路径
        logPath=self.config.get('log','logPath')
        return self._getProjectPath+logPath
    def screenshotpath(self):
        #截图存放路径
        get_screenshotpath=self.config.get('other_path','screenshotpath')
        return self._getProjectPath+get_screenshotpath
    def casePath(self):
        #用例存放路径
        get_case_path=self.config.get('other_path','case_path')
        return self._getProjectPath+get_case_path

    def reportPath(self):
        #测试报告存放路径
        get_report_path=self.config.get('other_path','report_path')
        return self._getProjectPath+get_report_path
    def getProjectPath(self):
        #获取项目路径
        return _get_path()

if __name__ == '__main__':
    pass