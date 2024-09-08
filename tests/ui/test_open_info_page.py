import allure
from zoolandia_project_tests.models.pages.base_page import base_page


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story("Проверка перехода на информационные страницы")
def test_go_to_page_success():
    base_page.go_to_info_page("/discount/", "Скидки")
    base_page.go_to_info_page("/contacts/", "Контакты и телефоны")
    base_page.go_to_info_page("/about/delivery/", "Доставка заказа, способы, сроки и стоимость доставки")
