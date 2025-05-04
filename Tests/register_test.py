import sys
import os
import time
from selenium.webdriver import ActionChains

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utilities.environmentsetup import EnvironmentSetup
from selenium.webdriver.common.by import By
from Mocks.MockRegister import valid_user, invalid_user_register_case_1, passwords_test_cases
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest

class RegisterTest(EnvironmentSetup, softest.TestCase):
    def test_register_fail(self):
        wait = WebDriverWait(self.driver, 30)
        action = ActionChains(self.driver)

        register_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Register')]")))
        register_link.click()

        case_number = 1  # Initialize case number

        # CASE 1: EMAIL ALREADY TAKEN, PHONE NUMBER INVALID, PASSWORDS NOT MATCHING
        self.fill_fields(invalid_user_register_case_1, wait)
        register_btn_xpath = "//div[@class='mt-4 flex items-center justify-end']//button"
        wait.until(EC.element_to_be_clickable((By.XPATH, register_btn_xpath))).click()

        # screenshot for the first case
        self.driver.save_screenshot(f"evidence/case_register_fail_{case_number}.png")
        case_number += 1

        self.assert_error_message(wait, "email has already been taken")
        self.assert_error_message(wait, "phone number must be 10 digits long")
        self.assert_error_message(wait, "The password field confirmation does not match.")

        # CASE 2+: PASSWORD VALIDATION CASES
        for case in passwords_test_cases:
            self.fill_fields({
                "password": case["password"],
                "password_confirmation": case["password"]
            }, wait)

            wait.until(EC.element_to_be_clickable((By.XPATH, register_btn_xpath))).click()

            # screenshot for the password validation cases
            self.driver.save_screenshot(f"evidence/case_register_fail_password_{case_number}.png")
            case_number += 1

            self.assert_error_message(wait, case["error"])

        self.assert_all()
        print("Test Passed: OK")

    def fill_fields(self, fields: dict, wait: WebDriverWait):
        for field_id, value in fields.items():
            time.sleep(1)
            input_element = wait.until(EC.element_to_be_clickable((By.ID, field_id)))
            input_element.clear()
            input_element.send_keys(value)

    def assert_error_message(self, wait: WebDriverWait, expected_text: str):
        error_element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//p[contains(text(), '{expected_text}')]")))
        self.soft_assert(self.assertIn, expected_text, error_element.text)
