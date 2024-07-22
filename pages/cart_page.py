from selene import browser, have


class CartPage:

    def open_cart(self):
        browser.element('.bx-basket-block [href="/personal/cart/"]').click()
        browser.element('.col-lg-9').should(have.text("Моя корзина"))
        return self

    def check_item_cart(self, info_item):
        browser.element('.basket-item-info-name').should(have.text(info_item))
        return self

    def clean_cart(self):
        browser.element('[class="basket-item-actions-remove visible-xs"]').click()
        browser.element('.basket-coupon-block-total-price-current').should(have.text("0 руб."))
        return self


cart_page = CartPage()
