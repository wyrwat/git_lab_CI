import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Import Service

class ShopSampleTests(unittest.TestCase):

    def setUp(self):
        print("Setup: Initializing WebDriver")
        # Use Service to specify the chromedriver path
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)  # Use service in Chrome()
        self.base_url = "https://autodemo.testoneo.com/en/"

    def tearDown(self):
        print('tearDown')
        self.driver.quit()

    def test_main_page_title(self):
        self.driver.get(self.base_url)
        expected_title = 'Lost Hat'
        actual_title = self.driver.title
        self.assertEqual(expected_title,actual_title)
