import allure
from selene import browser, have

from tests.conftest import BASE_URL
from zoolandia_project_tests.data.feed import Feed


class BasePage:
    def open_browser(self, url=None):
        with allure.step(f"Открыть {BASE_URL}{url}"):
            if url is not None:
                browser.open(BASE_URL + url)
            else:
                browser.open("/")
        return self

    def validate_url(self, url):
        with allure.step(f"Проверка открытой страницы"):
            browser.should(have.url(BASE_URL + url))
        return self

    def click_nav_bar_text(self, url):
        with allure.step(f"Клик по ссылке {url} из навигации"):
            browser.element(f'.head-block-bg [href="{url}"]').click()
        return self

    def check_title(self, content):
        with allure.step("Проверка заголовка страницы"):
            browser.element("#content_body").should(have.text(content))
        return self

    def find_item(self, feed: Feed):
        with allure.step(f'С помощью поисковой строки найти бренд "{feed.brand}"'):
            browser.element('#title-search-input').click().type(feed.brand).press_enter()
        with allure.step(f'Переход на страницу товара "{feed.description}"'):
            browser.element(f'.product-item-title [title="{feed.description}"]').click()
        return self

    def add_item_cart(self):
        with allure.step(f'Добавление товара в корзину'):
            browser.element('[data-entity="main-button-container"]').click()
        with allure.step('Закрытие модального окна после добавления товара в корзину'):
            browser.element('[class*="popup-window-close-icon popup-window-titlebar-close-icon"]').click()
        return self


base_page = BasePage()
