from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def __init__(self, browser, url, timeout=60):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_element(self, locator):
        print(f"Clicking element: {locator}")
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator)).click()

    def hover_on_element(self, locator):
        element = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(locator))
        ActionChains(self.browser).move_to_element(element).perform()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(locator)
        except NoSuchElementException:
            return False
        return True