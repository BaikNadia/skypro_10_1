import os

import pytest

from src.file_reader import read_csv_file, read_excel_file

print(os.getcwd())

def test_read_real_csv():
    """
    Тестирует функцию чтения реального CSV-файла.
    """
    # Определяем абсолютный путь к файлу
    project_root = os.path.dirname(os.path.abspath(__file__))  # Корень проекта (директория tests)
    file_path = os.path.join(project_root, "..", "data", "transactions.csv")

    if not os.path.exists(file_path):
        pytest.skip(f"Файл {file_path} не найден.")  # Пропускаем тест, если файл отсутствует

    result = read_csv_file(file_path)

    assert len(result) > 0, "CSV-файл должен содержать данные."
    assert all(isinstance(t, dict) for t in result), "Каждый элемент списка должен быть словарем."

    expected_first_transaction = {
        'id': '650703',
        'state': 'EXECUTED',
        'date': '2023-09-05T11:30:32Z',
        'amount': '16210',
        'currency_name': 'Sol',
        'currency_code': 'PEN',
        'from': 'Счет 58803664561298323391',
        'to': 'Счет 39745660563456619397',
        'description': 'Перевод организации'
    }
    assert result[0] == expected_first_transaction, "Первая транзакция не соответствует ожидаемой."


def test_read_real_excel():
    """
    Тестирует функцию чтения реального Excel-файла.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))  # Корень проекта (директория tests)
    file_path = os.path.join(project_root, "..", "data", "transactions.xlsx")

    if not os.path.exists(file_path):
        pytest.skip(f"Файл {file_path} не найден.")  # Пропускаем тест, если файл отсутствует

    result = read_excel_file(file_path)

    # Проверяем, что данные успешно прочитаны
    assert len(result) > 0
    assert all(isinstance(t, dict) for t in result)

    # Проверяем конкретные данные
    expected_first_transaction = {
        'id': 650703,
        'state': 'EXECUTED',
        'date': '2023-09-05T11:30:32Z',
        'amount': 16210,
        'currency_name': 'Sol',
        'currency_code': 'PEN',
        'from': 'Счет 58803664561298323391',
        'to': 'Счет 39745660563456619397',
        'description': 'Перевод организации'
    }
    assert result[0] == expected_first_transaction
