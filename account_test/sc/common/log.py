import logging
from account_test.sc.common.read_config import return_config

"""重写log日志类"""
class log():
    def setMsg(self,level,msg):
        self.logname = return_config().logName()
        self.logpath = return_config().logPath()
        log_name = self.logpath+self.logname+".log"
        logger = logging.getLogger()
        fh = logging.FileHandler(log_name)  #定义日志写入的文件
        ch = logging.StreamHandler()     #定义日志在控制台输出
        fmt = logging.Formatter("%(asctime)s %(levelname)-8s:%(message)s")
        #分别给文件日志和控制台日志设置刚才设定的日志格式
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)
        #添加haddler,为日志添加日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
        #添加日志信息，输出INFO级别的日志信息
        logger.setLevel(logging.INFO)
        """
        对输入的的参数进行判断，例如输入的level等级为info
        则调用logger中的info方法将日志信息写入到文件中
        """
        if level == "debug":
            logger.debug(msg)
        elif level == "info":
            logger.info(msg)
        elif level == "warning":
            logger.warning(msg)
        elif level == "error":
            logger.error(msg)
        #移除日志输出平台，避免重复写入
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()
    def debug(self,msg):
        self.setMsg('debug',msg)
    def info(self,msg):
        self.setMsg("info",msg)
    def warning(self,msg):
        self.setMsg("warning",msg)
    def error(self,msg):
        self.setMsg("error",msg)
if __name__ == '__main__':
   log().info("这是一个测试")

