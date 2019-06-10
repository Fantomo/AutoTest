# -*- encoding:utf-8 -*-

import os
import time

from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH

CHROMEDRIVER_PATH = os.path.join(DRIVER_PATH, 'chromedriver.exe')
FIREFOXDRIVER_PATH = os.path.join(DRIVER_PATH, 'geckodriver.exe')
IEDRIVER_PATH = os.path.join(DRIVER_PATH, 'IEDriverServer.exe')
EDGEDRIVER_PATH = os.path.join(DRIVER_PATH, 'MicrosoftWebDriver.exe')
OPERADIRVER_PATH = os.path.join(DRIVER_PATH, 'operadriver.exe')
PHONTOMJS_PATH = os.path.join(DRIVER_PATH, 'phantomjs.exe')

TYPES = {
	'chrome': webdriver.Chrome, 'firefox': webdriver.Firefox,
	'ie': webdriver.Ie, 'edge': webdriver.Edge,
	'opera': webdriver.Opera, 'phantomjs': webdriver.PhantomJS
}

EXECUTABLE_PATH = {
	'chrome': CHROMEDRIVER_PATH, 'firefox': FIREFOXDRIVER_PATH,
	'ie': IEDRIVER_PATH, 'edge': EDGEDRIVER_PATH,
	'opera': OPERADIRVER_PATH, 'phantomjs': PHONTOMJS_PATH
}


class Browser(object):

	def __init__(self, browser_type='chrome'):
		self._type = browser_type.lower()
		if self._type in TYPES:
			self.browser = TYPES[self._type]
		else:
			raise UnSupportBrowserTypeError("浏览器仅支持: %s!" % ', '.join(TYPES.keys()))
		self.driver = None

	def get(self, url, maximize_windows=True, implicitly_wait=30):
		self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
		self.driver.get(url)
		if maximize_windows:
			self.driver.maximize_window()
		self.driver.implicitly_wait(implicitly_wait)
		return self

	""" 截图 """
	def save_screen_shot(self, name='screen_shot'):
		day = time.strftime('%Y%m%d', time.localtime(time.time()))
		screenshot_path = os.path.join(REPORT_PATH, name + '_%s' % day)
		if not os.path.exists(screenshot_path):
			os.makedirs(screenshot_path)

		date = time.strftime('%H%M%S', time.localtime(time.time()))
		screenshot = self.driver.save_screenshot(os.path.join(screenshot_path, '%s_%s.png' % (day, date)))
		return screenshot

	def close(self):
		self.driver.close()
	
	def quit(self):
		self.driver.quit()


class UnSupportBrowserTypeError(Exception):
	pass


if __name__ == "__main__":
	browser = Browser('firefox').get()
	browser.save_screen_shot()
	time.sleep(2)
	browser.close()
