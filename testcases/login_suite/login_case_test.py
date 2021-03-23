# encoding: utf-8
#@author: city
#@file: login_case_test.py
#@time: 2020-08-09 15:21

import unittest
import time
import os
from common.Stard_End import StarEnd
from actions.login_ation import LoginAction
from Utils.test_case_data_utils import TestDataUtils
from Utils.log_utils import logger
from unittestreport import TestRunner




class LoginTest(StarEnd):
    test_case_data = TestDataUtils('login_suite', 'login_case_data').convert_exceldata_to_testdata()
    # test_case_data = TestDadaUtils('login_suite', 'login_case_data','LoginTest').convert_exceldata_to_testdata()
    # print(test_case_data)
    @unittest.skipIf(test_case_data['test_login_success']['isnot'], '条件为真跳过')
    def test_login01_success(self):
        logger.info('test_login01_success 用例开始执行')
        test_function_data=self.test_case_data['test_login_success']
        self._testMethodDoc = test_function_data['test_name']
        login_action=LoginAction(self.base_page.driver)
        login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        # self.assertEqual(main_page.get_username(),test_function_data['excepted_result'],'test01登录失败')
        logger.info('test_login01_success 用例结束执行')


    @unittest.skipIf(test_case_data['test_login_fail']['isnot'], '条件为真跳过')
    def test_login02_fail(self):
        logger.info('test_login02_fail 用例开始执行')
        test_function_data=self.test_case_data['test_login_fail']
        print(test_function_data)
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        login_action.login_fail(test_function_data['test_parameter'].get('username'),
                                test_function_data['test_parameter'].get('password'))
        # actual_result =
        # print('actual_result:%s'%actual_result)
        # self.assertEqual(actual_result,test_function_data['excepted_result'])
        logger.info('test_login02_fail 用例结束执行')

    @unittest.skipIf(test_case_data['test_login_default']['isnot'], '条件为真跳过')
    def test_login03_default(self):
        logger.info('test_login03_default 用例开始执行')
        test_function_data=self.test_case_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        time.sleep(3)
        logger.info('test_login03_default 用例结束执行')



if __name__ =='__main__':
    unittest.main(verbosity=2)
    # nowtime = time.strftime('%Y-%m-%d')
    # current = os.path.dirname(__file__)
    # reportpath = os.path.join(current, '../../'+local_config.report_path).replace('\\','/')
    # case_path = os.path.join(current,'../../',local_config.testcase_path).replace('\\','/')
    # reportName ='91Trial自动化测试报告%s.html' % nowtime
    # suite = unittest.defaultTestLoader.discover(start_dir=case_path,
    #                                             pattern='*.py',
    #                                             top_level_dir=None)
    # runner = TestRunner(suite,
    #                     filename = reportName,
    #                     report_dir = reportpath,
    #                     title = '91Trial自动化测试报告',
    #                     tester = 'city',
    #                     desc   =  "city执行测试生产的报告",
    #                     templates = 2    # 参数可选 1、2 ，展示不同风格
    #                     )
    # runner.run()
