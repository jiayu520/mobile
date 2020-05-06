import pytest
from appium import webdriver
from hamcrest import  *

class TestDW():
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "unicodeKeyBoard": True,  # 为了中文输入
            "resetkeyBoard": True,
            "noReset": True  # 不重置
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
    @pytest.mark.skip
    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute('resource-id'))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute('clickable'))
        print(search_ele.get_attribute('bounds'))

    def test_hamcrest(self):
        assert_that(10,equal_to(9),'这是一个提示')
        assert_that(13,close_to(10,2))
        assert_that("contains  some string",contains_string("string"))