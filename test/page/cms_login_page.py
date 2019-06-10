# -*- encoding:utf-8 -*-
from test.common.page import Page
from test.element.cms_login_element import LoginElement as le


# 封装cms首页
class CMSMainPage(Page):

	def login(self, user, pwd):
		# 输入用户名
		self.driver.find_element(*le.LOC_USER_INPUT).send_keys(user)
		# 输入密码
		self.driver.find_element(*le.LOC_PASSWORD_INPUT).send_keys(pwd)
		self.driver.find_element(*le.LOC_LOGIN_BTN).click()

	def get_err_tips(self):
		# 获取错误提示
		return self.driver.find_element(*le.LOC_ERR_TIPS).text
