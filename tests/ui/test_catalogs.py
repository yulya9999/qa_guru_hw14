import allure
import pytest

from zoolandia_project_tests.models.pages.base_page import base_page


@allure.feature("Тестирование каталогов")
class TestCatalog:
    @allure.story("Проверка перехода в каталог")
    @pytest.mark.parametrize("url, page_title", [
        ("/catalog/sobakam/", "Собакам"),
        ("/catalog/koshkam/", "Кошкам"),
        ("/catalog/gryzunam/", "Грызунам"),
        ("/catalog/ptitsam/", "Птицам"),
        ("/catalog/rybkam/", "Рыбкам"),
        ("/catalog/reptiliyam/", "Рептилиям"),
        ("/catalog/khorkam/", "Хорькам"),
        ("/catalog/aptechka/", "Аптечка"),
    ])
    def test_open_catalog_success(url, page_title):
        base_page.open_browser(url)
        base_page.validate_url(url)
        base_page.check_title(page_title)
