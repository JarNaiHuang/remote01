

class SearchPage:
    """搜索页面"""

    def __init__(self, page):
        """实例属性：页面元素定位"""
        # 页面对象属性
        self.page = page
        # 搜索框
        self.search_loc = page.locator('#q')
        # 搜索按钮
        self.search_button_loc = page.get_by_text("搜索")
        # 搜索结果
        # self.result_loc = page.get_by_role('link',name="vivox21....").nth(1)
        self.result_loc = page.locator('div.shop_name2').nth(0)


    def open_url(self, url):
        """打开搜索页面"""
        self.page.goto(url)

    def input_search(self, text):
        """输入搜索内容"""
        self.search_loc.fill(text)

    def click_search(self):
        """点击搜索按钮"""
        self.search_button_loc.click()

    def search(self, text):
        """业务方法：搜索操作"""
        self.input_search(text)
        self.click_search()