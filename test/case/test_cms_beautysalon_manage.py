# -*- encoding:utf-8 -*-

import unittest

from test.common.login import *
from test.page.cms_beautysalon_manage_page import BeautySalonManage
from utils.generator import *


class TestBeautySalonManage(unittest.TestCase):

	STORES_NAME = ''

	@classmethod
	def setUpClass(cls):
		driver = BeautySalonManage(browser_type='chrome').get(URL)
		cls.driver = login(driver, flag=True)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_a_create_stores(self):
		self.driver.sys_set()
		self.driver.create_stores_btn()
		global STORES_NAME
		STORES_NAME = random_company_prefix()
		self.driver.input_stores_name(STORES_NAME)
		self.driver.input_stores_admin(random_name())
		self.driver.input_admin_mobile(random_phone_number())
		self.driver.input_addr(random_address())
		self.driver.save_stores()

	def test_b_create_store(self):
		self.driver.wait()
		self.driver.create_store_btn()
		self.driver.input_store_name(random_company_prefix())
		self.driver.opt_stores(STORES_NAME)
		self.driver.opt_store_type()
		self.driver.input_start_time('2019-4-12')
		self.driver.input_close_time('2019-4-12')
		self.driver.input_tel(random_phone_number())
		self.driver.input_addr(random_address())
		self.driver.save_store()


if __name__ == "__main__":
	unittest.main()
