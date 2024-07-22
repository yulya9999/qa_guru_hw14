from selene import browser


class BasePage:

    def open_browser(self):
        browser.open('/')
        return self

    def search_line(self, value):
        browser.element('#title-search-input').click().type(value).press_enter()
        return self

    def add_item_cart(self, element_add_cart):
        browser.element(element_add_cart).click()
        return self

    def close_window(self, element_close):
        browser.element(element_close).click()
        return self


base_page = BasePage()
