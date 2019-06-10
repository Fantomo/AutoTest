# -*- encoding:utf-8 -*-

from selenium.webdriver.common.by import By


class BSManageElement:

	SYS_SETTING_BTN = (By.XPATH, "//*[@class='clearfix']/li[3]")  # 系统设置
	BSM_BTN = (By.LINK_TEXT, '美容院管理')  # 美容院管理按钮
	STORES_BTN = (By.LINK_TEXT, '店群')  # 店群按钮
	FRAME_ID = 'iframe-box'
	CREATE_BTN = (By.CSS_SELECTOR, '.cup span')  # 新建店群按钮
	STORES_NAME = (By.ID, 'storesName')  # 店群名称输入框
	STORES_ADMIN = (By.ID, 'storesAdminName')  # 店群管理员
	STORES_ADMIN_MOBILE = (By.ID, 'storesAdminMobile')  # 店群管理员手机号
	STORES_PRINCIPAL = (By.ID, 'dutyStaff')  # 店群负责人
	SERV_TEL = (By.CSS_SELECTOR, 'input.w280')  # 客服电话
	ADD_SERV_TEL_BTN = (By.XPATH, '//div[5]/div/div')  # 添加客服电话按钮
	SELECT_PROVINCE = (By.ID, 'province_select_item')  # 省城 直辖
	SELECT_CITY = (By.ID, 'city_select_item')  # 城市
	SELECT_AREA = (By.ID, 'count_select_item')  # 地区
	INPUT_addr = (By.ID, 'address')  # 详细地址输入框
	SAVE_BTN = (By.ID, 'createStoresBtn')  # 保存按钮
	SAVE_AND_KEEP_BTN = (By.ID, 'createStoresAndKeepBtn')  # 保存并新建

	STORE_BTN = (By.LINK_TEXT, '门店')  # 门店按钮
	STORE_NAME = (By.ID, 'name')  # 门店名称输入框
	OPT_SOTRES = (By.CSS_SELECTOR, 'span input')  # 选择店群
	STORE_TYPE = (By.ID, 'type')  # 门店类型
	OPEN_TIME = (By.ID, 'openTime')  # 开始使用时间
	CLOSE_TIME = (By.ID, 'closeTime')  # 使用截止日期
	TEL = (By.ID, 'contact')  # 门店客服电话
	ADD_TEL_BTN = (By.XPATH, '//div[1]/div[6]/div/div')  # 添加客服电话按钮
	ADD_IMG = (By.ID, 'fileList')  # 添加图片
	SAVE_STORE_BTN = (By.ID, 'createStoreSaveBtn')  # 保存
	js = 'window.scrollTo(0,500)'  # 向下滚动500px
