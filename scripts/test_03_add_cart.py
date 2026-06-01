from base import logger
from pages.add_cart_page import AddCartPage


class TestAddCart:
    """测试添加购物车类"""

    def test_01_add_cart_success(self, search_ok):
        """测试添加购物车成功"""
        # 创建对象
        cart_page = AddCartPage(search_ok)
        try:
            # 前置：登录成功-->搜索成功
            # 调用方法
            cart_page.add_cart()
            # 记录日志:操作结果的文本信息
            result = cart_page.get_element_text(cart_page.success_tip_loc)
            logger.info(f"添加结果是：{result}")
            # 断言
            cart_page.assert_have_text(cart_page.success_tip_loc, "添加成功")
        except Exception as e:
            logger.error(f"添加购物车异常：{e}")
            raise e
        finally:
            # 无论是否成功都需要截图
            cart_page.get_screen_shot("add_cart")
