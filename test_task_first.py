from .pages.main_page import MainPage
from .pages.pre_open_market_page import PreOpenMarketPage


def test_run(browser):
    link = "https://www.nseindia.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_pre_open_market()
    pre_open_market_page = PreOpenMarketPage(browser, browser.current_url)
    pre_open_market_page.parce_data_to_csv()