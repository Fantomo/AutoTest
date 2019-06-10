# -*- encoding:utf-8 -*-

import os
import unittest

from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner

from test.page.cms_login_page import CMSMainPage


class TestCMSLogin(unittest.TestCase):
	__DATA = Config().get('data')
	URL = __DATA['Online']['URL'] if __DATA['Environmen'] == 'Online' else __DATA['Test']['URL']

	excel = os.path.join(DATA_PATH, 'login.xlsx')

	def sub_setUp(self):
		self.driver = CMSMainPage(browser_type='chrome').get(self.URL)

	def sub_tearDown(self):
		self.driver.quit()

	def test_login(self):
		datas = ExcelReader(self.excel).data
		for data in datas:
			if data['execute'].lower() == 'yes':
				with self.subTest(data=data):
					self.sub_setUp()
					self.driver.login(data['mobile'], data['password'])
					self.driver.wait()
					current_url = self.driver.current_url()
					try:
						if current_url != self.URL:
							self.assertEqual(current_url, data['expect'])
						else:
							self.assertEqual(self.driver.get_err_tips(), data['expect'])
					except AssertionError:
						self.driver.save_screen_shot()
						raise AssertionError
					finally:
						self.sub_tearDown()


if __name__ == "__main__":
	# unittest.main()
	report = REPORT_PATH + '\\report.html'
	with open(report, 'wb') as f:
		runner = HTMLTestRunner(f, verbosity=2, title='登录测试', description='登录测试')
		runner.run(TestCMSLogin('test_login'))
