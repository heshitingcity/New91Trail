# encoding: utf-8
#@author: city
#@file: Stard_End.py
#@time: 2020-08-12 20:27

import time
import unittest
from Utils.config_utils import  local_config
from common.browser import  Browser
from common.base_page import BasePage
from Utils.log_utils import logger
from actions.common_action import CommonPageAction


class StarEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info('=====================测 试 类 初 始 化=====================')


    def setUp(self):
        '''
         测试用例的初始化
        :return:
        '''
        logger.info('--------测试方法初始化---------------')
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_Wait(10)
        self.base_page.open_url(local_config.url)


    def tearDown(self):
        # 测试用例失败的截图
        errors = self._outcome.errors
        for test,exc_info in errors: #断言失败，就会有错误的信息
            if exc_info:
                self.base_page.default_wait()
                # self.base_page.screenshot()  # 截图
        self.base_page.implicitly_Wait(10)
        CommonPageAction(self.base_page.driver).quit()
        self.base_page.exit_driver()
        logger.info('--------测试方法执行完毕---------------')



    @classmethod
    def tearDownClass(cls):
        logger.info('=====================测 试 类 执 行 完 毕=====================')




if __name__ == '__main__':
    unittest.main(verbosity=2)