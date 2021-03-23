import  os
import  time
from common import HTMLTestReportCN
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from Utils.log_utils import logger
from Utils.config_utils import local_config
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver # webdriver.Chrome() driver

    #f封装浏览器操作
    def open_url(self,url):
        try:
             self.driver.get(url)
             logger.info('打开url地址: %s'%url)
        except Exception as e:
            logger.error('不能打开指定的测试网址，原因是：%s'%e.__str__())

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    #   隐式等待
    def implicitly_Wait(self,senconds):
        self.driver.implicitly_wait(senconds)

    def wait(self,senconds=local_config.time_out):
        self.driver.wait(senconds)

    def set_browser_min(self):
        self.driver.maximize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        try:
            title=self.driver.title
            logger.info('获取浏览器标题，标题为： %s'%title)
        except Exception as e:
            logger.error('获取浏览器标题失败，原因是：%s'%e.__str__())
        return title

    def get_url(self):
        url = self.driver.current_url
        logger.info('获取浏览器url，url为： %s' %url)
        return

    def close_tab(self):
        logger.info('关闭浏览器 当前浏览器窗口')
        self.driver.close()

    def exit_driver(self):
        logger.info('关闭浏览器')
        self.driver.quit()


    # 页面提供的元素识别字段
        # element_info={'element_name': '用户名输入框',
        #                  'locator_type': 'xpath',
        #                  'locator_value': '//input[@name="account"]',
        #                  'timeout': 5}
    #元素识别封装
    def find_element(self,element_info):
        '''
        :param element_info: 元素信息，字典类型{}
        :return: element 元素
        '''
        try:
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout =   element_info['timeout']
            if locator_type_name=='id':
                 locator_type=By.ID
            elif locator_type_name=='name':
                 locator_type =By.NAME
            elif locator_type_name =='xpath':
                locator_type = By.XPATH
            elif locator_type_name == 'css':
                locator_type =By.CSS_SELECTOR
            self.implicitly_Wait(10)
            element = WebDriverWait(self.driver, locator_timeout).until(lambda x: x.find_element(locator_type,locator_value_info))
            # logger.info('[%s] 元素识别成功'%element_info['element_name'])
        except Exception as e:
            logger.error('[%s] 元素识别失败，原因是： %s'%(element_info['element_name'],e.__str__()))
        return  element

    #元素操作封装
    def click(self,element_info):
        try:
            element=self.find_element(element_info)
            element.click()
            # logger.info('[%s] 元素进行了点击操作'%element_info['element_name'])
        except Exception as e:
            logger.error('[%s] 元素点击操作失败，原因是：%s' %(element_info['element_name'], e.__str__()))


    def input(self,element_info,content):
        try:
            element=self.find_element(element_info)
            element.send_keys(content)
            # logger.info('[%s]元素输入数据: %s'%(element_info['element_name'],content))
        except Exception as e:
            logger.error('[%s]元素输入数据失败，原因是：%s' % (element_info['element_name'], e.__str__()))



    #获取文本信息
    def get_text(self,element_info):
        try:
            element = self.find_element(element_info)
            text_value=element.text
            logger.info('[%s]元素的text信息已获取到，为:[%s]' % (element_info['element_name'], text_value))
        except Exception as e:
            logger.error('[%s]元素获取text信息失败，原因是：%s' % (element_info['element_name'], e.__str__()))
        return text_value



    #  鼠标键盘操作 （建议：先判断操作系统的类型） --单个封装
    #鼠标悬停
    def move_to_element_by_mouse(self,element_info):
        element=self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()
        logger.info('元素hover')

    # 右击
    def right_click_element(self,element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).context_click(element).perform()
        logger.info('元素右击')

    # 演示2： 双击
    def double_click_element(self,element_info):
        element=self.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()
        logger.info('元素双击')

    #回车
    def press_enter_key(self,element_info):
        try:
            self.find_element(element_info).send_keys(Keys.ENTER)
        except Exception as e:
            raise e


    #屏幕滚动
    def Scroll_top(self):
        JS="var action=document.documentElement.scrollTop=0"
        self.driver.execute_script(JS)

    def Scroll_buttom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        logger.info('屏幕滚动到底部')


   #执行js的封装
     #继续封装selenium 执行js的脚本
    def __execute_script(self,js_str,element_info=None):
        if element_info:
            element = self.find_element(element_info)
            self.driver.execute_script(js_str,element)
        else:
            self.driver.execute_script(js_str)

    #删除元素的一个属性
    def delete_element_attribute(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)
        logger.info('删除[{0}]的属性：{1}'.format(element_info['element_name'],attribute_name))

    #改元素的属性
    def update_element_attribute(self,element_info,attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value), element)
        logger.info('修改[{}]的属性：{}'.format(element_info,attribute_name))


    # 切框架
    #思路1：
    # def switch_to_frame(self,element_info):
    #     element = self.find_element(element_info)
    #     self.driver.switch_to.frame(element)
    #
    # #思想2：
    # def switch_to_frame_id_or_name(self,id_or_name):  #id=frame
    #     self.driver.switch_to.frame(id_or_name)
    # def switch_to_frame_by_element(self,element_info): #element_info
    #     element = self.find_element(element_info)
    #     self.driver.switch_to.frame(element)

    # 切框架思想3：
    def switch_to_frame(self,**element_dict): #id=frame element=element_info
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in  element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element_info'])
            self.driver.switch_to.frame(element)

    #弹出框的处理
    def switch_to_alert(self,action='accept',time_out=local_config.time_out):
        self.wait(time_out)
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        alert_text = alert.text
        if action== 'accept':
            alert.accept()
        else:
            alert.dismiss()
        return  alert_text

    #封装切句柄
    def get_window_handle(self):
          return self.driver.current_window_handle

    def switch_to_window_by_handle(self,window_handle):
        self.driver.switch_to.window(window_handle)

    def switch_to_window_by_title(self,title):
         window_handles=self.driver.window_handles
         for window_handle in window_handles:
              if  WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                  self.driver.switch_to.window(window_handle)
                  break

    def switch_to_window_by_url(self,url):
         window_handles=self.driver.window_handles
         for window_handle in window_handles:
              if WebDriverWait(self.driver,local_config.time_out).until(EC.url_contains(url)):
                  self.driver.switch_to.window(window_handle)
                  break

    # 报告中添加截图
    def screenshot_as_file(self):
        report_path = os.path.join( os.path.abspath(os.path.dirname(__file__)) , '..', local_config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot( self.driver )

    # 截图：
    def  screenshot(self,*screenshot_path):
          if len(screenshot_path)==0:
              screenshot_filepath=local_config.screent_shot_path
          else:
              screenshot_filepath=screenshot_path[0]
          now = time.strftime('%Y_%m_%d_%H_%M_%S')
          current_dir=os.path.dirname(__file__)
          screenshot_filepath=os.path.join(current_dir,'..',screenshot_filepath,'UItest_%s.png'%now)
          self.driver.get_screenshot_as_file(screenshot_filepath)



    #固定时间等待
    def default_wait(self,timeout=local_config.time_out):
        time.sleep(timeout)
        logger.info("a")