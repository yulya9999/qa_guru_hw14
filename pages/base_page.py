from selene import browser, have
import allure


class BasePage:

    def open_browser(self, content):
        with allure.step(f"Открыть главную страницу"):
            browser.open("/")
            browser.element(".col-lg-9").should(have.text(content))
        return self

    def open_catalog(self, url, content):
        with allure.step(f"Открыть каталог {url}"):
            browser.open(f'/catalog{url}')
        browser.element(".col-lg-9").should(have.text(content))
        return self

    def search_line(self, value):
        with allure.step(f'С помощью поисковой строки найти бренд "{value}"'):
            browser.element('#title-search-input').click().type(value).press_enter()
        return self

    def add_item_cart(self, element_add_cart, value):
        with allure.step(f'Добавление товара "{value}" в корзину'):
            browser.element(element_add_cart).click()
        return self

    def close_modal_window_after_add_cart(self):
        with allure.step('Закрытие модального окна после добавления товара в корзину'):
            browser.element('[class*="popup-window-close-icon popup-window-titlebar-close-icon"]').click()
        return self


class AuthPage:

    def user_auth(self):
        with allure.step('Аутентификация пользователя'):
            browser.open("/auth/")
            browser.element('.bx-system-auth-form [name="USER_LOGIN"]').type("Юлия")
            browser.element('.bx-system-auth-form [name="USER_PASSWORD"]').type("P@ssw0rd")
            browser.element('.bx-system-auth-form [name="Login"]').click()
        return self


base_page = BasePage()
auth_page = AuthPage()
