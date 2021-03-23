#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/11/19 17:53
# @File    : addPatient_case_test.py


import unittest
from common.Stard_End import StarEnd
from actions.login_ation import LoginAction
from actions.common_action import CommonPageAction
from common.common_page import BasePage
from actions.ShaiXuan_visit_action import ShaiXuanVisitAtion
from Utils.test_case_data_utils import TestDataUtils
from Utils.log_utils import logger
from unittestreport import TestRunner


class addPatient_case(StarEnd):
    test_case_data = TestDataUtils('common_suite', 'addPatient_case_data').convert_exceldata_to_testdata()

    @unittest.skipIf(test_case_data['test_addPatient_success']['isnot'],'条件为真则跳过')
    def test_addPatient_success(self):
        logger.info('test_addPatient_success 用例开始执行')
        test_function_data = self.test_case_data['test_addPatient_success']
        self._testMethodDoc = test_function_data['test_name']
        LoginAction(self.base_page.driver).login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        CommonPage = CommonPageAction(self.base_page.driver)
        CommonPage.project_search_way01(test_function_data['test_parameter'].get('模糊搜索'))
        CommonPage.chose_patient_menu()
        CommonPage.AddNewPatient()
        ShaiXuanVisit = ShaiXuanVisitAtion(self.base_page.driver)
        ShaiXuanVisit.click_visit_date_input(test_function_data['test_parameter'].get('访视日期'))
        base_page = BasePage(self.base_page.driver)
        ShaiXuanVisit.click_patient_name_button(base_page.random_name())
        ShaiXuanVisit.click_randomNumber_button(base_page.random_numb(5))
        ShaiXuanVisit.click_Liver_puncture_button()
        ShaiXuanVisit.click_Non_hepatic_penetration_button()
        ShaiXuanVisit.click_birthday_button(test_function_data['test_parameter'].get('出生日期'))
        ShaiXuanVisit.click_sex_men_button()
        ShaiXuanVisit.click_height_button(test_function_data['test_parameter'].get('身高'))
        base_page.Scroll_buttom()
        ShaiXuanVisit.click_group_ETV_button()
        CommonPage.No_meiyou_button()
        CommonPage.Signature_shi_button()
        CommonPage.Third_Year_fou_button()
        CommonPage.Third_Year_shi_button()
        CommonPage.saveModule()
        CommonPage.upload_picture(test_functio