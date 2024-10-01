import allure
from selene import browser, have


class CartPage:
    @allure.feature("Открытие корзины")
    def open_cart(self):
        with allure.step("Переход в корзину"):
            browser.element('.bx-basket-block [href="/personal/cart/"]').click()
        return self

    def check_item_in_cart(self, description):
        with allure.step(f'Проверка наличия товара "{description}" в корзине'):
            browser.element('.basket-item-info-name').should(have.text(description))
        return self

    def clean_cart(self):
        with allure.step("Очистка корзины"):
            browser.element('[class="basket-item-actions-remove visible-xs"]').click()
        return self

    def check_cart_price(self, price=None):
        price = price or 0
        with allure.step("Стоимость корзины"):
            browser.element('.basket-coupon-block-total-price-current').should(have.text(f"{price} руб."))
            return self

    def recovery_item(self):
        with allure.step("Восстановление удаленного товара"):
            browser.element('.basket-items-list-item-removed-block [data-entity="basket-item-restore-button"]').click()
        return self


cart_page = CartPage()
