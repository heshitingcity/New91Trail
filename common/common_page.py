

from Utils.element_data_utils import ElementDataUtils
from common.base_page import BasePage

class CommonPage(BasePage):
    def __init__(self,driver):
        super(CommonPage,self).__init__(driver)  # 子类显示调用父类的构造方
        elements = ElementDataUtils('main', 'comment_page').get_element_info()
    #01、搜索项目
        self.projectSearch_input   =  elements['projectSearch_input']
        self.projectSearch_button  =  elements['projectSearch_button']
        self.click_project         =  elements['click_project']
        self.enter_search_project  =  elements['enter_search_project']
        self.chose_project         =  elements['chose_project']

    #02、退出登录
        self.username_clickbox     =  elements['username_clickbox']
        self.loginout_button       =  elements['loginout_button']

    #03、选择菜单
        self.index_menu      = elements['index_menu']
        self.patient_menu    = elements['patient_menu']
        self.visit_menu      = elements['visit_menu']
        self.taskmanage_menu = elements['taskmanage_menu']

    #04、选择访视
        self.ChooseVisit_frist   = elements['ChooseVisit_frist']  #筛选访视
        self.Vist_104_button = elements['Vist_104_button']  #104
        self.OtherVist_1      = elements['OtherVist_1']  #计划外

    #05、患者，访视搜索条件
        self.Name_Numb_search  = elements['Name_Numb_search']
        self.Name_Numb_button  = elements['Name_Numb_button']
        self.choose_visit_type = elements['choose_visit_type']
        self.choose_visit_104      = elements['choose_visit_104']

    #06、新增患者
        self.create_new_patient = elements['create_new_patient']
        self.operation_button   = elements['operation_button']
        self.deleteVisit        = elements['deleteVisit']
        self.saveModule       = elements['saveModule']
        self.submitModule     = elements['submitModule']
        self.visti_submit     = elements['visti_submit']
        self.picture_Upload   = elements['picture_Upload']


    #访视缺失
        self.miss_visit     = elements['miss_visit']
        self.defaul_select  = elements['defaul_select']
        self.defaul_option  = elements['defaul_option']
        self.option_1       = elements['option_1']
        self.option_2       = elements['option_2']
        self.option_3       = elements['option_3']
        self.option_4       = elements['option_4']
        self.other_reason   = elements['other_reason']

    #操作控件
        self.saveModule       = elements['saveModule']
        self.submitModule     = elements['submitModule']
        self.visti_submit     = elements['visti_submit']
        self.description      = elements['description']
        self.save_button      = elements['save_button']
        self.all_pass         = elements['all_pass']
        self.PdPvType         = elements['PdPvType']
        self.PdPvType_1       = elements['PdPvType_1']
        self.PdPvType_2       = elements['PdPvType_2']

        self.visit_back       = elements['visit_back']
        self.visit_back_input = elements['visit_back_input']
        self.cancel_button    = elements['cancel_button']
        self.confirm_button   = elements['confirm_button']
        self.determine_button = elements['determine_button']

        self.pass_button       = elements['pass_button']
        self.field_question   = elements['field_question']
        self.questionType     = elements['questionType']
        self.questionType_default  = elements['questionType_default']
        self.questionType_1   = elements['questionType_1']
        self.questionType_2   = elements['questionType_2']
        self.questionType_3   = elements['questionType_3']
        self.questionType_4   = elements['questionType_4']
        self.questionType_5   = elements['questionType_5']
        self.questionType_6   = elements['questionType_6']
        self.questionType_7   = elements['questionType_7']
        self.data_miss        = elements['data_miss']
        self.questionType_9   = elements['questionType_9']
        self.questionType_10  = elements['questionType_10']

        self.other   = elements['other']

    #图片缺图、质疑操作
        self.cannel_miss_pic_remind   = elements['cannel_miss_pic_remind']
        self.cannel_miss_pic_input    = elements['cannel_miss_pic_input']
        self.miss_pic_remind   = elements['miss_pic_remind']
        self.miss_pic_input    = elements['miss_pic_input']
        self.click_pic         = elements['click_pic']
        self.pic_question      = elements['pic_question']
        self.pic_fuzzy         = elements['pic_fuzzy']
        self.pic_Inconsistent  = elements['pic_Inconsistent']
        self.pic_question_remark   = elements['pic_question_remark']
        self.back              = elements['back']
        self.delete_pic        = elements['delete_pic']
        self.OCR               = elements['OCR']
        self.start_ocr         = elements['start_ocr']
        self.rotation_pic      = elements['rotation_pic']

        self.yes_you   = elements['yes_you']
        self.no_meiyou = elements['no_meiyou']
        self.no_fou    = elements['no_fou']
        self.NA        = elements['NA']
        self.UK        = elements['UK']
        self.signature_shi   = elements['signature_shi']
        self.third_Year_shi   = elements['third_Year_shi']
        self.signature_fou   = elements['signature_fou']
        self.third_Year_fou   = elements['third_Year_fou']



    def yes_you_button(self):
        self.click(self.yes_you)

    def no_meiyou_button(self):
        self.click(self.no_meiyou)

    def signature_shi_button(self):
        self.click(self.signature_shi)

    def third_Year_shi_button(self):
        self.click(self.third_Year_shi)

    def signature_fou_button(self):
        self.click(self.signature_fou)

    def third_Year_fou_button(self):
        self.click(self.third_Year_fou)


    def no_fou_button(self):
        self.click(self.no_fou)

    def NA_button(self):
        self.click(self.no_meiyou)

    def UK_button(self):
        self.click(self.UK)

