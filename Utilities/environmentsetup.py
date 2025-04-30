import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

class EnvironmentSetup(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        service = Service(binary_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://ibc-dev-production.up.railway.app")

    def tearDown(self):
        self.driver.quit()
