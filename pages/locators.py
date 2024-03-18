from selenium.webdriver.common.by import By


class MainPageLocators():
    MARKET_DATA_LINK = (By.CSS_SELECTOR, '#link_2')
    PRE_OPEN_MARKET_LINK = (By.CSS_SELECTOR, 'a[href="/market-data/pre-open-market-cm-and-emerge-market"]')
    HOME_PAGE_LINK = (By.CSS_SELECTOR, '#link_0')
    NIFTY_BANK_LINK = (By.CSS_SELECTOR, '#tabList_NIFTYBANK')
    VIEW_ALL_LINK = (By.CSS_SELECTOR, 'a[href="/market-data/live-equity-market?symbol=NIFTY BANK"]')


class PreOpenMarketPageLocators():
    TABLE_BODY_ROWS = (By.CSS_SELECTOR, 'table[id="livePreTable"] tbody tr')
    TABLE_HEAD_CELLS = (By.CSS_SELECTOR, 'table[id="livePreTable"] thead th')
    TABLE_BODY_CELL = (By.CSS_SELECTOR, 'td')


class NiftyBankPageLocators():
    SELECTOR_LIST = (By.CSS_SELECTOR, '#equitieStockSelect')


class TwitterElonMuskPageLocators():
    TWITS = (By.XPATH, '//article[@data-testid="tweet"]')
    TWITS_TEXT = (By.XPATH, '//div[@data-testid="tweetText"]')