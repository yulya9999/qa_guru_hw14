import allure
from zoolandia_project_tests.models.pages.auth_page import auth_page


@allure.epic("Тестирование сайта 'зооландия-пенза.рф'")
@allure.feature("Главная страница")
@allure.story("Авторизация пользователя")
def test_auth():
    auth_page.user_auth()
    auth_page.check_successful_auth()