#图片缺图、质疑
    def OCR_button(self):
        self.click(self.OCR)

    def Start_ocr(self):
        self.click(self.start_ocr)

    def rotation_pic_button(self):
        self.click(self.rotation_pic)

    def cannel_miss_pic_remind_button(self):
        self.click(self.cannel_miss_pic_remind)

    def Cannel_miss_pic_input(self,cannel_miss_reason):
        self.input(self.cannel_miss_pic_input,cannel_miss_reason)

    def miss_pic_remind_button(self):
        self.click(self.miss_pic_remind)

    def Miss_pic_input(self,miss_reason):
        self.input(self.miss_pic_input,miss_reason)

    def click_first_pict(self):
        self.click(self.click_pic)

    def Pic_question_button(self):
        self.click(self.pic_question)

    def Pic_fuzzy(self):
        self.click(self.pic_fuzzy)

    def Pic_Inconsistent(self):
        self.click(self.pic_Inconsistent)

    def Pic_question_remark(self,remark_info):
        self.input(self.pic_question_remark,remark_info)

    def back_button(self):
        self.click(self.back)

    def delete_pic_button(self):
        self.click(self.delete_pic)

#修改的说明、保存、质疑原因、一键通过、字段通过、质疑
    def saveModule_button(self):
        self.click(self.saveModule)

    def submitModule_button(self):
        self.click(self.submitModule)

    def visti_submit_button(self):
        self.click(self.visti_submit)

    def description_input(self,description_info):  #说明/原因输入框
        self.input(self.description,description_info)

    def Save_button(self):
        self.click(self.save_button)

    def all_pass_button(self):  #一键通过
        self.click(self.all_pass)


#访视打回
    def visit_back_button(self):
        self.click(self.visit_back)

    def Visit_back_input(self,reason_info):
        self.input(self.visit_back_input,reason_info)

    def Cancel_button(self):  #取消
        self.click(self.cancel_button)

    def Confirm_button(self):  #确认
        self.click(self.confirm_button)

    def Determine_button(self):  #确定
        self.click(self.determine_button)


#字段质疑、通过
    def Pass_button(self):  #通过
        self.click(self.pass_button)

    def PdPvType_button(self):
        self.click(self.PdPvType)

    def PdPvType_1_button(self):   #方案违背
        self.click(self.PdPvType_1)

    def PdPvType_2_button(self):  #方案偏离
        self.click(self.PdPvType_2)


    def field_question_button(self):
        self.click(self.field_question)

    def questionType_button(self):
        self.click(self.questionType)

    def questionType_default_button(self):
        self.click(self.questionType_default)

    def questionType_1_button(self):
        self.click(self.questionType_1)

    def questionType_2_button(self):
        self.click(self.questionType_2)

    def questionType_3_button(self):
        self.click(self.questionType_3)

    def questionType_4_button(self):
        self.click(self.questionType_4)

    def questionType_5_button(self):
        self.click(self.questionType_5)

    def questionType_6_button(self):
        self.click(self.questionType_6)

    def questionType_7_button(self):
        self.click(self.questionType_7)

    def data_miss_button(self):
        self.click(self.data_miss)

    def questionType_9_button(self):
        self.click(self.questionType_9)

    def questionType_10_button(self):
        self.click(self.questionType_10)

    def other_button(self):
        self.click(self.other)




#访视缺失
    def Defaul_select(self):
        self.click(self.defaul_select)

    def Defaul_option(self):
        self.click(self.defaul_option)

    def Option_1(self):  #未联系到患者
        self.click(self.option_1)

    def Option_2(self): #患者确认本次访视未访
        self.click(self.option_2)

    def Option_3(self): #结束治疗
        self.click(self.option_3)

    def Option_4(self): #中止治疗
        self.click(self.option_4)

    def Other_reason(self,text_info):  #其他原因文本框
        self.input(self.other_reason,text_info)


    def Create_new_patient(self):  # 新增患者按钮
        self.click(self.create_new_patient)

# 删除访视
    def Delete_visit(self):
        self.click(self.deleteVisit)


 # 访视缺失
    def Miss_visit(self):
        self.click(self.miss_visit)

# 操作按钮
    def Operation_button(self):
        self.click(self.operation_button)

    def SaveModule(self):  # 模块保存
        self.click(self.saveModule)

# 模块提交
    def SubmitModule(self):
        self.click(self.submitModule)

# 访视提交
    def Visti_submit(self):
        self.click(self.visti_submit)

# 图片上传
    def Picture_Upload(self,picture_path):
        self.input(self.picture_Upload,picture_path)


#患者搜索
    def patient_search1(self,Patient_info):
        self.input(self.Name_Numb_search,Patient_info)

    def patient_search_button(self):
        self.click(self.Name_Numb_button)


#访视筛选条件搜索
    def visit_type_default_chose(self):
        self.click(self.choose_visit_type)

    def choose_visit_name(self): #104
        self.click(self.choose_visit_104)



#点击访视
    def choose_SX_visit(self):  #筛选访视
        self.click(self.ChooseVisit_frist)

    def choose_JX_visit(self):
        self.click(self.Vist_104_button)

    def choose_JHW_visit(self):  #计划外访视
        self.click(self.OtherVist_1)



#账号退出
    def click_username(self):
         self.click(self.username_clickbox)

    def click_loginout_button(self):
        self.click(self.loginout_button)



#项目名称搜索
    def ProjectSearch_input(self,projectName):  #输入查找项目名称
        self.input(self.projectSearch_input,projectName)

    def ProjectSearch_button(self):
        self.click(self.projectSearch_button)

    #点击搜索后的项目名称1
    def Click_project(self):
        self.click(self.click_project)

    #项目搜索访视2
    def Enter_search_project(self):
        self.click(self.click_project)