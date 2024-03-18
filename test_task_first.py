from .pages.main_page import MainPage
from .pages.pre_open_market_page import PreOpenMarketPage
from .pages.nyfty_bank_page import NiftyBankPage


def test_run(browser):
    link = "https://www.nseindia.com/"
    page = MainPage(browser, link)
    page.open()
    try:
        page.go_to_pre_open_market()
    except Exception as e:
        print("Не удалось получить доступ к сайту:", str(e))
    pre_open_market_page = PreOpenMarketPage(browser, browser.current_url)
    pre_open_market_page.parce_data_to_csv()
    try:
        pre_open_market_page.go_to_home_page()
    except Exception as e:
        print("Не удалось получить доступ к сайту:", str(e))
    page = MainPage(browser, browser.current_url)
    page.go_to_nifty_bank_page()
    page.go_to_view_all()
    nifty_bank_page = NiftyBankPage(browser, browser.current_url)
    nifty_bank_page.click_selector_list_choose_and_scroll_table()