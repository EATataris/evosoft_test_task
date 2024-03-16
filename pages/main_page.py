from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def go_to_pre_open_market(self):
        self.hover_on_element(MainPageLocators.MARKET_DATA_LINK)

        self.click_element(MainPageLocators.PRE_OPEN_MARKET_LINK)
        time.sleep(3)

