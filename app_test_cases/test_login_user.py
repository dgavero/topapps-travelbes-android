import pytest
from app_sections.LoginScreen import LoginScreen
from app_test_cases.BaseTest import BaseTest
from app_utilities import dataProvider


class Test_UserLogin(BaseTest):

    @pytest.mark.parametrize("username,password", dataProvider.get_data("login_credentials"))
    def test_userlogin(self, username, password):
        login = LoginScreen(self.driver)
        login.userLogin(username, password)