import time

from .base_page import BasePage
from .locators import TwitterElonMuskPageLocators


class TwitterElonMuskPage(BasePage):
    def parse_ten_last_twits(self):
        twit_text_array = []
        twit_text_array_unique = []
        current_scroll_position = 0
        scroll_increment = 200

        while True:
            self.browser.execute_script(f'window.scrollTo(0, {current_scroll_position});')
            time.sleep(1)

            twits = self.browser.find_elements(*TwitterElonMuskPageLocators.TWITS)
            for twit in twits:
                twit_text = twit.find_elements(*TwitterElonMuskPageLocators.TWITS_TEXT)
                twit_text_array.append(twit_text[0].text)
                print(twit_text_array)

            for text in twit_text_array:
                if text not in twit_text_array_unique:
                    twit_text_array_unique.append(text)

            if len(twit_text_array_unique) >= 10:
                break
            current_scroll_position += scroll_increment

        print(twit_text_array_unique)

        with open('logfile.txt', 'w') as log_file:
            # Записываем каждый элемент списка twit_text_array_unique в файл
            for twit_text in twit_text_array_unique:
                log_file.write(twit_text + '\n')