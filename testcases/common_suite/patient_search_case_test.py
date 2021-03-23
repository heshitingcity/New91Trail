#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/11/2 15:00
# @File    : patient_search_case_test.py

import unittest
from actions.common_action import CommonPageAction
from Utils.test_case_data_utils import TestDadaUtils
from common.Stard_End import StarEnd
from Utils.log_utils import logger
from actions.login_ation import LoginAction


class PatienSearch(StarEnd):
    test_case_data = TestDadaUtils("common_suite","patientSearch_case_data").convert_exceldata_to_testdata()

    def setUp(self) -> None:
        super().setUp()


    @unittest.skipIf(test_case_data["test_patientSearch_success_by_name"]["isnot"],"条件为真则跳过")
    def test_patient_search1_by_name_success(self):
        logger.info("test_patient_search1_by_name_success  用例开始执行")
        test_function = self.test_case_data["test_patientSearch_success_by_name"]
        self._testMethodDoc = test_function["test_name"]
        login = LoginAction(self.base_page.driver)
        login.login_success(test_function['test_parameter'].get('username'),test_function['test_parameter'].get('password'))
        common_page = CommonPageAction(self.base_page.driver)
        common_page.project_search_way01(test_function['test_parameter'].get('projectName'))
        common_page.chose_patient_menu()
        common_page.Patient_search(test_function['test_parameter'].get('NameSearch'))
        logger.info("test_patient_search1_by_name_success  用例结束执行")


    @unittest.skipIf(test_case_data["test_patientSearch_success_by_number"]["isnot"],"条件为真则跳过")
    def test_patient_search2_by_Number_success(self):
        logger.info("test_patient_search2_by_Number_success  用例开始执行")
        test_function = self.test_case_data["test_patientSearch_success_by_number"]
        self._testMethodDoc = test_function["test_name"]
        login = LoginAction(self.base_page.driver)
        login.login_success(test_function['test_parameter'].get('username'),test_function['test_parameter'].get('password'))
        common_page = CommonPageAction(self.base_page.driver)
        common_page.project_search_way01(test_function['test_parameter'].get('projectName'))
        common_page.chose_patient_menu()
        common_page.Patient_search(test_function['test_parameter'].get('numberSearch'))
        logger.info("test_patient_search2_by_Number_success  用例结束执行")



    @unittest.skipIf(test_case_data["test_patientSearch_fail_by_name"]["isnot"],"条件为真则跳过")
    def test_patient_search3_by_name_fail(self):
        logger.info("test_patient_search3_by_name_fail  用例开始执行")
        test_function = self.test_case_data["test_patientSearch_fail_by_name"]
        self._testMethodDoc = test_function["test_name"]
        login = LoginAction(self.base_page.driver)
        login.login_success(test_function['test_parameter'].get('username'),test_function['test_parameter'].get('password'))
        common_page = CommonPageAction(self.base_page.driver)
        common_page.project_search_way01(test_function['test_parameter'].get('projectName'))
        common_page.chose_patient_menu()
        common_page.Patient_search(test_function['test_parameter'].get('NameSearch'))
        logger.info("test_patient_search3_by_name_fail  用例结束执行")



    @unittest.skipIf(test_case_data["test_patientSearch_fail_by_number"]["isnot"],"条件为真则跳过")
    def test_patient_search4_by_Number_fail(self):
        logger.info("test_patient_search4_by_Number_fail  用例开始执行")
        test_function = self.test_case_data["test_patientSearch_fail_by_number"]
        self._testMethodDoc = test_function["test_name"]
        login = LoginAction(self.base_page.driver)
        login.login_success(test_function['test_parameter'].get('username'),test_function['test_parameter'].get('password'))
        common_page = CommonPageAction(self.base_page.driver)
        common_page.project_search_way01(test_function['test_parameter'].get('projectName'))
        common_page.chose_patient_menu()
        common_page.Patient_search(test_function['test_parameter'].get('numberSearch'))
        logger.info("test_patient_search4_by_Number_fail  用例结束执行")



    @unittest.skipIf(test_case_data["test_patientSearch_success_by_vistiManage"]["isnot"],"条件为真则跳过")
    def test_patientSearch_success5_by_vistiManage(self):
        logger.info("test_patient_search1_by_name_success  用例开始执行")
        test_function = self.test_case_data["test_patientSearch_success_by_vistiManage"]
        self._testMethodDoc = test_function["test_name"]
        login = LoginAction(self.base_page.driver)
        login.login_success(test_function['test_parameter'].get('username'),test_function['test_parameter'].get('password'))
        common_page = CommonPageAction(self.base_page.driver)
        common_page.project_search_way01(test_function['test_parameter'].get('projectName'))
        common_page.chose_visit_menu()
        common_page.Patient_search(test_function['test_parameter'].get('NameSearch'))
        common_page.Visit_search()
        common_page.click_JX_visit()
        logger.info("test_patientSearch_success5_by_vistiManage  用例结束执行")




if __name__ == '__main__':
    unittest.main(verbosity=2)