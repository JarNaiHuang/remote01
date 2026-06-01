# 自动化测试一般用于回归测试，页面元素定位相对稳定

# 这个项目的登录页 定位信息不用改 是稳定的
class LoginPage:


    def __init__(self, page):
        self.page = page
        self.username_loc = page.locator('xpath=//*[@id="username"]')
        self.password_loc = page.locator("#password")
        self.code_loc = page.locator("#verify_code")
        self.login_button = page.locator('.J-login-submit')
        # 断言登录成功
        self.success_loc = page.locator('.red.userinfo')
        # 断言用户不存在！/ 密码错误！
        self.fail_loc = page.locator('.layui-layer-content.layui-layer-padding')
    def open_url(self,url):
        self.page.goto(url)
    def input_username(self, phone):
        self.username_loc.fill(phone)

    def input_password(self, password):
        self.password_loc.fill(password)

    def input_code(self, code):
        self.code_loc.fill(code)

    def click_login(self):
        self.login_button.click()

    def login(self, phone, password, code):
        self.input_username(phone)
        self.input_password(password)
        self.input_code(code)
        self.click_login()

# 只要在测试用例文件里调用 login就行了