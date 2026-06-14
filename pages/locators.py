from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    REG_EMAIL = (By.CSS_SELECTOR, "[name = 'registration-email']")
    REG_PASSWORD = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    REG_CHECK_PASSWORD = (By.CSS_SELECTOR, "[name = 'registration-password2']")
    REG_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration-submit']")
    LOG_EMAIL = (By.CSS_SELECTOR, "[name = 'login-username']")
    LOG_PASSWORD = (By.CSS_SELECTOR, "[name = 'login-password']")
    LOG_SUBMIT = (By.CSS_SELECTOR, "[name = 'login_submit']")
class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRICE_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    TITLE_CART = (By.CSS_SELECTOR, "#messages :first-child .alertinner :only-of-type")
    TITLE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
