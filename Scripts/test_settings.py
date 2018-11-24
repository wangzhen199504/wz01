import sys,os

import pytest

sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.page_settings import PageSetting


class TestSetting():
    def setup_class(self):
        self.driver = get_driver
        self.setting = PageSetting(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.paramarizr("","")

    def test_setting(self,value):

        #点击搜索按钮
        self.setting.page_click_search_btn()
        #点击输入按钮
        self.setting.page_search_input_value(value)

        #断言
        try:


        except:
            print("断言失败，数据有误")

        #点击返回按钮
        self.setting.page_click_back()