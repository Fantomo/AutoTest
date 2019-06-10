# -*- encoding:utf-8 -*-

from utils.config import Config

from test.element.cms_login_element import LoginElement as le

__DATA = Config().get('data')
URL = __DATA['Online']['URL'] if __DATA['Environmen'] == 'Online' else __DATA['Test']['URL']
__USER = __DATA['Online']['user'] if __DATA['Environmen'] == 'Online' else __DATA['Test']['user']
__PASSWORD = __DATA['Online']['pwd'] if __DATA['Environmen'] == 'Online' else __DATA['Test']['pwd']
__ADMIN_USER = __DATA['Online']['adminUser'] if __DATA['Environmen'] == 'Online' else __DATA['Test']['adminUser']
__ADMIN_PWD = __DATA['Online']['adminPwd'] if __DATA['Environmen'] == 'Online' else __DATA['Test']['adminPwd']


def login(driver, flag=False):
	"""
	:param driver:
	:param flag: 为False 时用店长帐号登录,默认为false; 为True 时用admin帐号登录
	"""
	if flag:
		user = __ADMIN_USER
		password = __ADMIN_PWD
	else:
		user = __USER
		password = __PASSWORD

	driver.find_element(*le.LOC_USER_INPUT).send_keys(user)
	driver.find_element(*le.LOC_PASSWORD_INPUT).send_keys(password)
	driver.find_element(*le.LOC_LOGIN_BTN).click()
	return driver
