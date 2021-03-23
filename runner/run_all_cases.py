# encoding: utf-8
#@author: city
#@file: run_all_cases.py
#@time: 2020-08-16 14:33

import os
import time
import unittest
from Utils.config_utils import local_config
from Utils.email_utils import EmailUtils
from unittestreport import TestRunner
from Utils.zip_utils import zip_dir

nowtime = time.strftime('%Y-%m-%d')
current = os.path.dirname(__file__)
class RunAllCases(object):

    def run(self):
        #测试套件的构建

        reportpath = os.path.join(current, '../' + local_config.report_path).replace('\\', '/')
        case_path = os.path.join(current, '../', local_config.testcase_path).replace('\\', '/')
        reportName = '91Trial自动化测试报告%s.html' % nowtime
        suite = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                    pattern='*test.py',
                                                    top_level_dir=None)
        runner = TestRunner(suite,
                            filename=reportName,
                            report_dir=reportpath,
                            title='91Trial自动化测试报告',
                            tester='city',
                            desc="city执行测试生产的报告",
                            templates=2  # 参数可选 1、2 ，展示不同风格
                            )
        runner.run()
        return reportpath

if __name__=="__main__":
    # #演示1
    # dir_path = RunAllCases().run()  #执行报告，返回报告路径
    # print(dir_path)
    # report_zip_path= dir_path+'/../91Trial自动化测试报告%s.html' % nowtime
    # zip_dir(dir_path,report_zip_path)
    # EmailUtils('PythonUI自动化测试报告(正式版)',report_zip_path).send_mail()

    # # #演示2
    dir_path=RunAllCases().run()
    print(dir_path)
    EmailUtils('PythonUI自动化测试报告',dir_path).zip_send_mail()
