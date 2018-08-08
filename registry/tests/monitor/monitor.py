# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-08-06 21:58:49
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-08 11:01:04


import psutil
import time
import socket
import smtplib,base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def get_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def get_memory():
    """
    获取内存信息
    :return：dict(memory_info)
    """
    memKeys = ['total','available','used','free','percent']
    mem = psutil.virtual_memory()
    memory_info = {key:getattr(mem, key) for key in dir(mem) if key in memKeys}
    return memory_info

def get_disk():
    """
    获取根目录"/"的磁盘信息
    :return：dict(disk_info)
    """
    diskKeys = ['total','used','free','percent']
    disk = psutil.disk_usage('/')
    disk_info = {key:getattr(disk, key) for key in dir(disk) if key in diskKeys}
    return disk_info

def send_mail(content):
    """ 发送邮件 """

    # 邮件配置
    mail_host = "10.27.0.214"                       # 服务器地址
    sender = "zhuangtao.fang@genlot.com"            # 发件人
    receivers = [                                   # 收件人列表
        "zhuangtao.fang@genlot.com",
    ]
    username = "zhuangtao.fang@genlot.com"          # 用户名
    password = base64.b64decode("NjY2ODg4Znp0")     # 邮箱密码

    # 邮件正文
    warn_info = "告警主机: %s \
    \n告警时间：%s \
    \nCPU使用率：%s%% \
    \n内存使用率：%s%% \
    \n磁盘使用率：%s%% \
    " % (content['ip'], content['date'], content['cpu'], content['memory']['percent'], content['disk']['percent'])
    message = MIMEText(warn_info, 'plain', 'utf-8')

    # 邮件标题、发件人、收件人
    subject = u'资源消耗预警 -- 服务器%s资源占用高！ ' % content['ip']
    message['Subject'] = Header(subject, 'utf-8')   # 邮箱标题
    message['From'] = "zhuangtao.fang@genlot.com"
    message['To'] = ','.join(receivers)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.login(username, password)
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()
        print "邮件发送成功！"
        return True
    except smtplib.SMTPException as e:
        print "Error: 邮件发送失败！"
        print str(e)
        return False

if __name__ == '__main__':

    information = {}
    # 判断标识，True：今天已发过邮件，不再发送；False：今天未发过邮件。
    is_send_today = False
    last_send_time = None

    ip = get_ip()
    information['ip'] = ip

    while True:
        time.sleep(60)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 获取cpu使用率
        cpu = psutil.cpu_percent(0)

        # 获取内存使用率
        memory = get_memory()

        # 获取磁盘使用率(获取磁盘"/"的容量和使用率)
        disk = get_disk()
        
        if cpu >= 80 or memory['percent'] >= 90 or disk['percent'] >= 90:
            information['date'] = now
            information['cpu'] = cpu
            information['memory'] = memory
            information['disk'] = disk

            if is_send_today == False:
                # 发送邮件
                send_mail(information)
                last_send_time = now[0:10]
                is_send_today = True
            else:
                print "%s 今天已发送过邮件，请及时处理！" % now

        # 每天重置邮件发送状态
        today = time.strftime("%Y-%m-%d", time.localtime())
        if today > last_send_time:
            is_send_today = False


