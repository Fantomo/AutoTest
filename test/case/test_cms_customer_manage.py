# -*- encoding: utf-8 -*-

import unittest

from test.common.login import login, URL
from test.page.cms_customer_manage_page import CustomerManage
from utils.generator import *


class TestCustomerManage(unittest.TestCase):

	def setUp(self):
		__driver = CustomerManage(browser_type='chrome').get(URL)
		self.driver = login(__driver)

	def tearDown(self):
		self.driver.quit()

	def test_create_new_customer(self):
		self.driver.customer_manage()
		self.driver.new_customer()
		self.driver.input_name(random_name(), flag='new')
		self.driver.input_mobile(random_phone_number(), flag='new')
		self.driver.save_new()
		tips = self.driver.get_tips()
		try:
			self.assertEqual(tips, '该顾客已在本店注册,可以正常登录使用')
		except AssertionError:
			try:
				self.assertEqual(tips, '创建成功')
			except AssertionError:
				try:
					self.assertEqual(tips, '该顾客已在其他门店注册，如果点击“确定”将会冻结该顾客，是否继续操作')
					self.driver.cancel_save()
				except AssertionError:
					self.driver.save_screen_shot()
					raise AssertionError

	def test_create_old_customer(self):

		self.driver.customer_manage()
		self.driver.old_customer()
		self.driver.input_name(random_name(), flag='old')
		self.driver.input_mobile(random_phone_number(), flag='old')
		# select_card(name) name值: 1 疗程卡, 2 时限卡, 3 时次卡
		self.driver.select_card(1)
		self.driver.wait(1)
		self.driver.select_card('2')
		self.driver.wait(1)
		self.driver.select_card('3')
		self.driver.wait(1)
		# select_service(num) num为服务次数,默认为10
		self.driver.select_service(num=15)
		self.driver.wait(1)
		self.driver.input_account_balance(100,'1000', '你好')
		self.driver.select_customer_role()
		self.driver.save_old()
		tips = self.driver.get_tips()
		try:
			self.assertEqual(tips, '该顾客已在本店注册,可以正常登录使用')
		except AssertionError:
			try:
				self.assertEqual(tips, '创建成功')
			except AssertionError:
				try:
					self.assertEqual(tips, '该顾客已在其他门店注册，如果点击“确定”将会冻结该顾客，是否继续操作')
					self.driver.cancel_save()
				except AssertionError:
					self.driver.save_screen_shot()
					raise AssertionError


if __name__ == "__main__":
	unittest.main(verbosity=2)
