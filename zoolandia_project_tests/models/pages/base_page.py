from selene import browser, have
import allure


class BasePage:

    def open_browser(self, content):
        with allure.step(f"Открыть главную страницу"):
            browser.open("/")
            browser.element("#content_body").should(have.text(content))
        return self

    def open_catalog(self, catalog, content):
        with allure.step(f"Открыть каталог {catalog}"):
            browser.open(f'/catalog{catalog}')
            browser.element("#content_body").should(have.text(content))
        return self

    def go_to_info_page(self, page, content):
        with allure.step(f"Переход на страницу {page}"):
            browser.open("/")
            browser.all(f'.container [href="{page}"]').second.click()
            browser.element("#content_body").should(have.text(content))
        return self

    def search_line(self, name_brand):
        with allure.step(f'С помощью поисковой строки найти бренд "{name_brand}"'):
            browser.element('#title-search-input').click().type(name_brand).press_enter()
        return self

    def go_to_product_page(self, name_product):
        with allure.step(f'Переход на страницу товара "{name_product}"'):
            browser.element(f'.product-item-title [title="{name_product}"]').click()
            browser.element("#content_body").should(have.text(name_product))
        return self

    def add_item_cart(self):
        with allure.step(f'Добавление товара в корзину'):
            browser.element('[data-entity="main-button-container"]').click()
        return self

    def close_modal_window_after_add_cart(self):
        with allure.step('Закрытие модального окна после добавления товара в корзину'):
            browser.element('[class*="popup-window-close-icon popup-window-titlebar-close-icon"]').click()
        return self


base_page = BasePage()
