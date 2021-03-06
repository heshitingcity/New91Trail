import os
import xlrd
from Utils.config_utils import local_config

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'..',local_config.element_info_path)

class ElementDataUtils(object):
    def __init__(self,module,page_name,element_path=excel_path):
        # self.element_path=element_path
        self.element_path=os.path.join(element_path,module,page_name+'.xlsx')
        self.workbook = xlrd.open_workbook(self.element_path)
        self.sheet=self.workbook.sheet_by_index(0)
        self.row_count=self.sheet.nrows

    def get_element_info(self):
        element_infos={}
        for i in range(1,self.row_count):
            element_info={}
            element_info['element_name']=self.sheet.cell_value(i,1)
            element_info['locator_type'] = self.sheet.cell_value(i, 2)
            element_info['locator_value'] = self.sheet.cell_value(i, 3)
            timeout_value = self.sheet.cell_value(i, 4)
            element_info['timeout'] = timeout_value if isinstance(timeout_value,float) else local_config.time_out
            element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__=="__main__":
    elements=ElementDataUtils('main','comment_page').get_element_info()
    # print(elements)
    for element_info in elements.values():
        print(element_info)

