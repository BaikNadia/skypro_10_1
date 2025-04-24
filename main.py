from dotenv import load_dotenv

from src.masks import get_mask_card_number, get_mask_account
from src.utils import read_json_file

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


# Загружаем переменные окружения
load_dotenv()

if __name__ == "__main__":
    transactions = read_json_file()  # Никаких параметров не нужно передавать
    if transactions:
        print(f"Прочитано {len(transactions)} транзакций.")

        for transaction in transactions:
            if "card_number" in transaction:
                try:
                    masked_card = get_mask_card_number(transaction["card_number"])
                    print(f"Маскированный номер карты: {masked_card}")
                except ValueError:
                    print("Ошибка маскировки карты")
            elif "account_number" in transaction:
                try:
                    masked_account = get_mask_account(transaction["account_number"])
                    print(f"Маскированный номер счета: {masked_account}")
                except ValueError:
                    print("Ошибка маскировки счета")
    else:
        print("Не удалось прочитать транзакции.")

from src.file_reader import read_csv_file

if __name__ == "__main__":
    file_path = "data/transactions.csv"
    transactions = read_csv_file(file_path)

    if transactions:
        print(f"Прочитано {len(transactions)} транзакций из CSV.")
        for transaction in transactions:
            print(transaction)
    else:
        print("Не удалось прочитать транзакции из CSV.")

from src.file_reader import read_excel_file

if __name__ == "__main__":
    file_path = "data/transactions.xlsx"
    transactions = read_excel_file(file_path)

    if transactions:
        print(f"Прочитано {len(transactions)} транзакций из Excel.")
        for transaction in transactions:
            print(transaction)
    else:
        print("Не удалось прочитать транзакции из Excel.")


from src.file_reader import read_csv_file, read_excel_file
from src.utils import search_operations_by_description, count_operations_by_category

def main():
    print("Выберите источник данных:")
    print("1. CSV-файл")
    print("2. Excel-файл")
    choice = input("Введите номер: ")

    if choice == "1":
        file_path = "data/transactions.csv"
        operations = read_csv_file(file_path)
    elif choice == "2":
        file_path = "data/transactions.xlsx"
        operations = read_excel_file(file_path)
    else:
        print("Неверный выбор.")
        return

    if not operations:
        print("Не удалось прочитать операции из файла.")
        return

    # Поиск операций по описанию
    search_string = input("Введите строку для поиска в описании: ")
    search_result = search_operations_by_description(operations, search_string)
    print(f"Найденные операции по запросу '{search_string}':")
    for operation in search_result:
        print(operation)

    # Подсчет операций по категориям
    category_mapping = {
        "Перевод между счетами": r"со счета на счет",
        "Перевод между картами": r"с карты на карту",
        "Открытие вклада": r"открытие вклада"
    }
    count_result = count_operations_by_category(operations, category_mapping)
    print("Количество операций по категориям:")
    for category, count in count_result.items():
        print(f"{category}: {count}")

