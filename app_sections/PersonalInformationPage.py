from app_sections.BasePage import BasePage
from app_utilities.scroll_util import ScrollUtil


class PersonalInformationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def editMiddleName(self, middlename):
        self.click("save_credentials_OKBTN_XPATH")
        self.click("access_device_location_ID")
        self.click("calendar_icon_XPATH")
        self.click("profile_icon_XPATH")
        self.click("personal_informationBTN_XPATH")
        self.type("personal_info_middle_namefield_XPATH", middlename)
        ScrollUtil.scrollToTextByAndroidUIAutomator("SAVE", self.driver)
        self.getText("personal_info_successPOPUP_XPATH")
        success_message = "Personal Information saved successfully"
        actual_message = self.getText("personal_info_successPOPUP_XPATH")

        assert actual_message == success_message, f"Expected '{success_message}' but got '{actual_message}'"
