
import os
import time
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Utils.config_utils import local_config
from Utils.zip_utils import zip_dir


class EmailUtils:
    def __init__(self, smtp_body,smtp_file = None):
        self.smtp_server   = local_config.smtp_server
        self.smtp_sender   = local_config.smtp_sender
        self.smtp_password = local_config.smtp_password
        self.smtp_receiver = local_config.smtp_receiver
        self.smtp_cc       = local_config.smtp_cc
        self.smtp_subject  = local_config.smtp_subject
        self.smtp_body     = smtp_body
        self.smtp_file     = smtp_file


    def mail_content(self):
        if self.smtp_file != None:
            if self.smtp_file.split('.')[-1].__eq__('zip'):
                return self.__mail_zip_content()
            # elif 扩展
        else:
            return self.__mail_text_content()

    def mail_content_by_zip(self):
        report_zip_path = self.smtp_file + '91Trail自动化测试报告%s.zip'%time.strftime('%Y-%m-%d')
        zip_dir(self.smtp_file, report_zip_path)
        self.smtp_file = report_zip_path  # 压缩后修改为压缩路径
        msg = self.mail_content()
        return msg

    def __mail_text_content(self):
        msg = MIMEText(self.smtp_body, "html", "utf-8")
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def __mail_zip_content(self):
        msg = MIMEMultipart()
        with open(self.smtp_file, 'rb') as f:
            mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
            mime.add_header('Content-Disposition', 'attachment',
                            filename=('utf-8', '', self.smtp_file.split('/')[-1]))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        msg.attach(MIMEText(self.smtp_body, "html", "utf-8"))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg


    def send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_password)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_password)
        mail_content = self.mail_content()
        try:
            smtp.sendmail(self.smtp_sender,
                          self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                          mail_content.as_string())
        except Exception as e:
            print(e)
        smtp.quit()


    def zip_send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_password)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_password)
        mail_content = self.mail_content_by_zip()
        try:
            smtp.sendmail(self.smtp_sender,
                          self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                          mail_content.as_string())
        except Exception as e:
            print(e)
        smtp.quit()


