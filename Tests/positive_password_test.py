import sys
import os
import random
import string
from Utilities.environmentsetup import EnvironmentSetup
from Page.generalUses import GeneralUses
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest

class TestRegister(EnvironmentSetup, softest.TestCase):
    def test_register_success_message(self):
        gu = GeneralUses(self.driver)
        
        random_name = ''.join(random.choices(string.ascii_lowercase, k=6))
        random_email = f"{random_name}@example.com"
        
        # Llamar al método de registro
        gu.register(random_name, random_email, "1234567890", "Password123")
        
        wait = WebDriverWait(self.driver, 15)
        wait.until(lambda driver: driver.current_url != "https://ibc-dev-production.up.railway.app/register")

        expected_url = "https://ibc-dev-production.up.railway.app/dashboard"
        current_url = self.driver.current_url

        self.soft_assert(self.assertEqual, expected_url, current_url)
        print(f"Redirigido correctamente a: {current_url}")

        self.assert_all()

