import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class EasySign(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://autofms.devtest.tk/index/login?next=%2F')

    def test_singin(self):
        driver = self.driver
        print(driver.current_url)
        print(driver.title)
        self.assertEqual(driver.title, "登入 | autofms 導覽列", "網站標題不正確")
        time.sleep(1)
        driver.find_element_by_name('account').send_keys('admin')
        driver.find_element_by_name('password').send_keys('111111')
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name('btn-primary').click()
        time.sleep(1)
        Banner = driver.find_element_by_xpath('//*[@id="page-banner"]').text
        print(Banner)
        self.assertEqual(Banner, "autofms Banner", "Banner不正確")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)