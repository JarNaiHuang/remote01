from base import logger
from config import BASE_URL
from pages.login_page_ex import LoginPage


class TestLogin:
    """测试登录页面类"""

    def test_01_login_success(self, page):
        # 创建对象 # 测试数据
        lg_page = LoginPage(page)
        try:
            # 调用方法/函数
            lg_page.open_url(BASE_URL + "/Home/user/login.html")
            lg_page.login_ex('13800001001', '123456', '8888')
            # 打印结果:获取文本
            # result = lg_page.success_loc.text_content()
            result = lg_page.get_element_text(lg_page.success_loc)
            logger.info(f"登录结果：{result}")
            # 断言
            # expect(lg_page.success_loc).to_have_text("13800001001")
            lg_page.assert_have_text(lg_page.success_loc, "13800001002")
        except Exception as e:
            logger.error(f"登录异常：{e}")
            raise e
        finally:
            # 无论是否成功都需要截图
            lg_page.get_screen_shot("login_success")

    def test_02_login_fail_username_error(self, page):
        # 创建对象
        lg_page = LoginPage(page)
        try:
            # 调用方法/函数  # 测试数据
            lg_page.open_url(BASE_URL + "/Home/user/login.html")
            lg_page.login_ex('138000010012', '123456', '8888')
            # 打印结果
            result = lg_page.get_element_text(lg_page.fail_loc)
            logger.info(f"登录结果：{result}")
            # 断言
            lg_page.assert_have_text(lg_page.fail_loc, "账号格式不匹配!")
        except Exception as e:
            logger.error(f"登录异常：{e}")
            raise e
        finally:
            # 无论是否成功都需要截图
            lg_page.get_screen_shot("login_fail")
