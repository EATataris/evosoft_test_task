from selenium.webdriver.common.by import By


class MainPageLocators():
    MARKET_DATA_LINK = (By.CSS_SELECTOR, '#link_2')
    PRE_OPEN_MARKET_LINK = (By.CSS_SELECTOR, 'a[href="/market-data/pre-open-market-cm-and-emerge-market"]')


class PreOpenMarketPageLocators():
    TABLE_HEAD_ROW = (By.XPATH, '//table[@id="livePreTable"]//thead//tr')
    TABLE_BODY_ROWS = (By.XPATH, '//table[@id="livePreTable"]//tbody//tr')

    TABLE_HEAD_CELLS = (By.CSS_SELECTOR, 'table[id="livePreTable"] thead th')
    TABLE_BODY_CELL = (By.CSS_SELECTOR, 'td')