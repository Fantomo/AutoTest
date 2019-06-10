# -*- encoding:utf-8 -*-

import random

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from test.common.event import Event
from test.element.cms_beautysalon_manage_element import BSManageElement as bse


class BeautySalonManage(Event):
	""" 系统设置 """

	def sys_set(self):
		self.find_element(*bse.SYS_SETTING_BTN).click()

	""" 新建店群按钮 """

	def create_stores_btn(self):
		self.find_element(*bse.BSM_BTN).click()
		# 美容院管理 --> 门店 按钮
		self.find_element(*bse.STORES_BTN).click()
		self.switch_to_frame(bse.FRAME_ID)
		# 新建店群 按钮
		self.find_element(*bse.CREATE_BTN).click()

	""" 输入店名 """

	def input_stores_name(self, stores_name):
		WebDriverWait(self, 10).until(lambda x: x.find_element(*bse.STORES_NAME))
		self.find_element(*bse.STORES_NAME).send_keys(stores_name)

	""" 店群老板姓名 """

	def input_stores_admin(self, stores_amdin):
		self.find_element(*bse.STORES_ADMIN).send_keys(stores_amdin)

	""" 店群老板手机号 """

	def input_admin_mobile(self, mobile):
		self.find_element(*bse.STORES_ADMIN_MOBILE).send_keys(mobile)

	def input_stores_principal(self, name):
		if name:
			self.find_element(*bse.SELECT_PROVINCE).send_keys(name)

	""" 店群客服电话 """

	def input_serv_tel(self, serv_tel):
		if serv_tel:
			self.find_element(*bse.SERV_TEL).send_keys_keys(serv_tel)
			self.find_element(*bse.ADD_SERV_TEL_BTN).click()

	""" 获取id方法 """

	def get_id(self, element):

		list = []
		eles = Select(self.find_element(*element)).options
		for ele in eles:
			id = ele.get_attribute('value')
			if id != '-1':
				list.append(id)
		return list

	""" 选择省份 """

	def opt_province(self, prov_id):

		Select(self.find_element(*bse.SELECT_PROVINCE)).select_by_value(prov_id)

	""" 选择城市 """

	def opt_city(self, city_id):

		Select(self.find_element(*bse.SELECT_CITY)).select_by_value(city_id)

	""" 选择地区 """

	def opt_area(self, area_id):

		Select(self.find_element(*bse.SELECT_AREA)).select_by_value(area_id)

	""" 随机选择省份城市地区 """

	def input_addr(self, addr=None):
		self.opt_province(random.choice(self.get_id(bse.SELECT_PROVINCE)))
		self.opt_city(random.choice(self.get_id(bse.SELECT_CITY)))
		self.opt_area(random.choice(self.get_id(bse.SELECT_AREA)))
		if addr:
			self.find_element(*bse.INPUT_addr).send_keys(addr)

	""" 保存店群 """

	def save_stores(self):
		self.find_element(*bse.SAVE_BTN).click()
		self.switch_to_default()

	""" 新建门店按钮 """

	def create_store_btn(self):
		self.find_element(*bse.STORE_BTN).click()
		self.wait()
		self.switch_to_frame(bse.FRAME_ID)
		self.find_element(*bse.CREATE_BTN).click()

	def input_store_name(self, store_name):
		self.find_element(*bse.STORE_NAME).send_keys(store_name)

	""" 选择店群 """

	def opt_stores(self, stores_name):
		stores = self.find_element(*bse.OPT_SOTRES)
		stores.clear()
		stores.send_keys(stores_name)
		self.key_down(bse.OPT_SOTRES)
		self.key_enter(bse.OPT_SOTRES)

	""" 选择门店类型 """

	def opt_store_type(self):
		Select(self.find_element(*bse.STORE_TYPE)).select_by_value(random.choice(self.get_id(bse.STORE_TYPE)))

	def input_start_time(self, time):
		self.find_element(*bse.OPEN_TIME).send_keys(time)

	def input_close_time(self, time):

		self.find_element(*bse.CLOSE_TIME).send_keys(time)

	""" 客服电话 """
	def input_tel(self, mobile):

		self.find_element(*bse.TEL).send_keys(mobile)
		self.find_element(*bse.ADD_TEL_BTN).click()

	def save_store(self):
		self.execute(bse.js)
		self.find_element(*bse.SAVE_STORE_BTN).click()
