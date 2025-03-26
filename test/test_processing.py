import pytest
from datetime import datetime
from src.processing import filter_by_state

@pytest.mark.parametrize("transactions, state, expected", [
    (  # Транзакции с различными состояниями
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "PENDING"},
            {"id": 3, "state": "EXECUTED"}
        ],
        "EXECUTED",
        [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]
    ),
    (  # Нет транзакций с указанным состоянием
        [
            {"id": 1, "state": "PENDING"},
            {"id": 2, "state": "CANCELED"}
        ],
        "EXECUTED",
        []
    ),
    (  # Пустой список транзакций
        [],
        "EXECUTED",
        []
    ),
    (  # Другое состояние
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "PENDING"}
        ],
        "PENDING",
        [{"id": 2, "state": "PENDING"}]
    )
])
def test_filter_by_state(transactions, state, expected):
    """
    Проверяет корректность фильтрации списка словарей по заданному статусу state.
    """
    result = filter_by_state(transactions, state)
    assert result == expected, f"Ошибка при фильтрации по статусу {state}"

def sort_by_date(transactions, ascending=True):
    """
    Сортирует список словарей по датам в порядке возрастания или убывания.

    :param transactions: Список словарей с данными о транзакциях.
    :param ascending: Порядок сортировки (True - по возрастанию, False - по убыванию).
    :return: Отсортированный список словарей.
    """
    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x.get("date", "1970-01-01")),
        reverse=not ascending
    )
