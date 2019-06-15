# -*- encoding: utf-8 -*-
import unittest

from test.page.cms_staff_manage_page import StaffManage
from test.common.login import login, URL
from utils.generator import *


class TestStaffManage(unittest.TestCase):
	STAFF_NAME = None

	# @classmethod
	# def setUpClass(cls):
	# 	__driver = StaffManage().get(URL)
	# 	cls.driver = login(__driver)
	#
	# @classmethod
	# def tearDownClass(cls):
	# 	cls.driver.quit()

	def setUp(self):
		__driver = StaffManage().get(URL)
		self.driver = login(__driver)

	def tearDown(self):
		self.driver.quit()

	def test_create_staff(self):
		self.driver.staff_manage()
		self.driver.create_staff()
		name = random_name()
		self.driver.input_staff_name(name)
		self.driver.input_staff_nickname("Test_" + name)
		self.driver.input_staff_mobile(random_phone_number())
		self.driver.input_staff_email(random_email())
		"""
		select_staff_position(position='职位名') 默认为None, 随机选择职位
		指定position= 值为: '美容师','储备顾问','魅力顾问','店长','美容顾问','养生顾问','美发师'
		"""
		self.driver.select_staff_position()
		self.driver.input_staff_id_card(random_id_card())
		self.driver.input_staff_hiredate('2019/5/1')
		self.driver.save_staff()
		tips, tips_type = self.driver.get_tips()
		tips_list = ['请输入手机号', '请输入姓名', '请填写身份证号码', '请选择入职日期', '手机号格式错误', '身份证号码格式错误', '日期格式错误', '请选择服务项目', '创建成功',
					 '账号在本系统已注册，请修改手机号', '账号在本店内已注册 请修改手机号']
		for t in tips:
			try:
				self.assertIn(t, tips_list)
			except AssertionError:
				self.driver.save_screen_shot()
				raise AssertionError
			finally:
				if tips_type == 'window_tips':
					self.driver.close_window_tips_btn()
				elif tips_type == 'err_tips':
					self.driver.cancel_create_staff()

	# if type(tips) is list:
	# 	for t in tips:
	# 		try:
	# 			self.assertIn(t, tips_list)
	# 		except AssertionError:
	# 			self.driver.save_screen_shot()
	# 			raise AssertionError
	# else:
	# 	try:
	# 		self.assertEqual(tips, '创建成功')
	# 	except AssertionError:
	# 		try:
	# 			self.assertEqual(tips, '账号在本系统已注册，请修改手机号')
	# 		except AssertionError:
	# 			try:
	# 				self.assertEqual(tips, '账号在本店内已注册 请修改手机号')
	# 			except AssertionError:
	# 				self.driver.save_screen_shot()
	# 				raise AssertionError

	# def test_update_staff(self):
	# 	print("update")
	# 	self.driver.staff_manage()
	# 	self.driver.update_staff()
	# 	self.driver.input_staff_hiredate()
	# 	self.driver.save_staff()
	# 	tips = self.driver.get_tips()
	# 	print(tips)

	def test_search_staff(self):
		self.driver.staff_manage()
		self.driver.input_name_or_tel("Test")
		self.driver.search_btn()
		search_names = self.driver.check_search_result()
		staff_names = self.driver.get_staff_name(1)
		if staff_names:
			for name in search_names:
				try:
					self.assertIn(name, staff_names)
				except AssertionError:
					self.driver.save_screen_shot()
					raise AssertionError


if __name__ == '__main__':
	unittest.main(verbosity=2)
