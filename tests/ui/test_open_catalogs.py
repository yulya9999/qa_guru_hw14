import allure
import pytest
from zoolandia_project_tests.models.pages.base_page import base_page


@allure.feature("Каталоги магазина")
@allure.story("Проверка перехода в каталог")
@pytest.mark.parametrize("url, page_title", [
    ("/sobakam/", "Собакам"),
    ("/koshkam/", "Кошкам"),
    ("/gryzunam/", "Грызунам"),
    ("/ptitsam/", "Птицам"),
    ("/rybkam/", "Рыбкам"),
    ("/reptiliyam/", "Рептилиям"),
    ("/khorkam/", "Хорькам"),
    ("/aptechka/", "Аптечка"),
])
def test_open_catalog_success(url, page_title):
    base_page.open_catalog(url)
    base_page.validate_url(url)
    base_page.check_title(page_title)
