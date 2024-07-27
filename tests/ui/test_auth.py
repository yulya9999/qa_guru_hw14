import allure
from qa_guru_hw14_tests.pages.auth_page import auth_page


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story("Авторизация пользователя")
def test_auth():
    auth_page.user_auth()
    auth_page.check_successful_auth()
