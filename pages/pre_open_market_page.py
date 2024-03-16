from .base_page import BasePage
from .locators import PreOpenMarketPageLocators
import time, csv


class PreOpenMarketPage(BasePage):
    def parce_data_to_csv(self):
        # table_head_row = self.browser.find_elements(*PreOpenMarketPageLocators.TABLE_HEAD_ROW)
        table_body_rows = self.browser.find_elements(*PreOpenMarketPageLocators.TABLE_BODY_ROWS)
        table_head_cells = self.browser.find_elements(*PreOpenMarketPageLocators.TABLE_HEAD_CELLS)
        print('Hi')

        data_scv = []

        table_head_cells_data = []
        for cell in table_head_cells:
            table_head_cells_data.append(cell.text)

        print(table_head_cells_data.index('SYMBOL'))
        print(table_head_cells_data.index('FINAL'))

        for row in table_body_rows:
            cells = row.find_elements(*PreOpenMarketPageLocators.TABLE_BODY_CELL)
            company_name = cells[table_head_cells_data.index('SYMBOL')].text
            total_price = cells[table_head_cells_data.index('FINAL')].text
            data_scv.append([company_name, total_price])

        with open('company_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Имя", "Цена"])
            writer.writerows(data_scv[:-1])