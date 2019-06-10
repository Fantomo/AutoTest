# -*- encoding:utf-8 -*-

from faker import Factory

fake = Factory().create('zh_CN')


def random_phone_number():
	""" 随机手机号 """
	return fake.phone_number()


def random_name():
	""" 随机姓名 """
	return fake.name()


def random_address():
	""" 随机地址 """
	return fake.address()


def random_email():
	""" 随机邮箱 """
	return fake.email()


def random_company_prefix():
	""" 随机公司名(短) """
	return fake.company_prefix()


def random_company():
	""" 随机公司名(长) """
	return fake.company()


if __name__ == "__main__":
	print(random_phone_number())
	print(random_name())
	print(random_address())
	print(random_email())
	print(random_company_prefix())
	print(random_company())
