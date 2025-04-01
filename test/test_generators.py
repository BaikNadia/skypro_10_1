import pytest

from src.generators import filter_by_currency, transaction_descriptions


# Функция для преобразования генератора в список
def generator_to_list(gen):
    return list(gen)


# Параметризованные тесты для корректных данных
@pytest.mark.parametrize("transactions, currency, expected", [
    (  # Транзакции с разными валютами
            [
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 2, "amount": 200, "currency": "EUR"},
                {"id": 3, "amount": 150, "currency": "USD"}
            ],
            "USD",
            [{"id": 1, "amount": 100, "currency": "USD"}, {"id": 3, "amount": 150, "currency": "USD"}]
    ),
    (  # Только одна транзакция в нужной валюте
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
def test_filter_by_currency_valid(transactions, currency, expected):
    """
    Проверяет корректность фильтрации транзакций по валюте.
    """
    result = generator_to_list(filter_by_currency(transactions, currency))
    assert result == expected, f"Ошибка при фильтрации по валюте {currency}"


# Тест на обработку случая отсутствия транзакций в заданной валюте
def test_filter_by_currency_no_matching_currency():
    """
    Проверяет, что функция возвращает пустой итератор, если нет транзакций в заданной валюте.
    """
    transactions = [
        {"id": 1, "amount": 100, "currency": "EUR"},
        {"id": 2, "amount": 200, "currency": "JPY"}
    ]
    result = generator_to_list(filter_by_currency(transactions, "USD"))
    assert result == [], "Ошибка: должен быть пустой список"


# Тест на обработку пустого списка транзакций
def test_filter_by_currency_empty_transactions():
    """
    Проверяет, что функция корректно работает с пустым списком транзакций.
    """
    transactions = []
    result = generator_to_list(filter_by_currency(transactions, "USD"))
    assert result == [], "Ошибка: должен быть пустой список"


# Тест на обработку списка без соответствующих валютных операций
def test_filter_by_currency_no_currency_key():
    """
    Проверяет, что функция не завершается ошибкой при обработке транзакций без ключа 'currency'.
    """
    transactions = [
        {"id": 1, "amount": 100},  # Отсутствует ключ 'currency'
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    result = generator_to_list(filter_by_currency(transactions, "USD"))
    assert result == [], "Ошибка: должен быть пустой список"


# Функция для преобразования генератора в список
def generator_to_list(gen):
    return list(gen)


# Параметризованные тесты для корректных данных
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
    (  # Нет описаний
            [
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 2, "amount": 200, "currency": "EUR"}
            ],
            []
    )
])
def test_transaction_descriptions_valid(transactions, expected):
    """
    Проверяет корректность возвращаемых описаний транзакций.
    """
    result = generator_to_list(transaction_descriptions(transactions))
    assert result == expected, f"Ошибка при получении описаний: {transactions}"


# Тест на работу с пустым списком транзакций
def test_transaction_descriptions_empty_transactions():
    """
    Проверяет, что функция корректно работает с пустым списком транзакций.
    """
    transactions = []
    result = generator_to_list(transaction_descriptions(transactions))
    assert result == [], "Ошибка: должен быть пустой список"


# Тест на работу с транзакциями без описаний
def test_transaction_descriptions_no_descriptions():
    """
    Проверяет, что функция игнорирует транзакции без описаний.
    """
    transactions = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR", "description": "Оплата услуг"},
        {"id": 3, "amount": 150, "currency": "USD"}
    ]
    result = generator_to_list(transaction_descriptions(transactions))
    assert result == ["Оплата услуг"], "Ошибка: должны быть только описания с ключом 'description'"


# Тест на работу с большим количеством транзакций
def test_transaction_descriptions_large_transactions():
    """
    Проверяет работу функции с большим количеством транзакций.
    """
    transactions = [
        {"id": i, "amount": i * 100, "currency": "USD", "description": f"Описание {i}"}
        for i in range(1, 11)  # 10 транзакций
    ]
    result = generator_to_list(transaction_descriptions(transactions))
    expected = [f"Описание {i}" for i in range(1, 11)]
    assert result == expected, "Ошибка: не все описания были возвращены"


# Параметризованные тесты для корректных данных
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
    (  # Нет описаний
            [
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 2, "amount": 200, "currency": "EUR"}
            ],
            []
    )
])
def test_transaction_descriptions_valid(transactions, expected):
    """
    Проверяет корректность возвращаемых описаний транзакций.
    """
    result = generator_to_list(transaction_descriptions(transactions))
    assert result == expected, f"Ошибка при получении описаний: {transactions}"


# Тест на работу с пустым списком транзакций
def test_transaction_descriptions_empty_transactions():
    """
    Проверяет, что функция корректно работает с пустым списком транзакций.
    """
    transactions = []
    result = generator_to_list(transaction_descriptions(transactions))
    assert result == [], "Ошибка: должен быть пустой список"


# Тест на работу с транзакциями без описаний
def test_transaction_descriptions_no_descriptions():
    """
    Проверяет, что функция игнорирует транзакции без описаний.
    """
    transactions = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR", "description": "Оплата услуг"},
        {"id": 3, "amount": 150, "currency": "USD"}
    ]
    result = generator_to_list(transaction_descriptions(transactions))
    assert result == ["Оплата услуг"], "Ошибка: должны быть только описания с ключом 'description'"


# Тест на работу с большим количеством транзакций
def test_transaction_descriptions_large_transactions():
    """
    Проверяет работу функции с большим количеством транзакций.
    """
    transactions = [
        {"id": i, "amount": i * 100, "currency": "USD", "description": f"Описание {i}"}
        for i in range(1, 11)  # 10 транзакций
    ]
    result = generator_to_list(transaction_descriptions(transactions))
    expected = [f"Описание {i}" for i in range(1, 11)]
    assert result == expected, "Ошибка: не все описания были возвращены"
