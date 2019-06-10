# -*- encoding:utf-8 -*-

import random, time

from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from test.common.page import Page
from test.element.cms_customer_manage_element import CustomerManageElement as cme


class CustomerManage(Page):
	"""
	用户管理页
	"""

	def customer_manage(self):
		"""
		点击顾客管理
		"""
		self.find_element(*cme.CUSTOMER_MANAGE_BTN).click()
		self.switch_to_frame(cme.FRAME_ID)

	def create_customer(self):
		"""
		点击新建按钮
		"""
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.CREATE_CUSTOMER_BTN))
		self.find_element(*cme.CREATE_CUSTOMER_BTN).click()
		self.switch_to_default()
		frame = self.execute(js=cme.FIND_FRAME_JS)
		self.switch_to_frame(frame)

	def new_customer(self):
		"""
		选择新顾客导入
		"""
		self.create_customer()
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.NEW_CUSTOMER))
		# 选择新顾客导入
		self.find_element(*cme.NEW_CUSTOMER).click()
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.NEXT_BTN)).click()

	def old_customer(self):
		"""
		老顾客导入
		:return:
		"""
		self.create_customer()
		WebDriverWait(self.driver, 3).until(lambda x: x.find_element(*cme.OLD_CUSTOMER))
		self.find_element(*cme.OLD_CUSTOMER).click()
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.NEXT_BTN)).click()

	def input_name(self, name, flag='old'):
		"""
		:param name: input username
		:param flag: old 为老顾客导入, new 为新顾客导入
		"""
		if flag == 'new':
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.NEW_USER_NAME))
			self.find_element(*cme.NEW_USER_NAME).send_keys(name)
		elif flag == 'old':
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.OLD_USER_NAME))
			self.find_element(*cme.OLD_USER_NAME).send_keys(name)

	def input_mobile(self, mobile, flag='old'):
		"""
		:param mobile: input usermobile
		:param flag: old 为老顾客导入, new 为新顾客导入
		"""
		if flag == 'new':
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.NEW_USER_MOBILE))
			self.find_element(*cme.NEW_USER_MOBILE).send_keys(mobile)
		elif flag == 'old':
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.OLD_USER_MOBILE))
			self.find_element(*cme.OLD_USER_MOBILE).send_keys(mobile)
			WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.STEP_ONE)).click()

	def select_service_btn(self):
		"""
		选择服务卡项按钮
		"""
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.ADD_SERVICE_BTN))
		self.find_element(*cme.ADD_SERVICE_BTN).click()

	def save_new(self):
		"""
		保存顾客
		"""
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.SAVE_BTN)).click()

	def save_new_continue(self):
		"""
		保存并继续新建顾客
		"""
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.SAVE_TO_CONTINUE)).click()

	def get_tips(self):
		"""
		获取提示信息
		:return: 返回提示信息文本
		"""
		try:
			WebDriverWait(self.driver, 3).until(lambda x: x.find_element(*cme.TIPS))
			return self.find_element(*cme.TIPS).text
		except TimeoutException:
			try:
				self.switch_to_default()
				WebDriverWait(self.driver, 3).until(lambda x: x.find_element(*cme.WINDOWS_TIPS))
				return self.find_element(*cme.WINDOWS_TIPS).text
			except TimeoutException:
				raise TimeoutError

	def cancel_save(self):
		"""
		顾客转店取消按钮
		"""
		WebDriverWait(self.driver, 3).until(lambda x: x.find_element(*cme.CANCEL_BTN))
		self.find_element(*cme.CANCEL_BTN).click()

	def get_options_value(self, element):
		"""
		获取select中option的value
		:return: value 列表
		"""
		values = []
		elements = Select(self.find_element(*element)).options
		for ele in elements:
			value = ele.get_attribute('value')
			if value != '-1':
				values.append(value)
		return values

	def select_card(self, name):
		"""
		导入会员卡
		:param name:会员卡类型, 1 疗程卡, 2 时限卡, 3, 时次卡
		:return:
		"""
		try:
			if name == '1':
				element = cme.TREATMENT_CARD
			elif name == '2':
				element = cme.TIME_CARD
			elif name == '3':
				element = cme.TIME_COUNT_CARD
			self.select_service_btn()
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*element))
			self.find_element(*element).click()
			Select(self.find_element(*cme.SELECT_CARD)).select_by_value(
				random.choice(self.get_options_value(cme.SELECT_CARD)))
		except NameError:
			raise NameError("检查输入的name值: 1 疗程卡, 2 时限卡, 3 时次卡")

	def select_service(self, flag=True):
		"""
		导入服务
		:param flag 判断是否为回调
		"""
		if flag:
			self.select_service_btn()
			WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.SERVICE)).click()
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.SELECT_SERV)).click()
		# WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.SERV_TYPE_ONE))
		time.sleep(1)
		# 选择一级分类
		Select(self.find_element(*cme.SERV_TYPE_ONE)).select_by_value(
			random.choice(self.get_options_value(cme.SERV_TYPE_ONE)))
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.SERV_TYPE_TWO))
		# 选择二级分类
		Select(self.find_element(*cme.SERV_TYPE_TWO)).select_by_value(
			random.choice(self.get_options_value(cme.SERV_TYPE_TWO)))
		try:
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.SERVICES))
			service_elements = self.find_elements(*cme.SERVICES)
			services = []
			for element in service_elements:
				services.append(element)
			# 随机选择服务
			random.choice(services).click()
			WebDriverWait(self.driver, 5000).until(lambda x: x.find_element(*cme.SERVICE_NUM))
			# 输入服务次数
			self.find_element(*cme.SERVICE_NUM).send_keys('10')

		except (TimeoutException, StaleElementReferenceException, ElementNotVisibleException):
			# 二级目录下没有项目时，callback select_service() 重新选择项目
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.CLOSE_BTN))
			self.find_element(*cme.CLOSE_BTN).click()
			time.sleep(1)
			self.select_service(flag=False)

	def input_account_balance(self, account_balance=None, product_balance=None, old_customer_debt=None):
		"""
		导入账户余额
		:param account_balance: 储值余额
		:param product_balance: 产品余额
		:param old_customer_debt: 欠款金额
		"""
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.STEP_TWO)).click()
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.ACCOUNT_BALANCE))
		self.find_element(*cme.ACCOUNT_BALANCE).send_keys(account_balance)
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.PRODUCT_BALANCE))
		self.find_element(*cme.PRODUCT_BALANCE).send_keys(product_balance)
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.OLD_CUSTOMER_DEBT))
		self.find_element(*cme.OLD_CUSTOMER_DEBT).send_keys(old_customer_debt)

	def select_customer_role(self):
		"""
		选择顾客身份
		:return:
		"""
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.STEP_THREE)).click()
		try:
			WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*cme.SELECT_DUTY_BEAUTICIAN))
			self.find_element(*cme.SELECT_DUTY_BEAUTICIAN).click()
			# 获取责任美容师列表
			staff_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(cme.STAFF_LIST))
			# 随机选择责任美容师
			random.choice(staff_list).click()
		except TimeoutException:
			pass

	def save_old(self):
		"""
		保存老顾客
		"""
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cme.SAVE_OLD_BTN)).click()
