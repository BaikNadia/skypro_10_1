import os
import json
import requests
from dotenv import load_dotenv

def read_json_file(file_path: str) -> list:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список при ошибках.
    """
    if not os.path.exists(file_path):
        return []  # Если файл не существует, возвращаем пустой список

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):  # Проверяем, что данные — это список
                return data
            else:
                return []  # Если данные не являются списком, возвращаем пустой список
    except (json.JSONDecodeError, ValueError):
        return []  # Если файл поврежден или пустой, возвращаем пустой список


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
