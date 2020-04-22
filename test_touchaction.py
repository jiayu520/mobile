from appium.webdriver import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def  setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.MainActivity",
            "unicodeKeyBoard": True,  # 为了中文输入
            "resetkeyBoard": True,
            "noReset": True  # 不重置
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardonw(self):
        self.driver.quit()

    def test_toucahaction(self):
        action   =  TouchAction(self.driver)
        action.press(x=243,y=395).move_to(x=721,y=378).move_to(x=1190,y=364).release().perform()#手势密码