from base import logger
from pages.search_page_ex import SearchPage


class TestSearch:
    """测试搜索页面类"""

    def test_search_success(self, login_ok):
        """测试搜索功能"""
        # 创建对象
        search_page = SearchPage(login_ok)
        try:
            # 调用方法
            search_page.search("华为")
            # 打印结果
            result = search_page.get_element_text(search_page.result_loc)
            logger.info(f"搜索结果：{result}")
            # 断言
            search_page.assert_contain_text(search_page.result_loc, "华为")
        except Exception as e:
            logger.error(f"搜索异常：{e}")
            raise e
        finally:
            # 无论是否成功都需要截图
            search_page.get_screen_shot("search")

