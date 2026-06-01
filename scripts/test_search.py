from playwright.sync_api import expect
from config import BASE_URL
from pages.login_page import LoginPage
from pages.search_page import SearchPage


class TestSearch:
    """测试搜索页面类"""

    def test_search(self, page):
        """测试搜索功能"""
        # 登录
        lg_page = LoginPage(page)
        # 调用方法/函数
        lg_page.open_url(BASE_URL + "/Home/user/login.html")
        lg_page.login('13800001001', '123456', '8888')

        # 创建对象
        search_page = SearchPage(page)
        # 调用方法
        # search_page.open_url(BASE_URL)  # 已经登录了，不需要打开新的URL
        search_page.search("手机")
        # 打印结果
        result = search_page.result_loc.text_content()
        print(result)
        # 断言
        expect(search_page.result_loc).to_contain_text("vivoX21 6GB+128GB 4G")