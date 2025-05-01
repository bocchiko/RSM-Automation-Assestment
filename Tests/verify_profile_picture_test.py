from Utilities.environmentsetup import EnvironmentSetup
from Page.generalUses import GeneralUses
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest

class TestVerifyProfilePicture(EnvironmentSetup, softest.TestCase):
    def test_verify_profile_picture(self):
        gu = GeneralUses(self.driver)
        gu.login("test@example.com", "password")
        gu.navigate_to_profile()

        wait = WebDriverWait(self.driver, 15)

        img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "w-10.h-10.rounded-full")))

        img_src = img.get_attribute("src")
        self.assertIsNotNone(img_src, "El atributo src de la imagen está vacío.")
        print(f"Imagen src detectado: {img_src}")

        # Verify if the image has a valid extension
        valid_extensions = (".png", ".jpg", ".jpeg")
        self.soft_assert(self.assertTrue, img_src.lower().endswith(valid_extensions), f"La imagen no es .png ni .jpeg: {img_src}")

        # Verify if the image is loaded correctly
        is_image_loaded = self.driver.execute_script("""
            const img = arguments[0];
            return img.complete && typeof img.naturalWidth != "undefined" && img.naturalWidth > 0;
        """, img)
        self.driver.save_screenshot("evidence/verify_profile_picture.png")

        self.soft_assert(self.assertTrue, is_image_loaded, "La imagen no se visualiza correctamente.")

        self.assert_all()
