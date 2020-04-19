import pytest


from appium import webdriver
class TestDW():
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "unicodeKeyBoard" : True,#为了中文输入
            "resetkeyBoard": True,
            "noReset": True  # 不重置
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴 ")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price =  float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price  >  200
if __name__ == '__main__':
    pytest.main()