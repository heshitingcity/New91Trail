# encoding: utf-8
#@author: newdream_daliu
#@file: quit_test.py
#@time: 2020-08-09 17:10

import unittest
from common.Stard_End import  StarEnd
from Utils.test_case_data_utils import TestDataUtils
from common.base_page import BasePage
from actions.login_ation import LoginAction
from actions.common_action import CommonPageAction


class QuitTest(StarEnd):
     # test_class_data = TestDadaUtils('common_suite', 'quit_case_data',).convert_exceldata_to_testdata()
     test_class_data = TestDataUtils('common_suite', 'quit_case_data','QuitTest').convert_exceldata_to_testdata()
     def setUp(self):
         super().setUp()

     @unittest.skipIf(test_class_data['test_quit']['isnot'], '条件为真跳过')
     def test_quit(self):
         test_function_data = self.test_class_data['test_quit']
         self._testMethodDoc = test_function_data['test_name']

         LoginAction(self.base_page.driver).login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))

         CommonPageAction(self.base_page.driver).quit()
         actual_result=BasePage(self.base_page.driver).get_title()
         self.assertEqual(actual_result,'91trial','test_quit 用例不通过')

if __name__=="__main__":
    unittest.main(verbosity=2)