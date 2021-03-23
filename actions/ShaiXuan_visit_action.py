#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/11/19 17:26
# @File    : ShaiXuan_visit_action.py

import time
from common.ShaiXuan_visit_page import ShaiXuan_Visit_Page



class ShaiXuanVisitAtion:
    def __init__(self,driver):
        self.SX_Visit_page = ShaiXuan_Visit_Page(driver)

    def click_VisitInfo_module_button(self):
        self.SX_Visit_page.VisitInfo_module_button()

    def click_visit_date_input(self,date_info):
        time.sleep(3)
        self.SX_Visit_page.visit_date_input(date_info)



    def click_visit_date_submitAfter_button(self,date_info):
        time.sleep(3)
        self.SX_Visit_page.visit_date_submitAfter_button()
        time.sleep(3)
        self.click_visit_date_input(date_info)

    def click_patient_name_button(self,name_info):
        time.sleep(3)
        self.SX_Visit_page.patient_name_button(name_info)

    def click_patient_name_submitAfter_button(self,name_info):
        time.sleep(3)
        self.SX_Visit_page.patient_name_submitAfter_button()
        time.sleep(3)
        self.click_patient_name_button(name_info)

    def click_randomNumber_button(self,random_info):
        time.sleep(3)
        self.SX_Visit_page.randomNumber_button(random_info)


    def click_randomNumber_submitAfter_button(self,random_info):
        time.sleep(3)
        self.SX_Visit_page.randomNumber_submitAfter()
        time.sleep(3)
        self.click_randomNumber_button(random_info)

    def click_Liver_puncture_submitAfter_button(self):
        time.sleep(3)
        self.SX_Visit_page.Liver_puncture_submitAfter_button()


    def click_Liver_puncture_button(self):
        time.sleep(3)
        self.SX_Visit_page.Liver_puncture_button()


    def click_Non_hepatic_penetration_button(self):
        time.sleep(3)
        self.SX_Visit_page.Non_hepatic_penetration_button()

    def click_birthday_button(self,birthday_info):
        time.sleep(3)
        self.SX_Visit_page.birthday_button(birthday_info)

    def click_birthday_submitAfter_button(self,birthday_info):
        time.sleep(3)
        self.SX_Visit_page.birthday_submitAfter_button()
        time.sleep(3)
        self.click_birthday_button(birthday_info)



    def click_sex_men_button(self):
        time.sleep(3)
        self.SX_Visit_page.sex_men_button()

    def click_sex_women_button(self):
        time.sleep(3)
        self.SX_Visit_page.sex_women_button()

    def click_height_button(self, height_info):
        time.sleep(3)
        self.SX_Visit_page.height_button(height_info)

    def click_group_ETV_button(self):
        time.sleep(3