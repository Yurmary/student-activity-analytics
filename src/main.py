import json
from gspread import service_account
import logging
from api_utils import fetch_data_from_api
from db_utils import create_tables, insert_data
from logging_utils import setup_logging
from email_utils import send_email
from gsheets_utils import update_google_sheets

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

gc = service_account.ServiceAccountCredentials.from_json_keyfile_dict(credentials)

def main():
    # Настройка логирования
    setup_logging()
    logging.info("Начало выполнения скрипта ETL")

    # Получение данных из API
    data = fetch_data_from_api()
    if not data:
        logging.error("Ответ от API пуст или не получен")
        return

    # Создание таблиц в PostgreSQL
    create_tables()

    # Вставка данных в PostgreSQL
    insert_data(data)
    logging.info("Данные успешно загружены в PostgreSQL")

    # Агрегация данных и обновление Google Sheets
    aggregated_data = aggregate_data(data)
    update_google_sheets(aggregated_data)
    logging.info("Данные успешно обновлены в Google Sheets")

    # Отправка email-уведомления
    send_email("Скрипт ETL успешно завершил выполнение", "Данные успешно загружены и агрегированы")
    logging.info("Оповещение на почту отправлено")

if __name__ == "__main__":
    main()
