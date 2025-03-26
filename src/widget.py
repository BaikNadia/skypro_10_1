import re
from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета и добавляет метку времени.

    :param info: Строка в формате 'Visa Platinum 7000792289606361', 'Maestro 7000792289606361' или 'Счет 73654108430135874305'
    :return: Строка с замаскированным номером и меткой времени
    """
    # Извлекаем последовательность цифр из строки
    numbers = re.findall(r'\d+', info)

    if not numbers:
        return "Некорректный формат данных"

    number = numbers[0]

    if "счет" in info.lower():
        try:
            return get_mask_account(number)
        except ValueError:
            return "Некорректный формат данных"
    else:
        try:
            return get_mask_card_number(number)
        except ValueError:
            return "Некорректный формат данных"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата 'YYYY-MM-DDTHH:MM:SS' в формат 'DD.MM.YYYY'.

    :param date_str: Строка с датой в формате ISO.
    :return: Строка с датой в формате 'DD.MM.YYYY'.
    :raises ValueError: Если формат даты неверный.
    """
    if not date_str or not isinstance(date_str, str):
        return "Некорректный формат даты"

    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректный формат даты"
