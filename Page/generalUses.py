from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

import softest

class GeneralUses(softest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def login(self, username, password):
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)

        username_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        username_input.clear()
        username_input.send_keys(username)

        pswd_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        pswd_input.clear()
        pswd_input.send_keys(password)

        login_btn = "//div[@class='flex items-center justify-end mt-4 space-x-3']//button"
        wait.until(EC.element_to_be_clickable((By.XPATH, login_btn)))
        wait.until(EC.element_to_be_clickable((By.XPATH, login_btn))).click()

        success_msg = "//div[contains(text(), ' logged in! ')]"
        wait.until(EC.presence_of_element_located((By.XPATH, success_msg)))
        self.driver.save_screenshot("evidence/logged.png")