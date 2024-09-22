import os
import allure
from zoolandia_project_tests.models.pages.auth_page import auth_page
from zoolandia_project_tests.models.pages.user_page import User


@allure.story("Авторизация пользователя")
def test_auth():
    test_user = User(login=os.getenv("USER_LOGIN"),
                     password=os.getenv("USER_PASSWORD"),
                     name=os.getenv("USER_NAME"))
    auth_page.user_auth(test_user.login, test_user.password)
    auth_page.check_successful_auth(test_user.name)
