import allure

from pages.base_page import base_page, auth_page


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story("Авторизация пользователя")
def test_auth():
    auth_page.user_auth()
