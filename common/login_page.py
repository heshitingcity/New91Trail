#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/14 20:18
# @File    : loginout.py
# @software: PyCharm


from common.base_page import BasePage
from Utils.element_data_utils import ElementDataUtils


class LoginPage(BasePage):    #类--页面
    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)  #子类显示调用父类的构造方
        elements = ElementDataUtils('login', 'login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button      = elements['login_button']

    def input_username(self,username):  #方法--控件的操作
         self.input(self.username_inputbox,username)

    def input_password(self,password):
        self.input(self.password_inputbox,password)

    def click_login(self):
        self.click(self.login_button)

    def get_login_fail_alert_content(self):
        return self.switch_to_alert()





