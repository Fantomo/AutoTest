# -*- encoding:utf-8 -*-

import time

from test.common.browser import Browser

# from utils.log import logger


# 浏览器页面控制
class Page(Browser):

	def __init__(self, page=None, browser_type='chrome'):
		if page:
			self.driver = page.driver
		else:
			super(Page, self).__init__(browser_type=browser_type)

	# 获取当前窗口句柄
	@property
	def current_window(self):
		return self.driver.current_window_handle

	# 获取标题
	@property
	def title(self):
		return self.driver.title

	# 获取当前网址
	def current_url(self):
		return self.driver.current_url

	# 等待时间
	def wait(self, seconds=3):
		time.sleep(seconds)

	# 执行js脚本
	def execute(self, js, *args):
		return self.driver.execute_script(js, *args)

	# 查找指定元素
	def find_element(self, *args):
		return self.driver.find_element(*args)

	# 查找指定多个元素
	def find_elements(self, *args):
		return self.driver.find_elements(*args)

	# 切换窗口
	def switch_to_window(self, partial_url='', partial_title=''):
		"""
			切换窗口
			窗口数>=3时,需传入参数指定跳转到那个窗口
		"""
		all_windows = self.driver.window_handles
		if len(all_windows) == 1:
			logger.warning('只有一个窗口')
		elif len(all_windows) == 2:
			other_windos = all_windows[1 - all_windows.index(self.current_window)]
			self.driver.switch_to.window(other_windos)
		else:
			for window in all_windows:
				self.driver.switch_to.window(window)
				if partial_url in self.driver.current_url or partial_title in self.driver.title:
					break

		# logger.debug(self.driver.current_url, self.driver.title)

	# 切换frame页面
	def switch_to_frame(self, param):
		self.driver.switch_to.frame(param)

	def switch_to_default(self):
		self.driver.switch_to.default_content()

	# 切换alter
	def switch_to_alert(self):
		return self.driver.switch_to.alert

	# 设置隐式等待
	def implicitly_wait(self, timeout=30):
		return self.driver.implicitly_wait(timeout)
