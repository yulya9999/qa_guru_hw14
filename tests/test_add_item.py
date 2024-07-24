import allure

from pages.base_page import base_page
from pages.cart_page import cart_page


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story('Товар "LAZZARO Игрушка д/кошек шар с перьями"')
def test_add_toy_lazzaro():
    base_page.open_browser("Команда интернет-магазина «Зооландия» рада приветствовать вас!")
    base_page.search_line("LAZZARO")
    base_page.add_item_cart(
            '.product-item-button-container [id="bx_113636234_267537_34fe06408355c83ff49cf42c9875666b_buy_link"]',
            "LAZZARO Игрушка д/кошек шар с перьями")
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("LAZZARO Игрушка д/кошек шар с перьями")
    cart_page.clean_cart()


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story('Товар "BRAVADI FAN для собак всех пород индейка с ячменем (4кг)"')
def test_add_feed_bravadi():
    base_page.open_catalog("/sobakam/", "Собакам")
    base_page.add_item_cart(
        '.product-item-button-container [id = "bx_113636234_269045_ea59f9c453263b5c3f8fc2bc6f5fda8f_buy_link"]',
        "BRAVADI FAN для собак всех пород индейка с ячменем (4кг)")
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("BRAVADI FAN для собак всех пород индейка с ячменем (4кг)")
    cart_page.clean_cart()


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story('Товар "Дразнилка-мяч погремушка с перьями"')
def test_restoring_del_product():
    base_page.open_catalog("/koshkam/", "Кошкам")
    base_page.add_item_cart(
        '.product-item-button-container [id = "bx_113636234_268299_98b8c7a1a1eff95da05fb09dfc5abcbc_buy_link"]',
        "Дразнилка-мяч погремушка с перьями")
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("Дразнилка-мяч погремушка с перьями")
    cart_page.clean_cart()
    cart_page.recovery_item("126 руб.")
