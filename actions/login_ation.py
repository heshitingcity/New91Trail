
import time
from common.login_page import LoginPage
from common.common_page import CommonPage
from Utils.log_utils import logger
from Utils.config_utils import local_config

class LoginAction:
    def __init__(self,driver):
        self.login_page=LoginPage(driver)


    def login_action(self,username,password):
        time.sleep(3)
        self.login_page.input_username(username)
        time.sleep(3)
        self.login_page.input_password(password)
        time.sleep(3)
        self.login_page.click_login()
        logger.info('输入的账号是：%s,  密码是：%s'%(username,password))
        return CommonPage(self.login_page.driver)

    def login_success(self,username,password):
        self.login_action(username,password)




    def login_fail(self,username,password):
        self.login_action(username,password)
        # return self.login_page.get_login_fail_alert_content()


    #默认登录成功
    def default_login(self):
        self.login_action(local_config.username,local_config.password)
        logger.info('默认的账号，密码登录成功！')
        return CommonPage(self.login_page.driver)


        #扩展
    def login_by_cookie(self):
        pass
