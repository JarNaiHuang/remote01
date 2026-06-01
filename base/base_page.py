import os
from datetime import datetime
from playwright.sync_api import Page, Locator, expect
from base import logger
from config import PATH


class BasePage:
    """页面基类，封装 Playwright 的公共原子操作"""

    def __init__(self, page: Page, navigation_timeout: int = 30000, action_timeout: int = 15000):
        """
        初始化 BasePage
        :param page: Playwright Page 对象
        :param navigation_timeout: 页面导航（如 goto）的默认超时时间（毫秒），默认30秒
        :param action_timeout: 页面操作（如 click, fill）的默认超时时间（毫秒），默认10秒
        """
        self.page = page
        # 设置默认超时时间
        self.page.set_default_navigation_timeout(navigation_timeout)
        self.page.set_default_timeout(action_timeout)

    # ================= 基础交互操作 =================

    def open_url(self, url: str):
        """打开指定网址"""
        logger.info(f"打开网址: {url}")
        self.page.goto(url)

    def click_element(self, locator: Locator):
        """
        点击元素
        :param locator: 页面元素
        :return: 无
        """
        logger.info("点击元素")
        locator.click()

    def double_click_element(self, locator: Locator):
        """双击元素"""
        logger.info("双击元素")
        locator.dblclick()

    def right_click_element(self, locator: Locator):
        """右键点击元素"""
        logger.info("右键点击元素")
        locator.click(button="right")

    def input_text(self, locator: Locator, text: str):
        """
        输入文本
        :param locator: 页面元素
        :param text: 输入内容
        :return: 无
        """
        logger.info(f"输入文本: {text}")
        locator.fill(text)

    def press_sequentially(self, locator: Locator, text: str):
        """
        逐字输入文本（模拟真人操作）
        :param locator: 页面元素
        :param text: 输入文本
        :return:
        """
        logger.info(f"逐字输入文本: {text}")
        locator.press_sequentially(text)

    def clear_input(self, locator: Locator):
        """单独清空输入框内容"""
        logger.info("清空输入框")
        locator.clear()

    def hover_element(self, locator: Locator):
        """鼠标悬停在元素上"""
        logger.info("鼠标悬停")
        locator.hover()

    def select_option_by_value(self, locator: Locator, value: str):
        """下拉框选择（根据 value）"""
        logger.info(f"下拉框选择 value: {value}")
        locator.select_option(value=value)

    def select_option_by_label(self, locator: Locator, label: str):
        """下拉框选择（根据 label）"""
        logger.info(f"下拉框选择 label: {label}")
        locator.select_option(label=label)

    # ================= 文本获取操作 =================

    def get_element_text(self, locator: Locator) -> str:
        """
        获取元素的可见文本内容
        :param locator: 页面元素
        :return: 元素对应文本内容
        """
        text = locator.inner_text()
        logger.info(f"获取元素文本: {text}")
        return text

    def get_element_attribute(self, locator: Locator, attribute_name: str) -> str:
        """获取元素的指定属性值"""
        value = locator.get_attribute(attribute_name)
        logger.info(f"获取元素属性 {attribute_name}: {value}")
        return value

    # ================= 进阶场景操作 =================

    def get_new_page(self, action_trigger, timeout: int = 10000):
        """处理多窗口/新标签页"""
        logger.info("等待新页面打开")
        with self.page.expect_popup(timeout=timeout) as page_info:
            action_trigger()
        new_page = page_info.value
        logger.info("新页面打开成功")
        return new_page

    def switch_to_frame(self, frame_selector: str):
        """
        切换到指定的 iframe，并返回 FrameLocator 对象
        :param frame_selector: iframe 的定位字符串 (如 "iframe#login-frame")
        :return: FrameLocator 对象
        """
        logger.info(f"准备切换到 iframe: {frame_selector}")
        # 官方推荐：直接通过 page 获取 FrameLocator
        return self.page.frame_locator(frame_selector)

    def get_screen_shot(self, img_name):
        """
        获取页面截图
        :param img_name: 截图名称
        :return: 无
        """
        # 获取当前时间，按照时间格式保存
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        # 截图保存路径
        path = os.path.join(PATH, 'img', f"{img_name}_{now}.png")
        # 截图全屏
        self.page.screenshot(path=path)
        # 记录日志
        logger.info(f"{img_name}图片已保存")

    # ================= 常用断言 =================

    def assert_element_visible(self, locator: Locator):
        """断言元素可见"""
        logger.info("断言元素可见")
        expect(locator).to_be_visible()

    def assert_have_text(self, locator: Locator, expected_text: str):
        """
        断言元素文本是某内容【相等】
        :param locator: 页面元素
        :param expected_text: 预期结果
        :return: 无
        """
        logger.info(f"断言元素文本是: {expected_text}")
        expect(locator).to_have_text(expected_text)

    def assert_contain_text(self, locator: Locator, expected_text: str):
        """
        断言元素包含指定文本【包含】
        :param locator: 页面元素
        :param expected_text: 预期结果
        :return: 无
        """
        logger.info(f"断言元素包含文本: {expected_text}")
        expect(locator).to_contain_text(expected_text)

    def assert_url_contains(self, expected_url_part: str):
        """断言当前 URL 包含指定字符串"""
        logger.info(f"断言 URL 包含: {expected_url_part}")
        expect(self.page).to_have_url(expected_url_part)

    def assert_title(self, expected_title: str):
        """断言页面标题"""
        logger.info(f"断言页面标题: {expected_title}")
        expect(self.page).to_have_title(expected_title)
