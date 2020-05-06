import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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
    def test_attr(self):
        element  = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        search_element = (element.is_enabled())#判断 搜索框是否可用
        print(element.text)#获取 name属性
        print(element.location)#获取 坐标
        print(element.size)#获取宽和高
        if  search_element  == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴 ")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            search_result = alibaba_element.get_attribute("displayed")#判断是否可见
            if search_result ==  'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_toucahaction(self):
        action = TouchAction(self.driver)
        window_rect  = self.driver.get_window_rect()#获取屏幕的 大小
        width =  window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start  =  int(height * 4/5)
        y_end =  int(height  * 1/5)
        action.press(x=x1,y=y_start).wait(500).move_to(x=x1,y=y_end).release().perform()#滑动操作


    def test_getcurrent_prices(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴 ")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_prices  = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert float(current_prices) > 200

    def test_myinfo(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tar_name").text("我的")')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票 "))')

    def test_scrool_finde_element(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new  UiSelector().text("查找文本").instance(0));')
        #滚动查找
if __name__ == '__main__':
    pytest.main()