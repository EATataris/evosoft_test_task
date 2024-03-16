from .pages.main_page import MainPage


def test_run(browser):
    link = "https://www.nseindia.com/"
    page = MainPage(browser, link)
    page.open()