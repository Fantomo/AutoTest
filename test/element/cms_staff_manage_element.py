# -*- encoding:utf-8 -*-

from selenium.webdriver.common.by import By


class StaffManageElement:

	STAFF_MANAGE_BTN = (By.LINK_TEXT, '员工管理')  # 员工管理按钮
	FRAME_ID = 'iframe-box'  # iframe_id
	CREATE_STAFF_BTN = (By.CSS_SELECTOR, 'li.common_btn>span')  # 新建员工按钮
	CANCEL_CREATE_BTN = (By.CSS_SELECTOR, 'div#cancelEditBtn')  # 取消新建按钮
	GET_FRAME_ID = "return document.getElementsByTagName('iframe')[1].id;"
	STAFF_NAME = (By.CSS_SELECTOR, 'input#staff_name')  # 员工姓名
	STAFF_NICKNAME = (By.CSS_SELECTOR, 'input#nickname')  # 员工昵称
	STAFF_MOBILE = (By.CSS_SELECTOR, 'input#staff_mobile')  # 员工手机号
	STAFF_EMAIL = (By.CSS_SELECTOR, 'input#staff_email')  # 员工email
	SELECT_STAFF_POSITION = (By.ID, 'staff_position')  # 员工职务
	STAFF_ID_CARD = (By.CSS_SELECTOR, 'input#id_card')  # 员工身份证
	STAFF_HIREDATE = (By.CSS_SELECTOR, 'input#inner_date')  # 员工入职日期
	SAVE_BTN = (By.CSS_SELECTOR, 'div#saveCreateBtn')  # 保存员工
	TIPS = (By.CSS_SELECTOR, 'span.form_tips.err_tips')  # 提示信息
	WINDOW_TIPS = (By.CSS_SELECTOR, 'div#layui-layer2 > div.layui-layer-content')  # 弹窗提示信息
	WINDOW_TIPS_BTN = (By.CSS_SELECTOR, 'a.layui-layer-btn0')  # 弹窗提示"确定"按钮
	TOAST_TIPS = (By.XPATH, 'id("layui-layer2")/div[@class="layui-layer-content layui-layer-padding"]')  # toast 消息
	EDIT_STAFF = (By.XPATH, '/html/body/table/tbody/tr[1]/td[8]/i[1]')  # 编辑员工
	SEARCH_STAFF = (By.CSS_SELECTOR, 'input#searchInput')  # 查找员工
	SEARCH_BTN = (By.CSS_SELECTOR, 'a.search-btn')  # 查找按钮
	STAFFS_NAME = (By.CSS_SELECTOR, 'tr.hover-style > :nth-child(2)')  # 员工姓名
	FIND_STAFF_NAME = "SELECT a.name FROM staff as a WHERE a.store_id = %s and a.`status` = 1"
