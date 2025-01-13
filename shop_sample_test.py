import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Import Service

class ShopSampleTests(unittest.TestCase):

    def setUp(self):
        print('Initializing WebDriver')

        options = Options()
        options.add_argument("--headless")  # Ensure Chrome runs in headless mode
        options.add_argument("--no-sandbox")  # Disable sandbox for CI environments
        options.add_argument("--disable-dev-shm-usage")  # Avoid potential issues with shared memory
        options.add_argument("--remote-debugging-port=9222")  # Optional: for debugging

        service = Service(ChromeDriverManager().install())

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
