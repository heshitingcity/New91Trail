import os
import time
import zipfile
from Utils.config_utils import local_config

def zip_dir(dir_path, zip_path):
    '''

    :param dir_path: 目标文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    '''
    zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        file_path = root.replace(dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
        # 循环出一个个文件名
        for filename in filenames:
            zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
    zip.close()

current_path = os.path.abspath(os.path.dirname(__file__))
smtp_file_path = os.path.join( current_path , '..' , local_config.report_path,'91Trail自动化测试报告%s.zip'%time.strftime('%Y-%m-%d'))
dir_path = os.path.join( current_path , '..' , local_config.report_path )
zip_dir(dir_path,smtp_file_path)