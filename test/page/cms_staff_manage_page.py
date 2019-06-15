# -*- encoding: utf-8 -*-
import random, time
from enum import Enum, unique

from test.common.page import Page
from test.element.cms_staff_manage_element import StaffManageElement as sme
from utils.handle_db import HandleDB

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class StaffManage(Page):
	"""
	员工管理页
	"""
	NOW = time.strftime('%Y-%m-%d', time.localtime())
	def staff_manage(self):
		"""
		点击员工管理
		"""
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sme.STAFF_MANAGE_BTN)).click()
		WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(sme.FRAME_ID))

	def create_staff(self):
		"""
		点击新建员工按钮
		"""
		WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(sme.CREATE_STAFF_BTN)).click()
		self.switch_to_default()
		WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(self.execute(js=sme.GET_FRAME_ID)))

	def input_staff_name(self, staff_name):
		"""
		:param staff_name:员工姓名
		"""
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.STAFF_NAME)).send_keys(staff_name)

	def input_staff_nickname(self, nickname):
		"""
		:param nickname:员工昵称
		"""
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.STAFF_NICKNAME)).send_keys(nickname)

	def input_staff_mobile(self, mobile):
		"""
		:param mobile: 员工账号
		"""
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.STAFF_MOBILE)).send_keys(mobile)

	def input_staff_email(self, email):
		"""
		:param email: 员工email
		"""
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.STAFF_EMAIL)).send_keys(email)

	def select_staff_position(self, position:str=None):
		"""
		:param position: 员工职位
		"""
		if position:
			if position == '美容师':
				value = '1'
			elif position == '储备顾问':
				value = '2'
			elif position == '魅力顾问':
				value = '3'
			elif position == '店长':
				value = '4'
			elif position == '美容顾问':
				value = '6'
			elif position == '养生顾问':
				value = '7'
			elif position == '美发师':
				value = '9'
			else:
				value = random.choice(self.get_opt_value())
			Select(self.find_element(*sme.SELECT_STAFF_POSITION)).select_by_value(value)
		else:
			Select(self.find_element(*sme.SELECT_STAFF_POSITION)).select_by_value(random.choice(self.get_opt_value()))

	def get_opt_value(self):
		"""
		:return: 职位select 中的 value
		"""
		elements = Select(self.find_element(*sme.SELECT_STAFF_POSITION)).options
		values = []
		for ele in elements:
			values.append(ele.get_attribute('value'))
		return values

	def input_staff_id_card(self, id_card):
		"""
		输入员工身份证号
		:param id_card: 员工身份证号
		"""
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.STAFF_ID_CARD)).send_keys(id_card)

	def input_staff_hiredate(self, hiredate=NOW):
		"""
		输入员工入职时间
		:param hiredate: 员工入职时间
		"""
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.STAFF_HIREDATE)).send_keys(hiredate)

	def save_staff(self):
		"""
		保存 员工信息
		"""
		# self.execute(js='window.scrollTo(0,500)')
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.SAVE_BTN)).click()

	def get_tips(self):
		"""
		:return: 页面提示信息, 提示类型
		"""
		self.switch_to_default()
		# return self.find_element(*sme.TOAST_TIPS).text
		tips = []
		try:
			tips.append(WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.TOAST_TIPS)).text)
			return tips, 'toast_tips'
		except TimeoutException:
			try:
				WebDriverWait(self.driver, 5).until(
					EC.frame_to_be_available_and_switch_to_it(self.execute(js=sme.GET_FRAME_ID)))
				WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(sme.TIPS))
				for ele in self.find_elements(*sme.TIPS):
					tips.append(ele.text)
				return tips, 'err_tips'
			except TimeoutException:
				self.switch_to_default()
				tips.append(WebDriverWait(self.driver, 3).until(lambda x: x.find_element(*sme.WINDOW_TIPS)).text)
				return tips, 'window_tips'

	def close_window_tips_btn(self):
		WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(sme.WINDOW_TIPS_BTN)).click()

	def cancel_create_staff(self):
		WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(sme.CANCEL_CREATE_BTN)).click()

	def update_staff(self):
		"""
		:return:
		"""
		WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(sme.EDIT_STAFF)).click()
		self.switch_to_default()
		WebDriverWait(self.driver, 5).until(
			EC.frame_to_be_available_and_switch_to_it(self.execute(js=sme.GET_FRAME_ID)))

	def input_name_or_tel(self, name_or_tel):
		"""
		在搜索框中输入员工姓名或手机号
		:param name_or_tel: 员工姓名或手机号
		"""
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.SEARCH_STAFF)).send_keys(name_or_tel)

	def search_btn(self):
		WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(sme.SEARCH_BTN)).click()

	def check_search_result(self):
		"""
		:return: 员工姓名
		"""
		staff_name = []
		try:
			elements = WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(sme.STAFFS_NAME))
			for element in elements:
				title = element.get_attribute('title')
				if not title:
					staff_name.append(element.text)
				else:
					staff_name.append(title)
			return staff_name
		except TimeoutException:
			return staff_name

	def get_staff_name(self, store_id):
		names = HandleDB().search_all(sme.FIND_STAFF_NAME, store_id)
		name_list = []
		for name in names:
			name_list.append(name[0])
		return name_list


@unique
class Positions(Enum):
	美容师 	= 1
	储备顾问 = 2
	魅力顾问 = 3
	店长 	= 4
	美容顾问 = 6
	养生顾问 = 7
	美发师 	= 9
