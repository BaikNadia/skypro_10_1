from src.widget import mask_account_card, get_date


if __name__ == "__main__":
    print(mask_account_card("Card 7000792289606361"))  # Вывод: 7000 79** **** 6361
    print(mask_account_card("Account 73654108430135874305"))  # Вывод: **4305
    print(mask_account_card("Card 1234"))  # Вывод: Некорректный номер карты
    print(mask_account_card("Account abcdefg"))  # Вывод: Некорректный номер счета
    print(mask_account_card("Unknown 1234567890123456"))  # Вывод: Неизвестный тип

# Пример использования функции
if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))  # Вывод: "11.03.2024"
    print(get_date("2023-12-25T15:45:30.123456"))  # Вывод: "25.12.2023"
    print(get_date("invalid-date-format"))          # Вывод: "Некорректный формат даты"

from src.utils import read_json_file

file_path = "data/operations.json"
transactions = read_json_file(file_path)
print(transactions)