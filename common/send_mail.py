#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：config.py 
@File    ：send_mail.py
@Author  ：SpringBear
@Date    ：2024/8/16 15:18
增加邮件服务:
目前支持发件人为163邮箱，支持多个收件人，支持发送附件（单个附件）
"""
# coding=utf-8
from email.mime.text import MIMEText
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import config

def send_email_with_attachment(sender_email, receiver_email, password, attachment_path, attachment_name, email_subject,
                               email_body):
    # 创建邮件对象并设置邮件格式
    message = MIMEMultipart()
    message['From'] = sender_email

    if isinstance(receiver_email, str):
        message['To'] = receiver_email
    else:
        message['To'] = ','.join(receiver_email)

    # message['To'] = receiver_email
    message['Subject'] = email_subject
    message['date'] = time.strftime('%Y-%m-%d-%H_%M_%S')


    # 添加邮件正文
    message.attach(MIMEText(email_body, 'plain'))

    # 添加附件
    attachment = MIMEApplication(open(attachment_path, 'rb').read())
    attachment.add_header('Content-Disposition', 'attachment', filename=attachment_name)
    message.attach(attachment)

    # 发送邮件
    try:
        mailhost = 'smtp.163.com'

        server = smtplib.SMTP(mailhost,25)
        # server.connect(mailhost,25) # 使用Gmail服务，如果是其他服务商请更改服务器和端口
        server.starttls()  # 启用TLS
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.close()
        print('Email sent successfully')
    except Exception as e:
        print('Failed to send email. Error:', e)

# 使用示例
send_email_with_attachment(
    'fivemsbear@163.com',  # 发件人邮箱
    ['2013099087@qq.com','2574284191@qq.com'],  # 收件人邮箱
     config.mailcode,  # 发件人邮箱密码
    '../report/unittest01.html',  # 附件路径
    'unittest01.html',  # 附件名称
    '测试邮件发送',  # 邮件主题
    '测试报告已添加至附件'  # 邮件正文
)


