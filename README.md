# Тестовое задание от EvoSoft
## Парсер данных через селениум на сайте
https://www.nseindia.com/
Алгоритм:
1. Зайти на https://www.nseindia.com
2. Навестись (hover) на MARKET DATA
3. Кликнуть на Pre-Open Market
4. Спарсить данные Final Price по всем позициям на странице и вывести их в csv файл. Имя;цена

#### После этого сымитировать небольшой пользовательский сценарий использования сайта.
Здесь по своему желанию, но как пример:
1. Зайти на главную страницу
2. Пролистать вниз до графика
3. Выбрать график "NIFTY BANK"
4. Нажать “View all” под "TOP 5 STOCKS - NIFTY BANK"
5. Выбрать в селекторе “NIFTY ALPHA 50”
6. Пролистать таблицу до конца

# Парсинг последних твитов Elon Musk
Используя HTTP-запрос получить список последних 10 твитов Илона Маска .
Вывести в лог только текст (если есть) последних твитов.Действия должны повторять
пользовательский путь, официальное API Twitter в задаче не должно быть использовано.

## Стэк технологий
- Python
- Selenium Webdirver for Chrome browser
- Pytest

## Как запустить сервис
### * Для корректной работы должен быть обязательно установлен chromedriver последней версии и выполнены настройки разрешащие запускать chromedriver как исполняемый файл
1. git clone https://github.com/EATataris/evosoft_test_task

2. cd /evosoft_test_task

3. python -m venv vevn - создайте виртуальное окружение

4. - ./venv/bin/activate - активируйте виртуальное окружение (Linux)
   - venv\Scripts\activate.bat (Windows)
   - source selenium_env/bin/activate (macOS)

5. pip install -r requirements.txt - установить все необходимые пакеты
6. pytest -s test_task_first.py - Запускаем тестовый файл с первым заданием
7. pytest -s test_task_ыусщтв.py - Запускаем тестовый файл со вторым заданием