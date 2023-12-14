from app_sections.BasePage import BasePage
import time


class LoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def techLogin(self, username, password):
        self.click("access_location_accept_XPATH")
        self.type("login_usernamefield_ACCESSIBILITYID", username)
        self.type("login_passfield_ACCESSIBILITYID", password)
        self.click("login_loginBTN_XPATH")