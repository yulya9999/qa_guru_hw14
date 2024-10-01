import allure

from zoolandia_project_tests.data.feed import Feed
from zoolandia_project_tests.models.pages.base_page import base_page
from zoolandia_project_tests.models.pages.cart_page import cart_page


@allure.feature("Тестирование корзины")
class TestCart:
    @allure.story('Проверка добавления товара в корзину')
    def test_add_item_to_cart(self):
        lazzaro_feed = Feed(brand="LAZZARO",
                            description="LAZZARO Adult Dog all breed DEER для собак всех пород с ОЛЕНИНОЙ")
        base_page.open_browser()
        base_page.find_item(lazzaro_feed)
        base_page.add_item_cart()
        cart_page.open_cart()
        cart_page.check_item_in_cart(lazzaro_feed.description)

    @allure.story('Проверка очистки корзины')
    def test_add_toy_lazzaro(self):
        lazzaro_feed = Feed(brand="LAZZARO",
                            description="LAZZARO Adult Dog all breed DEER для собак всех пород с ОЛЕНИНОЙ")
        base_page.open_browser()
        base_page.find_item(lazzaro_feed)
        base_page.add_item_cart()
        cart_page.open_cart()
        cart_page.check_item_in_cart(lazzaro_feed.description)
        cart_page.clean_cart()
        cart_page.check_cart_price()

    @allure.story('Проверка восстановления товара в корзине')
    def test_restoring_del_product(self):
        fiory_feed = Feed(brand="FIORY",
                          description="FIORY Корм для хорьков 650г",
                          price="1 167")
        base_page.open_browser()
        base_page.find_item(fiory_feed)
        base_page.add_item_cart()
        cart_page.open_cart()
        cart_page.check_item_in_cart(fiory_feed.description)
        cart_page.clean_cart()
        cart_page.check_cart_price()
        cart_page.recovery_item()
        cart_page.check_cart_price(fiory_feed.price)
