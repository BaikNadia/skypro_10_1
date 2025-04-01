def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency: Валюта для фильтрации (например, 'USD').
    :return: Итератор с транзакциями, где валюта соответствует заданной.
    """
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction



def transaction_descriptions(transactions):
    """
    Генерирует описания операций из списка транзакций.

    :param transactions: Список словарей с транзакциями.
    :yield: Описание каждой операции (строка).
    """
    for transaction in transactions:
        description = transaction.get("description")  # Получаем значение по ключу "description"
        if description is not None:  # Проверяем, что описание существует
            yield description


def card_number_generator(start=1, end=9999999999999999):
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение диапазона (по умолчанию 1).
    :param end: Конечное значение диапазона (по умолчанию 9999999999999999).
    :yield: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    # Проверяем корректность диапазона
    if start < 1 or end > 9999999999999999 or start > end:
        raise ValueError("Неверный диапазон для номеров карт")

    for number in range(start, end + 1):
        # Форматируем число в строку длиной 16 символов с нулями слева
        formatted_number = f"{number:016d}"

        # Разбиваем строку на группы по 4 цифры и объединяем через пробелы
        card_number = " ".join([formatted_number[i:i + 4] for i in range(0, 16, 4)])

        yield card_number
