import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, close_to


class Testparam():
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
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()#点击搜索的取消按钮

    @pytest.mark.parametrize('searchkey,type,expect_price',[
        ('alibaba','BABA',190),
        ('xiaomi','01810',10)
    ])
    def test_search(self,searchkey,type,expect_price):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        #注意参数type前面写了f,才能读取参数
        current_price = float(current_price.text)
        #expect_price = price
        assert_that(current_price,close_to(expect_price,expect_price*0.1))
