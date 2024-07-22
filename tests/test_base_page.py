from pages.base_page import base_page
from pages.cart_page import cart_page


def test_lazzaro():
    base_page.open_browser()
    base_page.search_line("LAZZARO")
    base_page.add_item_cart(
        '.product-item-button-container [id="bx_113636234_267537_34fe06408355c83ff49cf42c9875666b_buy_link"]')
    base_page.close_window('[class*="popup-window-close-icon popup-window-titlebar-close-icon"]')
    cart_page.open_cart()
    cart_page.check_item_cart("LAZZARO Игрушка д/кошек шар с перьями")
    cart_page.clean_cart()



