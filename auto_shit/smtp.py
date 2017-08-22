# -*-coding:utf8-*-
import smtplib
import traceback
import ConfigParser
import datetime
from create_example import Suites
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def sendmail(address):
    # @subject:邮件主题
    # @msg:邮件内容
    # @toaddrs:收信人的邮箱地址
    # @fromaddr:发信人的邮箱地址
    # @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    # @password:发信人的邮箱密码
    read_config = ConfigParser.RawConfigParser()
    read_config.read('test')
    mailsubject = read_config.get('mail', 'subject') +str(datetime.datetime.now())
    toaddrs =  read_config.get('mail', 'receiver')
    fromaddr = read_config.get('mail', 'sender')
    password = read_config.get('mail','sender_passowrd')
    smtpaddr = read_config.get('mail', 'stmpaddr')
    msg = read_config.get('mail','msg')
    mail_msg = MIMEMultipart()
    if not isinstance(mailsubject,unicode):
        mailsubject = unicode(mailsubject,'utf-8')
    mail_msg['Subject'] = mailsubject
    mail_msg['From'] =fromaddr
    mail_msg['To'] = toaddrs
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
    result_msg = MIMEApplication(open(address,'rb').read())
    result_msg.add_header('Content-Disposition', 'attachment', filename='result.html')
    mail_msg.attach(result_msg)
    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)  #连接smtp服务器
        s.login(fromaddr, password)  #登录邮箱
        s.sendmail(fromaddr, toaddrs.split(','), mail_msg.as_string()) #发送邮件
        s.quit()
    except Exception:
       print "Error: unable to send email"
       print traceback.format_exc()


if __name__ == '__main__':
    suite_obj = Suites()
    mailpath = suite_obj.casesuite()
    sendmail(mailpath)
