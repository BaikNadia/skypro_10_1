from src.masks import get_mask_card_number, get_mask_account
import re
from datetime import datetime


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

    number = numbers[0]  # Берём первую найденную группу цифр

    # Определяем тип по ключевым словам
    if "счет" in info.lower():  # Если в строке есть слово "счет"
        masked_number = get_mask_account(number)
    else:  # В противном случае предполагаем, что это карта
        masked_number = get_mask_card_number(number)


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата 'YYYY-MM-DDTHH:MM:SS.mmmmmm' в формат 'ДД.ММ.ГГГГ'.

    :param date_str: Строка с датой в формате 'YYYY-MM-DDTHH:MM:SS.mmmmmm'
    :return: Строка с датой в формате 'ДД.ММ.ГГГГ'
    """
    try:
        # Парсим входную строку в объект datetime
        date_obj = datetime.fromisoformat(date_str)

        # Форматируем дату в нужный формат 'ДД.ММ.ГГГГ'
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date

    except ValueError:
        return "Некорректный формат даты"
