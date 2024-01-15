import pytest
from app_sections.LoginScreen import LoginScreen
from app_test_cases.BaseTest import BaseTest
from app_utilities import dataProvider


class Test_Technicianlogin(BaseTest):

    @pytest.mark.parametrize("username,password", dataProvider.get_data("login_credentials"))
    def test_techlogins(self, username, password):
        login = LoginScreen(self.driver)
        login.techLogin(username, password)




