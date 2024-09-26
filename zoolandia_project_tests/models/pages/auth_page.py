import allure
from selene import browser, have

from zoolandia_project_tests.data.user import User


class AuthPage:

    def user_auth(self, user: User):
        with allure.step('Ввод логина и пароля'):
            browser.open("/auth/")
            browser.element('.bx-system-auth-form [name="USER_LOGIN"]').type(user.login)
            browser.element('.bx-system-auth-form [name="USER_PASSWORD"]').type(user.password)
        with allure.step('Нажатие на кнопку "Войти"'):
            browser.element('.bx-system-auth-form [name="Login"]').click()
        return self

    def check_successful_auth(self, user: User):
        with allure.step('Проверка отображения имени пользователя в шапке сайта'):
            browser.element('.bx_login_top_uname_link').should(have.text(user.name))
        return self


auth_page = AuthPage()
