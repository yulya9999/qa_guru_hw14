import allure
from selene import browser, have

from zoolandia_project_tests.data.feed import Feed


class CartPage:
    @allure.feature("Открытие корзины")
    def open_cart(self):
        with allure.step("Переход в корзину"):
            browser.element('.bx-basket-block [href="/personal/cart/"]').click()
        return self

    def check_item_in_cart(self, feed: Feed):
        with allure.step(f'Проверка наличия товара "{feed.description}" в корзине'):
            browser.element('.basket-item-info-name').should(have.text(feed.description))
        return self

    def clean_cart(self):
        with allure.step("Очистка корзины"):
            browser.element('[class="basket-item-actions-remove visible-xs"]').click()
        return self

    def check_cart_price(self, feed: Feed, price=None):
        with allure.step("Стоимость корзины"):
            if price is not None:
                browser.element('.basket-coupon-block-total-price-current').should(have.text(f"{feed.price} руб."))
            else:
                browser.element('.basket-coupon-block-total-price-current').should(have.text("0 руб."))
            return self

    def recovery_item(self):
        with allure.step("Восстановление удаленного товара"):
            browser.element('.basket-items-list-item-removed-block [data-entity="basket-item-restore-button"]').click()
        return self


cart_page = CartPage()
