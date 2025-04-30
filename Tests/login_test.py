import sys
import os

# Agregar el directorio raíz al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utilities.environmentsetup import EnvironmentSetup
from Page.generalUses import GeneralUses
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest


class TestLogin(EnvironmentSetup, softest.TestCase):
    def test_login_success_message(self):
        gu = GeneralUses(self.driver)
        gu.login("test@example.com", "password")

        wait = WebDriverWait(self.driver, 15)
        success_xpath = "//div[contains(text(), ' logged in! ')]"

        message_element = wait.until(EC.visibility_of_element_located((By.XPATH, success_xpath)))
        message_text = message_element.text

        self.soft_assert(self.assertIn, "You're logged in!", message_text)
        print(f"Mensaje de login detectado: {message_text}")
        self.assert_all()
