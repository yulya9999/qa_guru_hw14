import allure
from selene import browser, have


@allure.epic("Тестирование корзины")
class CartPage:
    @allure.feature("Открытие корзины")
    def open_cart(self, info_item):
        with allure.step("Переход в корзину"):
            browser.element('.bx-basket-block [href="/personal/cart/"]').click()
        with allure.step(f'Проверка наличия товара "{info_item}" в корзине'):
            browser.element('.basket-item-info-name').should(have.text(info_item))
        return self

    @allure.feature("Очистка корзины")
    def clean_cart(self):
        with allure.step("Очистка корзины"):
            browser.element('[class="basket-item-actions-remove visible-xs"]').click()
            browser.element('.basket-coupon-block-total-price-current').should(have.text("0 руб."))
        return self

    @allure.feature("Восстановление удаленного товара из корзины")
    def recovery_item(self, price):
        with allure.step("Восстановление удаленного товара"):
            browser.element('.basket-items-list-item-removed-block [data-entity="basket-item-restore-button"]').click()
            browser.element('.basket-coupon-block-total-price-current').should(have.text(price))

        return self


cart_page = CartPage()
