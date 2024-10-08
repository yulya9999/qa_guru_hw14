import os

import allure

from zoolandia_project_tests.data.user import User
from zoolandia_project_tests.models.pages.auth_page import auth_page


@allure.feature("Тестирование авторизации")
class TestAuth:
    @allure.story("Авторизация пользователя")
    def test_auth(self):
        test_user = User(login=os.getenv("USER_LOGIN"),
                         password=os.getenv("USER_PASSWORD"),
                         name=os.getenv("USER_NAME"))
        auth_page.user_auth(test_user)
        auth_page.check_successful_auth(test_user)
