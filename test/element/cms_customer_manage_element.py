# -*- encoding:utf-8 -*-

from selenium.webdriver.common.by import By


class CustomerManageElement:

	CUSTOMER_MANAGE_BTN = (By.LINK_TEXT, '顾客管理')  # 顾客管理按钮
	FRAME_ID = 'iframe-box'  # frame #id
	CREATE_CUSTOMER_BTN = (By.CSS_SELECTOR, 'li.common_btn')  # 新建顾客按钮
	OLD_CUSTOMER = (By.CSS_SELECTOR, 'div.customer.old')  # 老顾客档案导入
	NEW_CUSTOMER = (By.CSS_SELECTOR, 'div.customer.new')  # 新顾客档案导入
	FIND_FRAME_JS = "id = document.getElementsByTagName('iframe')[1].id; return id"  # 查找页面iframeID
	NEXT_BTN = (By.CSS_SELECTOR, 'div.kind-btn.next')  # 下一步
	NEW_USER_NAME = (By.CSS_SELECTOR, 'div.addStaff input#user_name')  # 新顾客姓名
	NEW_USER_MOBILE = (By.CSS_SELECTOR, 'div.addStaff input#user_mobile') # 新顾客手机
	OLD_USER_NAME = (By.CSS_SELECTOR, "div.steps input#user_name")  # 老顾客姓名
	OLD_USER_MOBILE = (By.CSS_SELECTOR, 'div.steps input#user_mobile') # 老顾客手机
	ADD_SERVICE_BTN = (By.CSS_SELECTOR, 'span.add_service')  # 添加服务按钮
	SAVE_BTN = (By.CSS_SELECTOR, 'div.kind-btn.save_new')  # 保存新顾客按钮
	SAVE_TO_CONTINUE = (By.CSS_SELECTOR, 'div.kind-btn.save_new_continue')  # 保存并继续创建按钮
	TIPS = (By.CLASS_NAME, 'layui-layer-content')  # 提示信息
	# FIND_TIPS_JS = "id = document.querySelector('div.layui-layer.layui-layer-dialog.layer-anim').id;return id;"
	WINDOWS_TIPS = (By.CSS_SELECTOR, "#layui-layer2 > div.layui-layer-content")  # 弹窗提示信息
	CANCEL_BTN = (By.CSS_SELECTOR, 'a.layui-layer-btn1')  # 顾客在其他店注册时取消按钮
	STEP_ONE = (By.CSS_SELECTOR, '.step_one .next')  # 跳转到服务卡项
	STEP_TWO = (By.CSS_SELECTOR, '.step_two .next')  # 跳转到账户余额
	STEP_THREE = (By.CSS_SELECTOR, '.step_three .next')  # 跳转到顾客身份
	TREATMENT_CARD = (By.CSS_SELECTOR, '.layer_select_service>ul>li:nth-child(1)')  # 添加疗程卡按钮
	TIME_CARD = (By.CSS_SELECTOR, '.layer_select_service>ul>li:nth-child(2)')  # 添加时限卡按钮
	TIME_COUNT_CARD= (By.CSS_SELECTOR, '.layer_select_service>ul>li:nth-child(3)')  # 添加时次卡按钮
	SERVICE = (By.CSS_SELECTOR, '.layer_select_service>ul>li:nth-child(4)')  # 添加单独服务按钮
	SELECT_CARD = (By.CLASS_NAME, 'card_sel')  # 会员卡 <select/> className
	SELECT_SERV = (By.CLASS_NAME, 'single_service_sel')  # 选择服务
	SERV_TYPE_ONE = (By.ID, 'sel_type')  # 服务一级分类
	SERV_TYPE_TWO = (By.ID, 'sel_type_two')  # 服务二级分类
	SERVICES = (By.CSS_SELECTOR, 'div.content_add[style="display: block;"] ul.clearfix>li')  # 单独服务
	SERVICE_NUM = (By.CSS_SELECTOR, 'input.residueCount')  # 导入服务次数
	CLOSE_BTN = (By.CSS_SELECTOR, 'div.content_add[style="display: block;"] span.close')  # 选择服务的关闭按钮
	ACCOUNT_BALANCE = (By.ID, 'account_balance')  # 储值余额
	PRODUCT_BALANCE = (By.ID, 'product_balance')  # 产品余额
	OLD_CUSTOMER_DEBT = (By.ID, 'oldCustomerDebt')  # 欠款金额
	SELECT_DUTY_BEAUTICIAN = (By.ID, 'choose-mrs')  # 选择责任美容师按钮
	STAFF_LIST = (By.CSS_SELECTOR, '#all-mrs>li[data-staffid]')  # 责任美容师列表
	SAVE_OLD_BTN = (By.CSS_SELECTOR, '.save_old') # 保存老顾客按钮
