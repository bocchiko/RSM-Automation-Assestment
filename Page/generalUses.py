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

    def navigate_to_profile(self):
        wait = WebDriverWait(self.driver, 15)

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), ' logged in! ')]")))

        user_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='inline-flex rounded-md']//button")))
        user_menu.click()

        profile_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://ibc-dev-production.up.railway.app/profile']")))
        profile_btn.click()
    
    def register(self, username, email, phone, password):
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)

        self.driver.get("https://ibc-dev-production.up.railway.app/register")

        name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_input.clear()
        name_input.send_keys(username)

        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_input.clear()
        email_input.send_keys(email)

        phone_input = wait.until(EC.presence_of_element_located((By.ID, "phone_number")))
        phone_input.clear()
        phone_input.send_keys(phone)

        password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_input.clear()
        password_input.send_keys(password)

        confirm_input = wait.until(EC.presence_of_element_located((By.ID, "password_confirmation")))
        confirm_input.clear()
        confirm_input.send_keys(password)

        register_btn = "//button[@class='inline-flex items-center rounded-md border border-transparent bg-gray-800 px-4 py-2 text-xs font-semibold uppercase tracking-widest text-white transition duration-150 ease-in-out hover:bg-gray-700 focus:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 active:bg-gray-900 dark:bg-gray-200 dark:text-gray-800 dark:hover:bg-white dark:focus:bg-white dark:focus:ring-offset-gray-800 dark:active:bg-gray-300 ms-4']"
        wait.until(EC.element_to_be_clickable((By.XPATH, register_btn)))
        wait.until(EC.element_to_be_clickable((By.XPATH, register_btn))).click()
        
        self.driver.save_screenshot("evidence/registered.png")
