from selene import browser, have
import allure
from zoolandia_project_tests.models.pages.user_page import test_user


@allure.epic("Тестирование сайта 'зооландия-пенза.рф'")
class AuthPage:

    def user_auth(self):
        with allure.step('Аутентификация пользователя'):
            browser.open("/auth/")
            browser.element('.bx-system-auth-form [name="USER_LOGIN"]').type(test_user.login)
            browser.element('.bx-system-auth-form [name="USER_PASSWORD"]').type(test_user.password)
            browser.element('.bx-system-auth-form [name="Login"]').click()
        return self

    def check_successful_auth(self):
        with allure.step('Проверка успешной аутентификации'):
            browser.element('.bx_login_top_uname_link').should(have.text(test_user.name))
        return self


auth_page = AuthPage()
