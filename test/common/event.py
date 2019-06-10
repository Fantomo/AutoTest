# -*- encoding:utf-8 -*-

from test.common.page import Page

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Event(Page):

	# 移动到指定元素
	def move_to(self, element):
		ActionChains(self.driver).move_to_element(element).perform()

	# 点击指定元素
	def move_to_click(self, element):
		ActionChains(self.driver).click(element).perform()

	# 双击
	def double_click(self, element):
		ActionChains(self.driver).double_click(element).perform()

	def move_window(self, source, xoffset, yoffset):
		ActionChains(self.driver).drag_and_drop_by_offset(source, xoffset, yoffset).perform()

	# 按方向下键
	def key_down(self, element):
		self.find_element(*element).send_keys(Keys.DOWN)

	# 按Enter
	def key_enter(self, element):
		self.find_element(*element).send_keys(Keys.ENTER)
