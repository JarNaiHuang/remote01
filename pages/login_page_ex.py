from base.base_page import BasePage


class LoginPage(BasePage):
    """登录页面"""

    def __init__(self, page):
        """实例属性：页面元素定位"""
        # 扩展式重新init方法
        super().__init__(page)
        # 账号
        self.username_loc = page.locator('xpath=//*[@id="username"]')
        # 密码
        self.password_loc = page.locator('#password')
        # 验证码
        self.code_loc = page.locator('#verify_code')
        # 登录按钮
        self.login_button_loc = page.locator('.J-login-submit')
        # 断言登录成功的元素定位
        self.success_loc = page.locator('.red.userinfo')
        # 断言登录失败的元素定位
        self.fail_loc = page.locator('.layui-layer-content.layui-layer-padding')

    def login_ex(self, phone, password, code):
        """业务方法：登录操作"""
        self.input_text(self.username_loc, phone)
        self.input_text(self.password_loc, password)
        self.input_text(self.code_loc, code)
        self.click_element(self.login_button_loc)
