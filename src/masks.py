from typing import Union


from src.logging_config import setup_logger

# Создаем логгер для модуля masks
logger = setup_logger("masks")


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    :param card_number: Строка с номером карты (16 цифр)
    :return: Замаскированный номер карты
    """
    if not card_number.isdigit() or len(card_number) != 16:
        logger.error(f"Неверный формат номера карты: {card_number}")
        raise ValueError("Неверный формат номера карты")

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Маскировка номера карты: {card_number} -> {masked_number}")
    return masked_number



def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.

    :param account_number: Строка с номером счета (может быть больше 4 цифр)
    :return: Замаскированный номер счета
    """
    if not account_number.isdigit() or len(account_number) < 4:
        logger.error(f"Неверный формат номера счета: {account_number}")
        raise ValueError("Неверный формат номера счета")

    masked_number = f"**{account_number[-4:]}"
    logger.info(f"Маскировка номера счета: {account_number} -> {masked_number}")
    return masked_number
