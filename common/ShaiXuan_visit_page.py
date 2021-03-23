
from Utils.log_utils import logger
from Utils.element_data_utils import ElementDataUtils
from common.base_page import BasePage

class ShaiXuan_Visit_Page(BasePage):
    def __init__(self,driver):
        super().__init__(driver)  # 子类显示调用父类的构造方
        #元素定位信息
        elements = ElementDataUtils('main', 'addPatient_CRC_page').get_element_info()
        self.VisitInfo_module       =   elements['VisitInfo_module']
        self.visit_date              =   elements['visit_date']
        self.current_date              =   elements['current_date']
        self.visit_date_submitAfter  =   elements['visit_date_submitAfter']
        self.patient_name           =   elements['patient_name']
        self.patient_name_submitAfter    =   elements['patient_name_submitAfter']
        self.randomNumber                =   elements['randomNumber']
        self.randomNumber_submitAfter    =   elements['randomNumber_submitAfter']
        self.Liver_puncture_submitAfter  =   elements['Liver_puncture_submitAfter']
        self.Liver_puncture              =   elements['Liver_puncture']  #肝穿
        self.Non_hepatic_penetration     =   elements['Non_hepatic_penetration']  #非肝穿
        self.birthday            =   elements['birthday']
        self.birthday_submitAfter   =   elements['birthday_submitAfter']
        self.sex_men         = elements['sex_men']
        self.sex_women       = elements['sex_women']
        self.height          = elements['height']
        self.group_ETV       = elements['group_ETV']
        self.group_ETV_IFN   = elements['group_ETV_IFN']
        self.group_ETV_Thy   = elements['group_ETV_Thy']



    def VisitInfo_module_button(self):
        self.click(self.VisitInfo_module)

    def visit_date_input(self,data_info):
        self.delete_element_attribute(self.visit_date,'maxlength')
        self.input(self.visit_date,data_info)
        BasePage(self.driver).press_enter_key(self.visit_date)
        logger.info('输入访视日期:%s'%data_info)


    def visit_date_submitAfter_button(self):
        self.click(self.visit_date_submitAfter)

    def patient_name_button(self,name_info):
        self.input(self.patient_name,name_info)
        logger.info('输入患者姓名： %s'%name_info)

    def patient_name_submitAfter_button(self):
        self.click(self.patient_name_submitAfter)

    def randomNumber_button(self,random_info):
        self.input(self.randomNumber,random_info)
        logger.info('输入随机号名：%s'%random_info)

    def randomNumber_submitAfter_button(self):
        self.click(self.randomNumber_submitAfter)


    def Liver_puncture_submitAfter_button(self):
        self.click(self.Liver_puncture_submitAfter)


    def Liver_puncture_button(self):
        self.click(self.Liver_puncture)
        logger.info('点击[肝穿]元素')

    def Non_hepatic_penetration_button(self):
        self.click(self.Non_hepatic_penetration)
        logger.info('点击[非肝穿]元素')

    def birthday_button(self,birthday_info):
        self.delete_element_attribute(self.birthday,'maxlength')
        self.input(self.birthday,birthday_info)
        BasePage(self.driver).press_enter_key(self.birthday)
        logger.info('点击[出生日期]元素')

    def birthday_submitAfte