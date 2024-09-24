from selene import browser, have
import allure
from tests.conftest import BASE_URL


@allure.epic("Тестирование главной страницы")
class BasePage:
    @allure.feature("Главная страница")
    def open_browser(self):
        with allure.step(f"Открыть главную страницу"):
            browser.open("/")
        return self

    @allure.feature("Страница каталога")
    def validate_url(self, url):
        with allure.step(f"Проверка открытой страницы"):
            browser.should(have.url(BASE_URL+url))
        return self

    @allure.feature("Страница каталога")
    def open_catalog(self, url):
        with allure.step(f"Открыть каталог {url}"):
            browser.open(f'/catalog{url}')
        return self

    @allure.feature("Информационные страницы")
    def click_nav_bar_text(self, url):
        with allure.step(f"Клик по ссылке {url} из навигации"):
            browser.element(f'.head-block-bg [href="{url}"]').click()
        return self

    @allure.feature("Страница каталога")
    def check_title(self, content):
        with allure.step("Проверка заголовка страницы"):
            browser.element("#content_body").should(have.text(content))
        return self

    @allure.feature("Поисковая строка")
    def find_item(self, name_brand, name_product):
        with allure.step(f'С помощью поисковой строки найти бренд "{name_brand}"'):
            browser.element('#title-search-input').click().type(name_brand).press_enter()
        with allure.step(f'Переход на страницу товара "{name_product}"'):
            browser.element(f'.product-item-title [title="{name_product}"]').click()
        return self

    @allure.feature("Страница товара")
    def add_item_cart(self):
        with allure.step(f'Добавление товара в корзину'):
            browser.element('[data-entity="main-button-container"]').click()
        with allure.step('Закрытие модального окна после добавления товара в корзину'):
            browser.element('[class*="popup-window-close-icon popup-window-titlebar-close-icon"]').click()
        return self


base_page = BasePage()
