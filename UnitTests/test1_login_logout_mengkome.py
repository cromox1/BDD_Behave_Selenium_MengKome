__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest

class TestMengkome1(unittest.TestCase):

    def setUp(self):
        self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        self.chrome_options = Options()
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--allow-running-insecure-content")
        self.chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        self.chrome_options.add_argument("--disable-cookie-encryption")
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument("--test-type")
        ## webdriver section
        self.driver = webdriver.Chrome(self.chromedriverpath, options=self.chrome_options)
        self.driver.implicitly_wait(10)
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.verificationErrors = []

    def test_one_login(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        driver = self.driver
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        try:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['version']) # Python 3.7 and below
        except:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion']) # Python 3.8 & above
        print()

        user1 = 'bacaone'
        pswd1 = 'qawsed123456'
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('username').click()
        driver.find_element_by_name('username').send_keys(user1 + Keys.ENTER)
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys(pswd1 + Keys.ENTER)
        print('CURRENT URL = ' + driver.current_url)
        userpage1 = driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
        print('Name of the user = ' + userpage1)
        driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
        print('CHECK USER1 = ' + str(user1))
        ## logout
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
        if driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
            print('User ' + user1 + ' successfully LOGGED OUT')
        else:
            print('User ' + user1 + ' IS NOT LOGGED OUT YET')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()