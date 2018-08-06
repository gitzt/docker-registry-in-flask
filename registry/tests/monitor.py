# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-08-06 21:58:49
# @Last Modified by:   lenovo
# @Last Modified time: 2018-08-06 23:34:36


import psutil
import time
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_mail(content):
    """ 发送邮件 """

    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "ztwork18"      # 用户名
    mail_auth = "1qaz2wsx"      # 这个是授权码，不是密码
    mail_postfix = "@163.com"   # 邮箱后缀

    sender = mail_user + mail_postfix
    receivers = ["ztwork18@163.com"]

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')

    message['From'] = "%s<ztwork18@163.com>" % Header('测试','utf-8')
    message['To'] =  "%s<ztwork18@163.com>" % Header('测试','utf-8')

    subject = '警报！'
    message['Subject'] = Header(subject, 'utf-8')   # 邮箱标题

    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.login(mail_user, mail_auth)
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()
        print "邮件发送成功"
    except smtplib.SMTPException as e:
        print "Error: 无法发送邮件"
        print str(e)



if __name__ == '__main__':

    information = {'memory':{}, 'cpu':{}, 'disk':{}, 'network':{}}

    ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

    # 获取cpu使用率
    cpu = psutil.cpu_percent(0)

    # 获取内存使用率
    men = psutil.virtual_memory()

    # 获取磁盘使用率(获取磁盘"/"的容量和使用率)
    disk = psutil.disk_usage('/')

    while True:

        if cpu > :
            pass
        print psutil.virtual_memory().percent

        print psutil.cpu_percent(0)

        print psutil.disk_usage('/')

        time.sleep(5)

    # 发送邮件
    # send_mail_files(mail_host, mail_user, mail_auth, sender, receivers)

