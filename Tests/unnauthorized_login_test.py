# test_unauthorized_login_test.py
import random
import string
from Utilities.environmentsetup import EnvironmentSetup
from Page.generalUses import GeneralUses
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest

class TestAccessControl(EnvironmentSetup, softest.TestCase):
    def test_access_profile_without_login(self):
        gu = GeneralUses(self.driver)
        
        # Llamamos al método de acceso sin estar logueados
        current_url = gu.access_profile_without_login()

        expected_url = "https://ibc-dev-production.up.railway.app/"
        
        # Comprobamos que la URL sea la de login
        self.soft_assert(self.assertEqual, expected_url, current_url)
        print(f"Redirigido correctamente a: {current_url}")

        self.assert_all()  # Asegura que todas las aserciones se ejecuten

