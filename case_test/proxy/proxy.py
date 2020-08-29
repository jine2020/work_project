import os
from case_test.common.app import App
class proxy(App):
    def close_charles(self):
        #关闭charles
        os.system('taskkill /IM Charles.exe')