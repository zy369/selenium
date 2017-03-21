import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class VerifyRemote(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platform'] = 'LINUX'
        desired_caps['browserName'] = 'firefox'
        # desired_caps['browserName'] = 'chrome'

        self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_one(self):
        search_box = self.driver.find_element_by_id('kw')
        search_box.send_keys('selenium', Keys.RETURN)

    def test_close(self):
        search_box = self.driver.find_element_by_id('kw')
        search_box.send_keys('selenium---------------', Keys.RETURN)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
