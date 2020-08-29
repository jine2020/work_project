from case_test.common.app import App
from case_test.proxy.proxy import proxy

class Start:
    def setup(self):
        self.start1=App().start()
    def teardown(self):
        # self.setup().back()
        self.start1.close()

class Starts:
    def setup(self) -> None:
        self.start1=App().start()
        self._case=self.start1.main().creationtimeDESC()

    def teardown(self) -> None :
        #self.start1.back()
        proxy().close_charles()
        self.start1.close()

    def checkcase(self):
        #返回庭审程序，本方地位等
        case_trialprocedure=self._case.getTrialprocedure()
        case_oustatus=self._case.getOurstatus()
        case_Phase=self._case.getPhase()
        case_types=self._case.getcasetypes()
        return case_trialprocedure,case_oustatus,case_Phase,case_types