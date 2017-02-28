#!/usr/bin/env python3  
#coding: utf-8  
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'll-chen6@hnair.com'  
receiver = 'xxxxx'  
subject = '每周会员统计数'  
smtpserver = 'smtp.hnair.com'  
username = 'xxxxx'  
password = 'xxxxx'  

def send(path):
	msg = MIMEText('<html><h1>倩云，你好，附件里是本周的数据</h1></html>','html','utf-8')  

	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = Header(subject, 'utf-8')

	title = '每周会员统计数.xlsx'.decode('utf-8')

	#构造附件  
	att = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')  
	att["Content-Type"] = 'application/octet-stream'  
	att["Content-Disposition"] = 'attachment; filename=%s' %title.encode('gb2312')

	msgRoot.attach(msg)
	msgRoot.attach(att) 
	  
	smtp = smtplib.SMTP()  
	smtp.connect(smtpserver)  
	smtp.login(username, password)  
	smtp.sendmail(sender, receiver, msgRoot.as_string())
	smtp.quit()


