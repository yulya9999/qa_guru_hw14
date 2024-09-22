from selene import browser, have
import allure


@allure.epic("Тестирование аутентификации пользователя'")
class AuthPage:

    @allure.feature("Аутентификация пользователя")
    def user_auth(self, login, password):
        with allure.step('Ввод логина и пароля на странице "Авторизация"'):
            browser.open("/auth/")
            browser.element('.bx-system-auth-form [name="USER_LOGIN"]').type(login)
            browser.element('.bx-system-auth-form [name="USER_PASSWORD"]').type(password)
        with allure.step('Нажатие на кнопку "Войти"'):
            browser.element('.bx-system-auth-form [name="Login"]').click()
        return self

    @allure.feature("Проверка успешной аутентификации")
    def check_successful_auth(self, name):
        with allure.step('Проверка отображения имени пользователя в шапке сайта'):
            browser.element('.bx_login_top_uname_link').should(have.text(name))
        return self


auth_page = AuthPage()
