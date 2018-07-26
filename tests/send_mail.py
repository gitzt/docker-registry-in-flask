# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.163.com"
mail_user = "ztwork18"
mail_auth = "1qaz2wsx"      # 这个是授权码，不是密码
mail_postfix = "@163.com"


sender = mail_user + mail_postfix
receivers = ["ztwork18@163.com"]

message['From'] = "%s<ztwork18@163.com>" % Header('测试','utf-8')
message['To'] =  "%s<ztwork18@163.com>" % Header('测试','utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
 
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




