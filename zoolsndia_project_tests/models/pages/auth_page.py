from selene import browser, have
import allure
from dotenv import load_dotenv
import os


load_dotenv()
user_login = os.getenv("USER_LOGIN")
user_pass = os.getenv("USER_PASSWORD")
user_name = os.getenv("USER_NAME")


class AuthPage:

    def user_auth(self):
        with allure.step('Аутентификация пользователя'):
            browser.open("/auth/")
            browser.element('.bx-system-auth-form [name="USER_LOGIN"]').type(user_login)
            browser.element('.bx-system-auth-form [name="USER_PASSWORD"]').type(user_pass)
            browser.element('.bx-system-auth-form [name="Login"]').click()
        return self

    def check_successful_auth(self):
        with allure.step('Проверка успешной аутентификации'):
            browser.element('.bx_login_top_uname_link').should(have.text(user_name))
        return self


auth_page = AuthPage()
