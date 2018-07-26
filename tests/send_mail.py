# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_mail(mail_host, mail_user, mail_auth, sender, receivers):
    """ 这是一个纯文本邮件 """
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = "%s<ztwork18@163.com>" % Header('测试','utf-8')
    message['To'] =  "%s<ztwork18@163.com>" % Header('测试','utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

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


def send_mail_files(mail_host, mail_user, mail_auth, sender, receivers):
    """ 这是一个带附件的邮件 """
    message = MIMEMultipart()
    message['From'] = "%s<ztwork18@163.com>" % Header('测试','utf-8')
    message['To'] =  "%s<ztwork18@163.com>" % Header('测试','utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件，传送config.ini文件
    att = MIMEText(open('config.ini', 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="config.ini"'    # filename可以随意取，最终在邮件中看到的名字
    message.attach(att)

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
    mail_host = "smtp.163.com"
    mail_user = "ztwork18"
    mail_auth = "1qaz2wsx"      # 这个是授权码，不是密码
    mail_postfix = "@163.com"

    sender = mail_user + mail_postfix
    receivers = ["ztwork18@163.com"]

    # 发送邮件
    send_mail_files(mail_host, mail_user, mail_auth, sender, receivers)
