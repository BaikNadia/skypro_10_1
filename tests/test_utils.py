import json
from unittest.mock import patch

from src.utils import convert_currency, count_operations_by_category
from src.utils import read_json_file


def test_read_valid_json(tmp_path):
    # Создаем временный JSON-файл
    json_data = [{"id": 1, "amount": 100, "currency": "USD"}]
    json_file = tmp_path / "valid.json"
    json_file.write_text(json.dumps(json_data))

    result = read_json_file(str(json_file))
    assert result == json_data


def test_read_nonexistent_file():
    result = read_json_file("nonexistent.json")
    assert result == []


def test_read_invalid_json(tmp_path):
    # Создаем файл с некорректным содержимым
    invalid_json_file = tmp_path / "invalid.json"
    invalid_json_file.write_text("not a json")

    result = read_json_file(str(invalid_json_file))
    assert result == []


def test_read_empty_json(tmp_path):
    # Создаем пустой JSON-файл
    empty_json_file = tmp_path / "empty.json"
    empty_json_file.write_text("[]")

    result = read_json_file(str(empty_json_file))
    assert result == []


@patch("requests.get")
def test_convert_usd_to_rub(mock_get):
    # Мокируем ответ API
    mock_response = {
        "rates": {"RUB": 75.0}
    }
    mock_get.return_value.json.return_value = mock_response

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_currency(transaction)
    assert result == 7500.0  # 100 USD * 75 RUB/USD


@patch("requests.get")
def test_convert_eur_to_rub(mock_get):
    # Мокируем ответ API
    mock_response = {
        "rates": {"RUB": 85.0}
    }
    mock_get.return_value.json.return_value = mock_response

    transaction = {"amount": 200, "currency": "EUR"}
    result = convert_currency(transaction)
    assert result == 17000.0  # 200 EUR * 85 RUB/EUR


def test_convert_rub_no_conversion():
    transaction = {"amount": 150, "currency": "RUB"}
    result = convert_currency(transaction)
    assert result == 150.0  # Сумма остается без изменений


def test_convert_missing_currency():
    transaction = {"amount": 100}  # Отсутствует ключ 'currency'
    result = convert_currency(transaction)
    assert result == 0.0  # Возвращается 0.0 при отсутствии данных


def test_convert_missing_amount():
    transaction = {"currency": "USD"}  # Отсутствует ключ 'amount'
    result = convert_currency(transaction)
    assert result == 0.0  # Возвращается 0.0 при отсутствии данных


from src.utils import search_operations_by_description


def test_search_operations_by_description():
    """
    Тестирует функцию поиска операций по описанию.
    """
    operations = [
        {"id": "650703", "description": "Перевод организации"},
        {"id": "3598919", "description": "Перевод с карты на карту"},
        {"id": "593027", "description": "Перевод с карты на карту"}
    ]

    result = search_operations_by_description(operations, "организации")
    assert len(result) == 1
    assert result[0]["id"] == "650703"

    result = search_operations_by_description(operations, "с карты на карту")
    assert len(result) == 2
    assert result[0]["id"] == "3598919"
    assert result[1]["id"] == "593027"

    result = search_operations_by_description(operations, "неexistent")
    assert len(result) == 0


def test_count_operations_by_category():
    """
    Тестирует функцию подсчета операций по категориям.
    """
    operations = [
        {"id": "650703", "description": "Перевод организации"},
        {"id": "3598919", "description": "Перевод с карты на карту"},
        {"id": "593027", "description": "Перевод с карты на карту"},
        {"id": "4816780", "description": "Открытие вклада"}
    ]

    category_mapping = {
        "Перевод между счетами": r"со счета на счет",
        "Перевод между картами": r"с карты на карту",
        "Открытие вклада": r"открытие вклада"
    }

    result = count_operations_by_category(operations, category_mapping)
    assert result["Перевод между картами"] == 2
    assert result["Открытие вклада"] == 1
    assert "Перевод между счетами" not in result
