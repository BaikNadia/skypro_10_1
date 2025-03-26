def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.
    Формат: первые 4 цифры, затем 2 цифры **, затем ****, затем последние 4 цифры.

    :param card_number: Номер карты (строка из 16 цифр)
    :return: Замаскированный номер карты
    :raises ValueError: Если номер карты имеет недопустимый формат
    """
    if not isinstance(card_number, str) or not card_number.strip():
        raise ValueError("Неверный формат номера карты")

    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Неверный формат номера карты")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета.
    Формат: ** + последние 4 цифры.

    :param account_number: Номер счета (строка из цифр)
    :return: Замаскированный номер счета
    :raises ValueError: Если номер счета имеет недопустимый формат
    """
    if not isinstance(account_number, str) or not account_number.strip():
        raise ValueError("Неверный формат номера счета")

    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Неверный формат номера счета")

    return f"**{account_number[-4:]}"

