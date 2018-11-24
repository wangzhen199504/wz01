from selenium.webdriver.common.by import By

from Base.base import Base

search_btn = By.ID,"com.android.settings:id/search"
seach_input_value = By.ID,"android:id/search_src_text"
click_btn = By.CLASS_NAME,"android.widget.ImageButton"

class PageSetting(Base):

    #点击搜索按钮
    def page_click_search_btn(self):
        self.base_find_element(search_btn)
    #搜索框输入内容
    def page_search_input_value(self,text):
        self.base_input(seach_input_value,text)
    #点击返回按钮
    def page_click_back(self):
        self.base_click(click_btn)