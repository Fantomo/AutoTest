# -*- encoding:utf-8 -*-

import os
import unittest
import random
import time

from test.page.cms_work_manage_page import WorkManage
from test.common.login import login, URL
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.handle_db import HandleDB
from utils.HTMLTestRunner import HTMLTestRunner


class TestWorkManage(unittest.TestCase):
	excel = os.path.join(DATA_PATH, 'orders.xlsx')
	is_read = Config(os.path.join(DATA_PATH, 'is_read.yaml')).get('is_read')

	if is_read:
		@classmethod
		def setUpClass(cls):
			driver = WorkManage(browser_type='chrome').get(URL)
			cls.driver = login(driver)

		@classmethod
		def tearDownClass(cls):
			cls.driver.close()

	def sub_setUp(self):
		driver = WorkManage(browser_type='chrome').get(URL)
		self.driver = login(driver)

	def sub_tearDown(self):
		self.driver.quit()

	@unittest.skipIf(is_read, "使用excel数据")
	def test_random_order(self):
		print("使用excel数据")
		today = time.strftime('%Y-%m-%d', time.localtime())
		now = time.strftime('%H:%M', time.localtime())
		user_list = HandleDB().search_all("SELECT name from db_user_prod.bmuser a where a.status=1 and a.store_id = 4")
		self.driver.opt_user(random.choice(user_list))
		self.driver.wait(1.5)
		user_service_id = self.driver.get_service_id()
		if user_service_id:
			service_id = random.choice(user_service_id)
			self.driver.opt_service(service_id)
		else:
			print("用户无服务...")
			return

		self.driver.opt_time(today, start_time=now)
		self.driver.wait(1.5)
		staffs_id = self.driver.get_staff_id()
		if staffs_id:
			staff_id = random.choice(staffs_id)
			self.driver.opt_staff(staff_id)
		else:
			print("暂无美容师")
			return

		self.driver.opt_approve(random.choice(self.driver.get_approve_id()))

		self.driver.submit()
		self.driver.wait()
		try:
			self.assertEqual(self.driver.alert_window(), '新建成功！')
		except AssertionError:
			self.driver.save_screen_shot()
			raise AssertionError

	@unittest.skipUnless(is_read, '不使用excel数据')
	def test_create_order(self):
		print("不使用excel数据")
		try:
			datas = ExcelReader(self.excel).data
		except Exception:
			# self.create_order()
			raise Exception
		else:
			if datas:
				for data in datas:
					if data['execute'].lower() == 'yes':
						with self.subTest(data=data):
							try:
								self.sub_setUp()
								self.driver.opt_user(data['UserName'])
								self.driver.opt_service(data['ServerId'])
								self.driver.opt_time(data['StartDay'], data['StartTime'], data['EndTime'])
								self.driver.opt_staff(data['StaffId'])
								self.driver.opt_approve(data['ApproveId'])
								self.driver.submit()
								self.assertEqual(self.driver.alert_window(), data['expect'])
							except AssertionError:
								self.driver.save_screen_shot()
								raise AssertionError
							finally:
								self.sub_tearDown()


if __name__ == "__main__":
	# report = REPORT_PATH + "\\" + str(time.strftime('%Y%m%d_%H%M%S', time.localtime())) + '.html'
	# with open(report, 'wb') as f:
	# 	runner = HTMLTestRunner(f, verbosity=2, title='新建订单', description='新建工单')
	# 	runner.run(TestWorkManage('test_random_order'))
	unittest.main(verbosity=2)
