from .base_page import BasePage
from .locators import MainPageLocators
import time
from retrying import retry

class MainPage(BasePage):
    @retry(stop_max_attempt_number=3, wait_fixed=2000)
    def go_to_pre_open_market(self):
        self.hover_on_element(MainPageLocators.MARKET_DATA_LINK)
        self.click_element(MainPageLocators.PRE_OPEN_MARKET_LINK)

    def go_to_nifty_bank_page(self):
        self.click_element(MainPageLocators.NIFTY_BANK_LINK)

    def go_to_view_all(self):
        view_all_link = self.browser.find_element(*MainPageLocators.VIEW_ALL_LINK)
        self.browser.execute_script("window.scrollTo(0, 800);")
        self.click_element(view_all_link)