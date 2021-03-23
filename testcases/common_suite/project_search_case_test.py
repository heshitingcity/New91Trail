#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/19 18:02
# @File    : project_search_case_test.py

import unittest
from common.Stard_End import StarEnd
from Utils.test_case_data_utils import TestDataUtils
from actions.common_action import CommonPageAction
from actions.login_ation import LoginAction
from Utils.log_utils import logger



class ProjectSearch_action(StarEnd):

    test_case_data = TestDataUtils('common_suite', 'projectSearch_case_data').convert_exceldata_to_testdata()
    # print(test_case_data)

    def setUp(self) -> None:
        super().setUp()


    @unittest.skipIf(test_case_data['test_projectSearch_success']['isnot'], '条件为真跳过')
    def test_ProjectSearch01_1_success(self):
        logger.info('test_ProjectSearch01_1_success 用例开始执行')
        test_function_data=self.test_case_data['test_projectSearch_success']
        self._testMethodDoc = test_function_data['test_name']
        login_action=LoginAction(self.base_page.driver)
        login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))

        ProjectSearch = CommonPageAction(self.base_page.driver)
        ProjectSearch.project_search_way01(test_function_data['test_parameter'].get('精准搜索'))
        logger.info('test_ProjectSearch01_1_success 用例结束执行')


    @unittest.skipIf(test_case_data['test_projectSearch_success']['isnot'], '条件为真跳过')
    def test_ProjectSearch01_2_success(self):
        logger.info('test_ProjectSearch01_2_success 用例开始执行')
        test_function_data=self.test_case_data['test_projectSearch_success']
        self._testMethodDoc = test_function_data['test_name']
        login=LoginAction(self.base_page.driver)
        login.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        ProjectSearch = CommonPageAction(self.base_page.driver)
        ProjectSearch.project_search_way01(test_function_data['test_parameter'].get('精准搜索'))
        ProjectSearch.project_search_way02(test_function_data['test_parameter'].get('模糊搜索'))
        logger.info('test_ProjectSearch01_2_success 用例结束执行')



    @unittest.skipIf(test_case_data['test_projectSearch_fail']['isnot'],'条件为真则跳过')
    def test_ProjectSearch02_1_fail(self):
        logger.info('test_ProjectSearch02_1_fail   用例开始执行')
        test_function_data = self.test_case_data['test_projectSearch_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action=LoginAction(self.base_page.driver)
        login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        CommonPageAction(self.base_page.driver).project_search_way01(test_function_data['test_parameter'].get('projectName1'))
        logger.info('test_ProjectSearch02_1_fail 用例结束执行')


    @unittest.skipIf(test_case_data['test_projectSearch_fail']['isnot'],'条件为真则跳过')
    def test_ProjectSearch02_2_fail(self):
        logger.info('test_ProjectSearch02_2_fail   用例开始执行')
        test_function_data = self.test_case_data['test_projectSearch_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action=LoginAction(self.base_page.driver)
        login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        CommonPageAction(self.base_page.driver).project_search_way01(test_function_data['test_parameter'].get('projectName1'))
        CommonPageAction(self.base_page.driver).project_search_way02(test_function_data['test_parameter'].get('projectName'))
        logger.info('test_ProjectSearch02_2_fail 用例结束执行')


if __name__ == '__main__':
    unittest.main(verbosity=2)