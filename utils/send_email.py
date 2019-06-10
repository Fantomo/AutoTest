# -*- encoding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText


class SendEmail:

	global SEND_USER
	global EMAIL_HOST
	global PASSWORD

	EMAIL_HOST = "smtp.exmail.qq.com"
	SEND_USER = ''
	PASSWORD = ''

	def send_mail(self, user_list, sub, context):

		user = "Eric"+"<"+SEND_USER+">"
		message = MIMEText(context, _subtype='plain', _charset='utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ";".join(user_list)
		server = smtplib.SMTP()
		server.connect(EMAIL_HOST)
		server.login(SEND_USER, PASSWORD)
		server.sendmail(user, user_list, message.as_string())
		server.close()


if __name__ == '__main__':
	send = SendEmail()
	user_list = ['190938605@qq.com']
	sub = '测试邮件'
	context = "first email"
	send.send_mail(user_list, sub, context)
