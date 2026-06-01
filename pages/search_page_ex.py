from base.base_page import BasePage


class SearchPage(BasePage):
    """搜索页面"""

    def __init__(self, page):
        """实例属性：页面元素定位"""
        super().__init__(page)
        # 搜索框
        self.search_loc = page.locator('#q')
        # 搜索按钮
        self.search_button_loc = page.get_by_text("搜索")
        # 搜索结果
        self.result_loc = page.locator('div.shop_name2').nth(0)

    def search(self, text):
        """业务方法：搜索操作"""
        self.input_text(self.search_loc, text)
        self.click_element(self.search_button_loc)
