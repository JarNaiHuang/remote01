from base.base_page import BasePage


class AddCartPage(BasePage):
    """添加购物车页面"""

    def __init__(self, page):
        """实例属性：页面元素定位"""
        super().__init__(page)
        # 元素定位器
        # 1.进入商品详情页(默认选择的第一个商品)
        self.enter_goods_detail_loc = page.locator('div.shop_name2').nth(0)
        # 2.添加购物车
        self.add_cart_loc = page.get_by_role("link", name="加入购物车")
        # 切换iframe
        self.iframe_loc = page.frame_locator("#layui-layer-iframe1")
        # 3.获取成功提示
        self.success_tip_loc = self.iframe_loc.locator("#addCartBox > div.colect-top > div > span")

    def add_cart(self):
        """添加购物车"""
        self.click_element(self.enter_goods_detail_loc)
        self.click_element(self.add_cart_loc)
