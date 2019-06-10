# -*- encoding:utf-8 -*-

from selenium.webdriver.common.by import By


class WorkElement:

	FRAME_ID = 'iframe-box'  # frame id
	CREATE_ORDER_BTN = (By.XPATH, "//li[@class='common_btn']/span")  # 新建按钮
	# 获取新建预约iframe id
	FIND_FRAME_JS = "id = document.getElementsByTagName('iframe')[1].id; return id"
	SELECT_USER_BTN = (By.XPATH, '//span/a')  # 选择用户按钮
	USER = (By.XPATH, "//dd/span/input")  # 用户输入框
	USER_SERVICE = (By.NAME, 'bmsetmealId')  # 用户服务
	SELECT_USER = (By.NAME, 'userID')  # select 用户列表
	START_DAY_INPUT = (By.XPATH, "//*[@id='myDay']")  # 服务开始日期
	START_TIME_INPUT = (By.XPATH, "//*[@id='myStartTime']")  # 服务开始时间
	END_TIME_INPUT = (By.XPATH, "//*[@id='endTime']")  # 服务结束时间
	SELECT_STAFF = (By.NAME, 'operateID')  # 美容师列表
	SELECT_APPROVE = (By.NAME, 'managerId')  # 预约人列表
	SUBMIT_BTN = (By.XPATH, "//div[2]/div[1]")  # 保存按钮
	WINDOW_TITLE = (By.CLASS_NAME, 'layui-layer-title')  # 预约窗口标题栏
	FRAME_FOOTER = (By.CLASS_NAME, 'layer-footer')  # frame footer
	TEXT = (By.XPATH, '//*[@id="layui-layer2"]/div[2]')
	ALERT_MESSAGE = (By.CLASS_NAME, 'layui-layer-msg')  # 弹窗警告信息
