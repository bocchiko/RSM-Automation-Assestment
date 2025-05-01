from Utilities.environmentsetup import EnvironmentSetup
from Page.generalUses import GeneralUses
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import softest
import random
import string


class TestUpdateProfile(EnvironmentSetup, softest.TestCase):
    def test_update_profile(self):
        gu = GeneralUses(self.driver)
        gu.login("luis@example.com", "Luis2001")
        gu.navigate_to_profile()

        wait = WebDriverWait(self.driver, 15)

        # Random values for name and phone number
        random_name = ''.join(random.choices(string.ascii_letters, k=5))
        random_phone = ''.join(random.choices(string.digits, k=10))

        name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_input.clear()
        name_input.send_keys(random_name)

        phone_input = wait.until(EC.presence_of_element_located((By.ID, "phone_number")))
        phone_input.clear()
        phone_input.send_keys(random_phone)

        upload_img_input = wait.until(EC.presence_of_element_located((By.ID, "user_profile_image")))
        upload_img_input.send_keys(os.path.abspath("evidence/logged.png"))
        time.sleep(2)

        self.driver.save_screenshot("evidence/update_profile.png")

        save_btn = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='flex items-center gap-4']//button")))
        save_btn[0].click()

        # Verify the success message
        success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='flex items-center gap-4']//p")))
        self.soft_assert(self.assertIn, "saved", success_msg.text.lower())
        print(f"Guardado exitosamente: {success_msg.text}")
        self.assert_all()
