from Utilities.environmentsetup import EnvironmentSetup
from Page.generalUses import GeneralUses
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import softest
import json
import time
import os


class TestProfileData(EnvironmentSetup, softest.TestCase):
    def test_profile_data(self):
        gu = GeneralUses(self.driver)
        gu.login("test@example.com", "password")

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), ' logged in! ')]")))

        # JS to intercept XHR and Fetch requests
        self.driver.execute_script("""
        window.reportsResponse = null;
        (function(open) {
            XMLHttpRequest.prototype.open = function(method, url, async, user, pass) {
                this._url = url;
                this.addEventListener("load", function() {
                    if (!window.reportsResponse && this._url.includes("profile")) {
                        try {
                            window.reportsResponse = this.responseText;
                        } catch (e) {
                            console.error("XHR error:", e);
                        }
                    }
                });
                open.apply(this, arguments);
            };
        })(XMLHttpRequest.prototype.open);

        (function(fetch) {
            window.fetch = function() {
                return fetch.apply(this, arguments).then(response => {
                    if (!window.reportsResponse && response.url.includes("profile")) {
                        response.clone().text().then(text => {
                            try {
                                window.reportsResponse = text;
                            } catch (e) {
                                console.error("Fetch error:", e);
                            }
                        });
                    }
                    return response;
                });
            };
        })(window.fetch);
        """)

        gu.navigate_to_profile()
        time.sleep(2)
        js_response = self.driver.execute_script("return window.reportsResponse")
        self.assertIsNotNone(js_response, "No se capturó ninguna respuesta de perfil.")

        json_data = json.loads(js_response)

        # Saved response to a json file
        output_path = "evidence/profile_response.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)
        print(f"JSON exportado a: {output_path}")

        username = json_data["props"]["auth"]["user"]["name"]
        email = json_data["props"]["auth"]["user"]["email"]
        user_id = json_data["props"]["auth"]["user"]["id"]

        print(f"Nombre de usuario: {username}")
        print(f"Email: {email}")
        print(f"User ID: {user_id}")

        self.soft_assert(self.assertEqual, username, "Test")
        self.soft_assert(self.assertEqual, email, "test@example.com")
        self.soft_assert(self.assertEqual, user_id, 2)
        self.assert_all()
