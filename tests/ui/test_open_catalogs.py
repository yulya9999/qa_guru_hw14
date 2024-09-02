import allure
from zoolandia_project_tests.models.pages.base_page import base_page


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story("Проверка перехода в каталог")
def test_open_catalog_success():
    base_page.open_catalog("/sobakam/", "Собакам")
    base_page.open_catalog("/koshkam/", "Кошкам")
    base_page.open_catalog("/gryzunam/", "Грызунам")
    base_page.open_catalog("/ptitsam/", "Птицам")
    base_page.open_catalog("/rybkam/", "Рыбкам")
    base_page.open_catalog("/reptiliyam/", "Рептилиям")
    base_page.open_catalog("/khorkam/", "Хорькам")
    base_page.open_catalog("/aptechka/", "Аптечка")
