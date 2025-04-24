import json
import os

import requests
from dotenv import load_dotenv

from src.logging_config import setup_logger

# Создаем логгер для модуля utils
logger = setup_logger("utils")


def read_json_file() -> list:
    """
    Читает JSON-файл с транзакциями из переменной окружения OPERATIONS_FILE.

    :return: Список словарей с данными о транзакциях или пустой список при ошибках.
    """
    file_path = os.getenv("OPERATIONS_FILE")  # Берём путь из переменной окружения

    if not file_path:
        logger.critical("Переменная окружения OPERATIONS_FILE не задана.")
        return []

    logger.debug(f"Попытка чтения JSON-файла по пути: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):  # Проверяем, что данные — это список
                logger.info(f"Успешно прочитано {len(data)} транзакций из файла: {file_path}")
                return data
            else:
                logger.error(f"Некорректный формат данных в файле: {file_path}. Ожидался список.")
                return []
    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Ошибка чтения JSON-файла: {file_path}. Подробности: {str(e)}")
        return []


def convert_currency(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции из USD или EUR в рубли.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях (тип float).
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if not amount or not currency:
        return 0.0  # Если отсутствуют данные о сумме или валюте, возвращаем 0.0

    if currency == "RUB":
        return float(amount)  # Если валюта уже в рублях, ничего не меняем

    # Получаем курс валюты через API
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    if not api_key:
        raise EnvironmentError("Отсутствует переменная окружения EXCHANGE_RATE_API_KEY")

    url = f"http://api.exchangerate-api.com/v4/latest/{currency}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверяем статус ответа
        rates = response.json().get("rates", {})
        rub_rate = rates.get("RUB", 1.0)  # Если нет курса RUB, используем значение 1.0
        return float(amount) * rub_rate
    except (requests.RequestException, KeyError, ValueError):
        return float(amount)  # При ошибке возвращаем сумму без конвертации


load_dotenv()  # Загружаем переменные окружения из .env
