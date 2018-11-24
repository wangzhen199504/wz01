

class Base:

    def __init__(self,driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self,loc):
        self.driver.find_element(*loc)

    #点击元素
    def base_click(self,loc):
        ele = self.base_find_element(loc)
        ele.click()

    #输入内容
    def base_input(self,loc,text):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(text)