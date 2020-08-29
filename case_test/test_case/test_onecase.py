import pytest
from case_test.common.public import getYml
from case_test.common.start import Start


class TestOneCase(Start):
    """一审"""
    @pytest.mark.newcase
    def test_onecaseY(self):
        '''一审原告新建流程'''
        case=self.start1.main().mains().onetype().twotype().threetype()
        case_no=case.getcaseno()
        case_no2=case.fourtype().creationtimeDESC().getcaseno()
        assert case_no==case_no2,'Create Failure!'