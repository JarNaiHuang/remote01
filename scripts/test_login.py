import time

import pytest
from playwright.sync_api import expect

from config import BASE_URL
from pages.login_page import LoginPage
from utils.tools import read_json


class TestLogin:

    arg_names = "phone,password,code,expect_result"

    @pytest.mark.parametrize(arg_names, read_json("login_data.json"))
    def test_00_login(self,page,phone,password,code,expect_result):
            lg_page = LoginPage(page)
            lg_page.open_url(BASE_URL+"/Home/user/login.html")
            lg_page.login(phone, password, code)

            if phone == expect_result:
                result = lg_page.success_loc.text_content()
                print(result)
                expect(lg_page.success_loc).to_have_text(expect_result)
            else:
                result = lg_page.fail_loc.text_content()
                print(result)
                expect(lg_page.fail_loc).to_have_text(expect_result)
            time.sleep(2)
            page.close()