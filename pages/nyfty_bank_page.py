from .base_page import BasePage
from .locators import NiftyBankPageLocators
from selenium.webdriver.support.ui import Select
import time


class NiftyBankPage(BasePage):
    def click_selector_list_choose_and_scroll_table(self):
        select = Select(self.browser.find_element(*NiftyBankPageLocators.SELECTOR_LIST))
        select.select_by_visible_text('NIFTY ALPHA 50')
        time.sleep(3)
        self.browser.execute_script("window.scrollTo({left:0, top:1300, behavior:'smooth'});")
        time.sleep(3)

T