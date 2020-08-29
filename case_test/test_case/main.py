import warnings,os,pytest
from case_test.common.public import Common

def removes():
    try:
        _outer_path=Common().casePath()
        Common().remove(_outer_path+'cookies.bak')
        Common().remove(_outer_path + 'cookies.dat')
        Common().remove(_outer_path + 'cookies.dir')
        Common().remove(_outer_path + 'js.yml')
    except:
        print('no cookies')

class Case(Common):
    def cases(self):
        """批量执行测试用例文件"""
        #默认执行回归测试
        #运行前检查移除cookies及token
        removes()
        warnings.filterwarnings('ignore')
        _outer_path=self.casePath()
        _folderlist=os.listdir(_outer_path)
        case_list=[]
        for folder in _folderlist:
            if "test_proxy" in folder:
                case_list.append(folder)
            else:
                continue
        _case_conf=_outer_path+'run_case_conf\\'
        _case_types=self.get_publicurlandruntype(_case_conf+'testcase.yml')
        pytest.main([*case_list,f'-m={_case_types}','-vs'])
        #运行完成移除cookies及token
        removes()

Case().cases()
