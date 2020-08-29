from account_test.sc.common.log import log
from account_test.sc.common.read_config import return_config
import xlrd

class get_data(log,return_config):
    """获取数据"""
    def auto_get_element_data(self,sheet,element_name,col=3):
        """根据元素名称获取元素表数据"""
        self.error_txt = self.getErrorTxt()
        self.info_txt = self.getInfoTxt()
        path = xlrd.open_workbook(self.getElementPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        names=sheet1.col_values(0)
        i=0
        for name in names:
            if element_name==name:
                col_data=sheet1.cell(i, col - 1).value
                return  col_data
            else:
                i += 1
                if i==len(names):
                    self.error(self.error_txt[4].format(sheet, element_name))
    def auto_get_test_data(self,sheet,element_name,col=3):
        """根据元素名称获取测试数据"""
        self.error_txt = self.getErrorTxt()
        self.info_txt = self.getInfoTxt()
        path = xlrd.open_workbook(self.getTestDataPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        names=sheet1.col_values(0)
        i=0
        for name in names:
            if element_name==name:
                col_data=sheet1.cell(i, col - 1).value
                return  col_data
            else:
                i += 1
                if i==len(names):
                    self.error(self.error_txt[4].format(sheet, element_name))

    def auto_test_data_cols(self,sheet):
        """获取测试数据条数"""
        path = xlrd.open_workbook(self.getTestDataPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        clos=sheet1.ncols
        return clos-2

if __name__ == '__main__':
        get_data=get_data()
        print(get_data.auto_test_data_cols(1))