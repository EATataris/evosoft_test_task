from .pages.twitter_elonmusk_page import TwitterElonMuskPage


def test_run(browser):
    link = "https://twitter.com/elonmusk"
    page = TwitterElonMuskPage(browser, link)
    page.open()
    page.parse_ten_last_twits()