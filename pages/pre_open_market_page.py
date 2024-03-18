from selenium.common import StaleElementReferenceException
from retrying import retry
from .base_page import BasePage
from .locators import PreOpenMarketPageLocators, MainPageLocators
import time, csv


class PreOpenMarketPage(BasePage):
    def parce_data_to_csv(self):
        table_head_cells = self.browser.find_elements(*PreOpenMarketPageLocators.TABLE_HEAD_CELLS)
        time.sleep(3)
        data_csv = []

        table_head_cells_data = []
        for cell in table_head_cells:
            table_head_cells_data.append(cell.text)

        print(table_head_cells_data)
        for _ in range(3):
            try:
                table_body_rows = self.browser.find_elements(*PreOpenMarketPageLocators.TABLE_BODY_ROWS)

                for row in table_body_rows:
                    cells = row.find_elements(*PreOpenMarketPageLocators.TABLE_BODY_CELL)
                    company_name = cells[table_head_cells_data.index('SYMBOL')].text
                    total_price = cells[table_head_cells_data.index('FINAL')].text
                    data_csv.append([company_name, total_price])
                break
            except StaleElementReferenceException:
                continue

        with open('company_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Имя", "Цена"])
            writer.writerows(data_csv[:-1])

    @retry(stop_max_attempt_number=3, wait_fixed=2000)
    def go_to_home_page(self):
        self.click_element(MainPageLocators.HOME_PAGE_LINK)