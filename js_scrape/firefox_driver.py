import unittest
from selenium import webdriver

class Automation_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()