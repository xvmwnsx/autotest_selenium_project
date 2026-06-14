from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage, ProductPageLocators):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button.click()
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Button add to cart is not present"
    def compare_the_price_and_name(self):
        price_cart = self.browser.find_element(*ProductPageLocators.PRICE_CART).text
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        assert price_book == price_cart, "Price is not the same"
        title_cart = self.browser.find_element(*ProductPageLocators.TITLE_CART).text
        title_book = self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text
        assert title_cart == title_book, "Book titles are not the same"
    def get_product_price_and_name(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        self.product_name = self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text

    def compare_cart_and_real(self):
        assert self.product_price == self.browser.find_element(*ProductPageLocators.PRICE_CART).text, "Real price and cart price not equal"
        assert self.product_name == self.browser.find_element(*ProductPageLocators.TITLE_CART).text, "Real name and notification name not equal"
