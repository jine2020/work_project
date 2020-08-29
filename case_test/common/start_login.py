import os
from case_test.common.read_config import read_config

def start_login():
    _pj=read_config().getProjectPath()
    os.system(f'{_pj}\common\\start.bat')

def start_debugging_login():
    _pj=read_config().getProjectPath()
    os.system(f'{_pj}\common\\startdebuggingchrome.bat')
