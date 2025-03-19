from typing import Union


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    :param card_number: Строка с номером карты (16 цифр)
    :return: Замаскированный номер карты
    """
    if not card_number.isdigit() or len(card_number) != 16:
        return "Некорректный номер карты"

    first_six = card_number[:6]  # Первые 6 цифр
    last_four = card_number[-4:]  # Последние 4 цифры

    masked_part = "**" + "****"  # Маска для средней части
    result = f"{first_six[:4]} {first_six[4:6]}{masked_part} {last_four}"
    return result


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.

    :param account_number: Строка с номером счета (может быть больше 4 цифр)
    :return: Замаскированный номер счета
    """
    if not account_number.isdigit():
        return "Некорректный номер счета"

    last_four = account_number[-4:]  # Последние 4 цифры
    result = f"**{last_four}"
    return result
