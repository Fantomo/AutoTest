# -*- encoding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from test.common.event import Event
from test.element.cms_work_manage_element import WorkElement as we


class WorkManage(Event):
	""" 切换到新建预约窗口 """

	def create_order_btn(self):

		# 显示等待查找frame
		WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(we.FRAME_ID))
		self.driver.find_element(*we.CREATE_ORDER_BTN).click()

		self.switch_to_default()
		self.frame_id = self.execute(js=we.FIND_FRAME_JS)
		self.switch_to_frame(self.frame_id)

	""" 获取通用id """

	def get_id(self, element):

		list = []
		eles = Select(self.find_element(*element)).options
		for ele in eles:
			id = ele.get_attribute('value')
			if id != '-1':
				list.append(id)
		return list

	""" 获取用户id """

	def get_user_id(self):

		return self.get_id(we.SELECT_USER)

	""" 选择顾客 """

	def opt_user(self, user):

		self.create_order_btn()
		# 输入用户
		self.find_element(*we.USER).send_keys(user)
		self.key_down(we.USER)
		self.key_enter(we.USER)

	""" 获取服务id """

	def get_service_id(self):

		return self.get_id(we.USER_SERVICE)

	# 选择服务
	def opt_service(self, service_id):
		Select(self.find_element(*we.USER_SERVICE)).select_by_value(service_id)

	""" 选择时间 """

	def opt_time(self, start_day, start_time=None, end_time=None):

		start_time_input = self.find_element(*we.START_TIME_INPUT)
		end_time_input = self.find_element(*we.END_TIME_INPUT)
		self.find_element(*we.START_DAY_INPUT).send_keys(start_day)
		if start_time:
			start_time_input.send_keys(Keys.CONTROL, 'a')
			start_time_input.send_keys(start_time)
		else:
			start_time_input.click()

		if end_time:
			end_time_input.send_keys(Keys.CONTROL, 'a')
			end_time_input.clear()
			end_time_input.send_keys(end_time)
			end_time_input.click()
		else:
			end_time_input.click()

	""" 获取美容师 id """

	def get_staff_id(self):

		return self.get_id(we.SELECT_STAFF)

	""" 选择操作美容师 """

	def opt_staff(self, staff_id):
		Select(self.find_element(*we.SELECT_STAFF)).select_by_value(staff_id)

	""" 获取预约申请人id """

	def get_approve_id(self):
		return self.get_id(we.SELECT_APPROVE)

	""" 选择预约申请人 """

	def opt_approve(self, approve_id):
		Select(self.find_element(*we.SELECT_APPROVE)).select_by_value(approve_id)

	def move_to_top(self):
		self.switch_to_default()
		self.move_window(self.find_element(*we.WINDOW_TITLE), 0, -500)
		self.switch_to_frame(self.frame_id)

	""" 保存预约 """
	def submit(self):
		self.move_to_click(self.find_element(*we.SUBMIT_BTN))

	def alert_window(self):
		self.switch_to_default()
		return self.find_element(*we.TEXT).text

	def get_alert_text(self):
		self.wait(1)
		self.switch_to_default()
		return self.find_element(*we.ALERT_MESSAGE).text
