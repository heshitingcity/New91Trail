from Utils.element_data_utils import ElementDataUtils
from common.base_page import BasePage

class addPatient_CRC_Page(BasePage):
    def __init__(self,driver):
        super().__init__(driver)  # 子类显示调用父类的构造方
        #元素定位信息
        elements = ElementDataUtils('main', 'addPatient_CRC_page').get_element_info()


        self.VisitInfo_module       =   elements['VisitInfo_module']
        self.visi_date              =   elements['visi_date']
        self.visi_date_submitAfter  =   elements['visi_date_submitAfter']
        self.patient_name           =   elements['patient_name']
        self.patient_name_submitAfter    =   elements['patient_name_submitAfter']
        self.randomNumber                =   elements['randomNumber']
        self.randomNumber_submitAfter    =   elements['randomNumber_submitAfter']
        self.Liver_puncture_submitAfter  =   elements['Liver_puncture_submitAfter']
        self.Liver_puncture              =   elements['Liver_puncture']  #肝穿
        self.Non_hepatic_penetration     =   elements['Non-hepatic_penetration']  #非肝穿

    def VisitInfo_module_button(self):
        self.click(self.VisitInfo_module)

    def visi_date_input(self,data_info):
        self.delete_element_attribute(self.visi_date,'maxlength')
        self.input(self.visi_date,data_info)

    def visi_date_submitAfter_button(self):
        self.click(self.visi_date_submitAfter)

    def patient_name_button(self):
        self.click(self.patient_name)

    def randomNumber_button(self):
        self.click(self.randomNumber)

    def UK_button(self):
        self.click(self.UK)



        self.birthday            =   elements['birthday']
        self.birthday_submitAfter   =   elements['birthday_submitAfter']
        self.sex_men         = elements['sex_men']
        self.sex_women       = elements['sex_women']
        self.height          = elements['height']
        self.group_ETV       = elements['group_ETV']
        self.group_ETV_IFN   = elements['group_ETV_IFN']
        self.group_ETV_Thy   = elements['group_ETV_Thy']



    def yes_you_button(self):
        self.click(self.yes_you)

    def no_meiyou_button(self):
        self.click(self.no_meiyou)

    def yes_shi_button(self):
        self.click(self.yes_shi)

    def no_fou_button(self):
        self.click(self.no_fou)

    def NA_button(self):
        self.click(self.no_meiyou)

    def UK_button(self):
        self.click(self.UK)
