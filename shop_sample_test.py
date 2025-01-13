import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ShopSampleTests(unittest.TestCase):

    def setUp(self):
        print('setup')

        service = Service(r"libs/chromedriver")
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.base_url = "https://autodemo.testoneo.com/en/"

    def tearDown(self):
        print('tearDown')
        self.driver.quit()

    def test_main_page_title(self):
        self.driver.get(self.base_url)
        expected_title = 'Lost Hat'
        actual_title = self.driver.title
        self.assertEqual(expected_title,actual_title)
