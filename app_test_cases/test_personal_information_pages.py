import pytest

from app_sections.LoginScreen import LoginScreen
from app_sections.PersonalInformationPage import PersonalInformationPage
from app_test_cases.BaseTest import BaseTest
from app_utilities import dataProvider


class Test_PersonalInformationPages(BaseTest):

    @pytest.mark.parametrize("username,password", dataProvider.get_data("login_credentials"))
    @pytest.mark.parametrize("middlename", dataProvider.get_data("personal_info"))
    def test_updateInfo(self, middlename, username, password):

        login = LoginScreen(self.driver)
        personal_info = PersonalInformationPage(self.driver)

        login.techLogin(username, password)
        personal_info.editMiddleName(middlename)
