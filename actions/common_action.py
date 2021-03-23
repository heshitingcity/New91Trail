#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/19 17:49
# @File    : common_action.py

import time
import unittest
from common.common_page import CommonPage
from common.login_page import LoginPage
from Utils.log_utils import logger


class CommonPageAction:
    def __init__(self,driver):
        self.common_page=CommonPage(driver)

#01、退出登录
    def quit(self):
        try:
            time.sleep(3)
            self.common_page.click_username()
            time.sleep(3)
            self.common_page.click_loginout_button()
            time.sleep(3)
            logger.info('账号退出登录成功')
        except Exception as e:
            logger.debug(e)
        return LoginPage(self.common_page.driver)


#02、搜索项目
    def project_search_action(self,ProjectName):
        time.sleep(3)
        try:
            self.common_page.ProjectSearch_input(ProjectName)
            time.sleep(3)
            self.common_page.ProjectSearch_button()
            time.sleep(3)
        except Exception as e:
            print(e)


    def project_search_way01(self,ProjectName):
        try:
            self.project_search_action(ProjectName)
            self.common_page.Click_project()
            logger.info('搜索：[%s] 项目' % ProjectName)
        except Exception as e:
            print(e)

    def project_search_way02(self,ProjectName):
        self.common_page.Enter_search_project()
        self.project_search_action(ProjectName)
        self.common_page.Chose_project()
        logger.info('搜索：[%s] 项目'%ProjectName)


#03、选择菜单
    def chose_index_menu(self):
        self.common_page.Chose_index()
        logger.info('点击：首页')

    def chose_patient_menu(self):
        self.common_page.Chose_patient()
        logger.info('点击：受试者管理')

    def chose_visit_menu(self):
        self.common_page.Chose_visit()
        logger.info('点击：访视管理')

    def chose_taskmanage_menu(self):
        self.common_page.Chose_taskmanage()
        logger.info('点击：任务管理')

#04、点击访视
    def click_SX_visit(self):  #筛选访视
        self.common_page.choose_SX_visit()
        logger.info('点击：筛选访视')

    def click_JX_visit(self):  #基线访视
        self.common_page.choose_JX_visit()
        logger.info('点击：基线访视')

    def click_JHW_visit(self):  #计划外访视
        time.sleep(3)
        self.common_page.choose_JHW_visit()
        logger.info('点击：计划外访视')

# 05、访视搜索
    def Visit_search(self):
        time.sleep(3)
        self.common_page.visit_type_default_chose()
        time.sleep(3)
        self.common_page.choose_visit_name()
        logger.info('搜索访视')

#06、患者搜索
    def Patient_search(self,patient_info):
        time.sleep(3)
        self.common_page.patient_search_button()
        self.common_page.patient_search1(patient_info)
        self.common_page.patient_search_button()
        time.sleep(3)
        logger.info('搜索: %s 患者'%patient_info)


#07、新增患者按钮
    def AddNewPatient(self):
        time.sleep(3)
        self.common_page.Create_new_patient()
        logger.info('新增患者')

#08、删除访视
    def DeleteVisit_Yes(self):
        time.sleep(3)
        self.common_page.Operation_button()
        self.common_page.deleteVisit()
        self.common_page.confirm_button()
        logger.info('删除访视')

    def DeleteVisit_No(self):
        time.sleep(3)
        self.common_page.Operation_button()
        self.common_page.deleteVisit()
        self.common_page.Cancel_button()
        logger.info('取消删除访视')

#09、访视缺失
    def MissVisit(self):
        time.sleep(3)
        self.common_page.Operation_button()
        self.common_page.Miss_visit()
        logger.info('访视缺失')

    def MissVisit_other(self,text_info):
        time.sleep(3)
        self.common_page.Operation_button()
        self.common_page.Miss_visit()
        self.common_page.defaul_select()
        self.common_page.other_reason(text_info)
        self.common_page.confirm_button()
        logger.info('访视缺失_其他#%s'%text_info)


#10、图片上传
    def upload_picture(self,picture_path):
        time.sleep(3)
        self.common_page.Picture_Upload(picture_path)
        logger.info('上传图片')

#11、修改的说明、保存、质疑原因、一键通过、字段通过、质疑
    def saveModule(self):
        time.sleep(3)
        self.common_page.saveModule_button()
        logger.info('模块保存')

    def submitModule(self):
        time.sleep(3)
        self.common_page.submitModule_button()
        logger.info('模块提交')

    def visti_submit(self):
        time.sleep(3)
        self.common_page.visti_submit_button()
        logger.info('访视提交')


    def Pass_field_1(self):
        self.common_page.Pass_button()
        self.common_page.save_button()
        logger.info('通过字段')

    def Pass_field_2(self,description_info):
        self.common_page.Pass_button()
        self.common_page.PdPvType_1_button()
        # self.common_page.PdPvType_2_button()
        self.common_page.description_input(description_info)
        self.common_page.save_button()
        logger.info('通过字段_说明: %s'%description_info)

    def question_success(self,reson_info):
        time.sleep(3)
        self.common_page.field_question_button()
        time.sleep(3)
        self.common_page.questionType_button()
        time.sleep(3)
        self.common_page.questionType_3_button()  #数据不符合规则
        time.sleep(3)
        self.common_page.description_input(reson_info)
        time.sleep(3)
        self.common_page.save_button()
        logger.info('质疑字段：数据不符合规则')


#访视打回
    def Visit_Back(self,reason_info):
        time.sleep(3)
        self.common_page.visit_back_button()
        time.sleep(3)
        self.common_page.visit_back_input(reason_info)
        time.sleep(3)
        self.common_page.confirm_button()
        logger.info('访视打回')

#模块一键通过
    def All_pass(self):
        time.sleep(3)
        self.common_page.all_pass_button()
        time.sleep(3)
        self.common_page.confirm_button()
        logger.info('模块一键通过')

#删除图片
    def delete_picture(self):
        time.sleep(3)
        self.common_page.click_first_pict()
        time.sleep(3)
        self.common_page.delete_pic_button()
        time.sleep(3)
        self.common_page.Determine_button()
        logger.info('删除图片')


#缺图提醒\取消缺图
    def miss_picture_success(self,reason_info):
        time.sleep(3)
        self.common_page.miss_pic_remind_button()
        time.sleep(3)
        self.common_page.Miss_pic_input(reason_info)
        time.sleep(3)
        self.common_page.Determine_button()
        logger.info('缺图提醒')

    def cannel_miss_picture(self,cannel_reason_info):
        time.sleep(3)
        self.common_page.Cancel_button()
        time.sleep(3)
        self.common_page.Cannel_miss_pic_input(cannel_reason_info)
        time.sleep(3)
        self.common_page.Determine_button()
        logger.info('取消缺图提醒')


if __name__ == "__main__":
    unittest.main(verbosity=2)