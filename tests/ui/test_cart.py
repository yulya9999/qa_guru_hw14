import allure
import pytest

from zoolandia_project_tests.models.pages.base_page import base_page
from zoolandia_project_tests.models.pages.cart_page import cart_page


@pytest.fixture()
def lazzaro_feed():
    return {"brand": "LAZZARO", "description": "LAZZARO Adult Dog all breed DEER для собак всех пород с ОЛЕНИНОЙ"}


@pytest.fixture()
def fiory_feed():
    return {"brand": "FIORY", "description": "FIORY Корм для хорьков 650г"}


@allure.story('Проверка добавления товара в корзину')
def test_add_item_to_cart(lazzaro_feed):
    base_page.open_browser()
    base_page.find_item(lazzaro_feed["brand"], lazzaro_feed["description"])
    base_page.add_item_cart()
    cart_page.open_cart(lazzaro_feed["description"])


@allure.story('Проверка очистки корзины')
def test_add_toy_lazzaro(lazzaro_feed):
    base_page.open_browser()
    base_page.find_item(lazzaro_feed["brand"], lazzaro_feed["description"])
    base_page.add_item_cart()
    cart_page.open_cart(lazzaro_feed["description"])
    cart_page.clean_cart()


@allure.story('Проверка восстановления товара в корзине')
def test_restoring_del_product(fiory_feed):
    base_page.open_browser()
    base_page.find_item(fiory_feed["brand"], fiory_feed["description"])
    base_page.add_item_cart()
    cart_page.open_cart(fiory_feed["description"])
    cart_page.clean_cart()
    cart_page.recovery_item("1 167 руб.")
