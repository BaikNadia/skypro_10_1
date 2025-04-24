import pytest

from src.masks import get_mask_card_number, get_mask_account


# Параметризованные тесты для корректных номеров карт
@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),  # Корректный номер
    ("9876543210987654", "9876 54** **** 7654"),  # Другой корректный номер
])
def test_get_mask_card_number_valid(card_number, expected):
    """
    Проверяет правильность маскирования номера карты для корректных входных данных.
    """
    result = get_mask_card_number(card_number)
    assert result == expected, f"Ошибка при маскировании номера {card_number}"


# Параметризованные тесты для некорректных номеров карт
@pytest.mark.parametrize("card_number", [
    "123456789012345",  # Недостаточно цифр (15)
    "12345678901234567",  # Слишком много цифр (17)
    "1234-5678-9012-3456",  # Недопустимый формат (с дефисами)
    "123456789012345X",  # Недопустимый символ (буква X)
    "",  # Пустая строка
    "   ",  # Пробельные символы
    None,  # None вместо строки
])
def test_get_mask_card_number_invalid(card_number):
    """
    Проверяет обработку ошибок для некорректных входных данных.
    """
    with pytest.raises(ValueError, match="Неверный формат номера карты"):
        if card_number is not None:
            get_mask_card_number(str(card_number))
        else:
            get_mask_card_number(card_number)


# Тестирование граничных случаев
def test_get_mask_card_number_edge_cases():
    """
    Проверяет работу функции для граничных случаев.
    """
    # Минимальная длина (16 цифр)
    valid_number = "1234567890123456"
    result = get_mask_card_number(valid_number)
    assert result == "1234 56** **** 3456", "Ошибка при маскировании минимальной длины"

    # Случай с пробелами в начале/конце строки
    number_with_spaces = "   1234567890123456   "
    result = get_mask_card_number(number_with_spaces.strip())
    assert result == "1234 56** **** 3456", "Ошибка при обработке строки с пробелами"


# Параметризованные тесты для корректных номеров счетов
@pytest.mark.parametrize("account_number, expected", [
    ("123456789012", "**9012"),  # Корректный номер счета
    ("987654321098", "**1098"),  # Другой корректный номер счета
    ("1234", "**1234"),  # Минимальная длина (4 символа)
])
def test_get_mask_account_valid(account_number, expected):
    """
    Проверяет правильность маскирования номера счета для корректных входных данных.
    """
    result = get_mask_account(account_number)
    assert result == expected, f"Ошибка при маскировании номера {account_number}"


# Параметризованные тесты для некорректных номеров счетов
@pytest.mark.parametrize("account_number", [
    "123",  # Недостаточно цифр (меньше 4)
    "12345X",  # Недопустимый символ (буква X)
    "",  # Пустая строка
    "   ",  # Пробельные символы
    None,  # None вместо строки
])
def test_get_mask_account_invalid(account_number):
    """
    Проверяет обработку ошибок для некорректных входных данных.
    """
    with pytest.raises(ValueError, match="Неверный формат номера счета"):
        if account_number is not None:
            get_mask_account(str(account_number))

        else:
            get_mask_account(account_number)


# Тестирование граничных случаев
def test_get_mask_account_edge_cases():
    """
    Проверяет работу функции для граничных случаев.
    """
    # Минимальная длина (4 цифры)
    valid_number = "1234"
    result = get_mask_account(valid_number)
    assert result == "**1234", "Ошибка при маскировании минимальной длины"

    # Случай с пробелами в начале/конце строки
    number_with_spaces = "   123456789012   "
    result = get_mask_account(number_with_spaces.strip())
    assert result == "**9012", "Ошибка при обработке строки с пробелами"
