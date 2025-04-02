import pytest


from src.generators import filter_by_currency, card_number_generator, transaction_descriptions

# Фикстура для преобразования генератора в список
@pytest.fixture
def generator_to_list():
    def _convert(gen):
        return list(gen)
    return _convert

# Параметризованные тесты для filter_by_currency
@pytest.mark.parametrize("transactions, currency, expected", [
    (  # Несколько транзакций с разными валютами
        [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR"},
            {"id": 3, "amount": 150, "currency": "USD"}
        ],
        "USD",
        [{"id": 1, "amount": 100, "currency": "USD"}, {"id": 3, "amount": 150, "currency": "USD"}]
    ),
    (  # Одна транзакция в нужной валюте
        [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR"}
        ],
        "USD",
        [{"id": 1, "amount": 100, "currency": "USD"}]
    ),
    (  # Нет транзакций в заданной валюте
        [
            {"id": 1, "amount": 100, "currency": "EUR"},
            {"id": 2, "amount": 200, "currency": "JPY"}
        ],
        "USD",
        []
    ),
    (  # Пустой список транзакций
        [],
        "USD",
        []
    )
])
def test_filter_by_currency(generator_to_list, transactions, currency, expected):
    """
    Проверяет корректность фильтрации транзакций по валюте.
    """
    gen = filter_by_currency(transactions, currency)
    result = generator_to_list(gen)
    assert result == expected, f"Ошибка при фильтрации по валюте {currency}"

# Параметризованные тесты для transaction_descriptions
@pytest.mark.parametrize("transactions, expected", [
    (  # Несколько транзакций с описаниями
        [
            {"id": 1, "amount": 100, "currency": "USD", "description": "Перевод на счет"},
            {"id": 2, "amount": 200, "currency": "EUR", "description": "Оплата услуг"},
            {"id": 3, "amount": 150, "currency": "USD", "description": "Пополнение баланса"}
        ],
        ["Перевод на счет", "Оплата услуг", "Пополнение баланса"]
    ),
    (  # Одна транзакция с описанием
        [
            {"id": 1, "amount": 100, "currency": "USD", "description": "Перевод на счет"}
        ],
        ["Перевод на счет"]
    ),
    (  # Отсутствие описаний
        [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR", "description": None},
            {"id": 3, "amount": 150, "currency": "USD"}
        ],
        []
    ),
    (  # Пустой список транзакций
        [],
        []
    )
])
def test_transaction_descriptions(generator_to_list, transactions, expected):
    """
    Проверяет корректность получения описаний транзакций.
    """
    gen = transaction_descriptions(transactions)
    result = generator_to_list(gen)
    assert result == expected, f"Ошибка при получении описаний транзакций"



# Помощник для получения последнего элемента из генератора
def get_last_element(gen):
    """
    Возвращает последний элемент из генератора.
    """
    last_element = None
    for element in gen:
        last_element = element
    return last_element

# Параметризованные тесты для проверки корректности генерации номеров карт
@pytest.mark.parametrize("start, end, expected_first, expected_last", [
    (  # Диапазон из одного номера
        1, 1,
        "0000 0000 0000 0001",
        "0000 0000 0000 0001"
    ),
    (  # Маленький диапазон
        1, 3,
        "0000 0000 0000 0001",
        "0000 0000 0000 0003"
    ),
    (  # Большой диапазон
        9999, 10001,
        "0000 0000 0000 9999",
        "0000 0000 0001 0001"
    )
])
def test_card_number_generator_valid(start, end, expected_first, expected_last):
    """
    Проверяет корректность форматирования и диапазона генерации номеров карт.
    """
    gen = card_number_generator(start, end)

    # Получаем первый номер
    first_number = next(gen)
    assert first_number == expected_first, f"Ошибка при генерации первого номера в диапазоне {start}-{end}"

    # Получаем последний номер
    last_number = get_last_element(card_number_generator(start, end))
    assert last_number == expected_last, f"Ошибка при генерации последнего номера в диапазоне {start}-{end}"


