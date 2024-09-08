import allure
from zoolandia_project_tests.models.pages.base_page import base_page
from zoolandia_project_tests.models.pages.cart_page import cart_page


@allure.epic("Тестирование сайта 'зооландия-пенза.рф'")
@allure.feature("Очищение корзины")
@allure.story('Товар "LAZZARO Adult Dog all breed DEER для собак всех пород с ОЛЕНИНОЙ"')
def test_add_toy_lazzaro():
    base_page.open_browser("Команда интернет-магазина «Зооландия» рада приветствовать вас!")
    base_page.search_line("LAZZARO")
    base_page.go_to_product_page("LAZZARO Adult Dog all breed DEER для собак всех пород с ОЛЕНИНОЙ")
    base_page.add_item_cart()
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("LAZZARO Adult Dog all breed DEER для собак всех пород с ОЛЕНИНОЙ")
    cart_page.clean_cart()


@allure.epic("Тестирование сайта 'зооландия-пенза.рф'")
@allure.feature("Очищение корзины")
@allure.story('Каталог "Собакам". Товар "BRAVADI FAN для собак всех пород индейка с ячменем (4кг)"')
def test_add_feed_bravadi():
    base_page.open_catalog("/sobakam/", "Собакам")
    base_page.go_to_product_page("BRAVADI FAN для собак всех пород индейка с ячменем")
    base_page.add_item_cart()
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("BRAVADI FAN для собак всех пород индейка с ячменем (4кг)")
    cart_page.clean_cart()


@allure.epic("Тестирование сайта 'зооландия-пенза.рф'")
@allure.feature("Восстановление товара в корзине")
@allure.story('Каталог "Кошкам". Товар "Дразнилка-мяч погремушка с перьями"')
def test_restoring_del_product():
    base_page.open_catalog("/koshkam/", "Кошкам")
    base_page.go_to_product_page("Дразнилка-мяч погремушка с перьями")
    base_page.add_item_cart()
    base_page.close_modal_window_after_add_cart()
    cart_page.open_cart()
    cart_page.check_item_cart("Дразнилка-мяч погремушка с перьями")
    cart_page.clean_cart()
    cart_page.recovery_item("126 руб.")


@allure.epic("Тестирование сайта 'зооландия-пенза.рф'")
@allure.feature("Переход в корзину из всплывающего окна")
@allure.story('Товар "FIORY Корм для хорьков 650г"')
def test_open_cart_with_modal_window():
    base_page.open_catalog("/khorkam/", "Хорькам")
    base_page.go_to_product_page("FIORY Корм для хорьков 650г")
    base_page.add_item_cart()
    cart_page.open_cart_with_modal_window()
    cart_page.check_item_cart("FIORY Корм для хорьков 650г")
    cart_page.clean_cart()
