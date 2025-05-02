import sys
import os
from Utilities.environmentsetup import EnvironmentSetup
from Page.generalUses import GeneralUses
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest

class TestAccessControl(EnvironmentSetup, softest.TestCase):
    def test_unnauthorized_login(self):
        gu = GeneralUses(self.driver)

        # Intentar ir al perfil sin haber iniciado sesión
        profile_url = "https://ibc-dev-production.up.railway.app/profile"
        self.driver.get(profile_url)

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.ID, "email")))  # Espera que cargue el campo de login

        expected_url = "https://ibc-dev-production.up.railway.app/login"
        current_url = self.driver.current_url

        self.soft_assert(self.assertEqual, expected_url, current_url)
        print(f"Acceso no autorizado redirige correctamente a: {current_url}")

        self.assert_all()