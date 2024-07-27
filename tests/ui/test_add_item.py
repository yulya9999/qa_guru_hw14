import allure
from qa_guru_hw14_tests.models.pages.base_page import base_page
from qa_guru_hw14_tests.models.pages.cart_page import cart_page


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story('Товар "LAZZARO Игрушка д/кошек шар с перьями"')
def test_add_toy_lazzaro():
    base_page.open_browser("Команда интернет-магазина «Зооландия» рада приветствовать вас!")
    base_page.search_line("LAZZARO")
    base_page.go_to_product_page("LAZZARO Игрушка д/кошек шар с перьями")
    base_page.add_item_cart()
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("LAZZARO Игрушка д/кошек шар с перьями")
    cart_page.clean_cart()


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story('Товар "BRAVADI FAN для собак всех пород индейка с ячменем (4кг)"')
def test_add_feed_bravadi():
    base_page.open_catalog("/sobakam/", "Собакам")
    base_page.go_to_product_page("BRAVADI FAN для собак всех пород индейка с ячменем")
    base_page.add_item_cart()
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("BRAVADI FAN для собак всех пород индейка с ячменем (4кг)")
    cart_page.clean_cart()


@allure.feature("Тестирование сайта 'зооландия-пенза.рф'")
@allure.story('Товар "Дразнилка-мяч погремушка с перьями"')
def test_restoring_del_product():
    base_page.open_catalog("/koshkam/", "Кошкам")
    base_page.go_to_product_page("Дразнилка-мяч погремушка с перьями")
    base_page.add_item_cart()
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("Дразнилка-мяч погремушка с перьями")
    cart_page.clean_cart()
    cart_page.recovery_item("126 руб.")
