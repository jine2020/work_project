import time
from account_test.sc.common.read_config import return_config
import xlrd

class get_data(return_config):
    """获取数据"""
    def auto_get_data(self,sheet=1,rol=1):
        """单行数据"""
        path = xlrd.open_workbook(self.getBugListPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        rols=sheet1.row_values(rol-1)
        return rols

    def auto_lens(self,sheet=1):
        """BUG总行数"""
        path = xlrd.open_workbook(self.getBugListPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        cols = sheet1.col_values(0)
        return len(cols)

    def auto_lens_report(self,sheet=1):
        """REPORT总行数"""
        path = xlrd.open_workbook(self.getTestReportPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        cols = sheet1.col_values(0)
        return len(cols)

    def auto_list_bug(self,sheet=1):
        """bug id列表"""
        path = xlrd.open_workbook(self.getBugListPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        cols = sheet1.col_values(0)
        return cols[1:]

    def auto_uid(self,sheet=1,rol=4,col=1):
        """用户故事ID"""
        path = xlrd.open_workbook(self.getTestReportPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        cols=sheet1.col_values(rol-1)
        list_cols=str(cols[col+1])
        list_cols=list_cols.split(",")
        return list_cols
    def auto_xid(self,sheet=1,rol=3,col=1):
        """需求ID"""
        path = xlrd.open_workbook(self.getTestReportPath())
        sheet1 = path.sheet_by_index(sheet - 1)
        cols=sheet1.col_values(rol-1)
        list_cols=str(cols[col+1])
        list_cols=list_cols.split(",")
        return list_cols


    def bug_uid(self,rol):
        """BUG用户故事ID"""
        rol=rol+1
        uid=self.auto_get_data(rol=rol)[1]
        return uid

    def bug_id(self,rol):
        """BUG ID"""
        rol=rol+1
        bug_id=self.auto_get_data(rol=rol)[0]
        return bug_id

    def bug_create_date(self, rol):
        """BUG创建时间"""
        rol = rol + 1
        create_date = self.auto_get_data(rol=rol)[4]
        return create_date

    def new_bugs(self):
        """新增bug"""
        sum=0
        now=time.localtime()[2]-19+44062
        for rol in range(1,self.auto_lens()-1):
            bug_createtime=self.bug_create_date(rol)
            if int(bug_createtime)==now:
                sum+=1
        return sum

    def bug_type(self,rol):
        """BUG状态"""
        rol = rol + 1
        bug_type = self.auto_get_data(rol=rol)[2]
        return bug_type

    def sum(self):
        y_list=self.xuyanshou_bug() #需要验证的缺陷
        print(f"提测BUG{len(y_list)}")
        sum_bugs=self.auto_list_bug()
        for i in range(1,self.auto_lens_report()-1):
            uid= self.auto_uid(col=i)
            s_list=[] #用户故事下的缺陷
            w_list = []  # 完成的bug列表
            t_list = []  # 退回的bug列表
            for m in range(1,self.auto_lens()):
                bug_uid=self.bug_uid(m)
                if bug_uid in uid:

                    s_list.append(self.bug_id(m))
                    if self.bug_id(m) in y_list:
                        bug_type=self.bug_type(m)
                        if bug_type in ["完成","待验收"]:
                            w_list.append(self.bug_id(m))
                        else:
                            t_list.append(self.bug_id(m))
            print(f'用户故事：{uid}下未通过的缺陷：{len(t_list)}个,通过的缺陷：{len(w_list)}')
        print(f'非需求缺陷：->{suns}：：->{sum_bugs}')

    def xuyanshou_bug(self):
        #需要验收的bug
        fabu_bug=input("请输入发布的缺陷，以 “，”隔开：")
        fabu_bug_list=fabu_bug.split(',')
        return fabu_bug_list




if __name__ == '__main__':
        get_data=get_data()
        print(f'新增BUG：{get_data.new_bugs()}')
        get_data.sum()

