# -*- encoding:utf-8 -*-

from selenium.webdriver.common.by import By


class LoginElement:

	LOC_USER_INPUT = (By.ID, 'login_username')
	LOC_PASSWORD_INPUT = (By.ID, 'login_password')
	LOC_LOGIN_BTN = (By.ID, 'login-btn')
	LOC_ERR_TIPS = (By.XPATH, '//span')
