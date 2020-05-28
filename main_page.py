from appium import webdriver

from search_page import SearchPage


class MainPage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['autoGrantPermissions'] = True
        caps['noReset'] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("tv_agree").click()
    def to_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)