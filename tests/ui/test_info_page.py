import allure
import pytest

from zoolandia_project_tests.models.pages.base_page import base_page


@allure.feature("Тестирование информационных страниц")
class TestInfoPage:
    @allure.story("Проверка перехода на информационные страницы")
    @pytest.mark.parametrize("url, page_title", [
        ("/discount/", "Скидки"),
        ("/contacts/", "Контакты и телефоны"),
        ("/about/delivery/", "Доставка заказа, способы, сроки и стоимость доставки"),
    ])
    def test_navigation_bar_links(url, page_title):
        base_page.open_browser(url)
        base_page.validate_url(url)
        base_page.click_nav_bar_text(url)
        base_page.check_title(page_title)
