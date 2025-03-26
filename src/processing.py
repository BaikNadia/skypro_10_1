def filter_by_state(transactions, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: Значение, по которому фильтруются словари (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'PENDING', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]

filtered_transactions = filter_by_state(transactions, state='EXECUTED')
print(filtered_transactions)



from datetime import datetime

def sort_by_date(transactions, ascending=True):
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей с данными о банковских операциях.
    :param ascending: Порядок сортировки (True - по возрастанию, False - по убыванию).
    :return: Отсортированный список словарей.
    """
    return sorted(
        transactions,
        key=lambda x: datetime.strptime(x.get('date', '1970-01-01'), '%Y-%m-%d'),
        reverse=not ascending
    )

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'PENDING', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]

sorted_transactions = sort_by_date(transactions, ascending=False)
print(sorted_transactions)

