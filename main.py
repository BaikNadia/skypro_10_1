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
    print(get_date("invalid-date-format"))  # Вывод: "Некорректный формат даты"

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

from src.file_reader import read_json_file, read_csv_file, read_excel_file
from src.utils import search_operations_by_description, count_operations_by_category
import os


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор источника данных
    source_menu = {
        "1": ("JSON-файл", read_json_file),
        "2": ("CSV-файл", read_csv_file),
        "3": ("Excel-файл", read_excel_file)
    }

    while True:
        print("\nВыберите необходимый пункт меню:")
        for key, (source_name, _) in source_menu.items():
            print(f"{key}. Получить информацию о транзакциях из {source_name}")

        choice = input("Введите номер пункта меню: ")
        if choice in source_menu:
            source_name, read_function = source_menu[choice]
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    file_path = input(f"\nВведите путь к {source_name}: ")
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    operations = read_function(file_path)
    if not operations:
        print("Не удалось прочитать операции из файла.")
        return

    print(f"\nДля обработки выбран {source_name}.")

    # Фильтрация по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input("\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
                       "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n"
                       "Статус: ").upper()  # Приводим к верхнему регистру

        if status in valid_statuses:
            filtered_operations = [op for op in operations if op.get("state") == status]
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    if not filtered_operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Сортировка по дате
    sort_choice = input("\nОтсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        ascending_choice = input("Отсортировать по возрастанию или по убыванию? (asc/desc): ").lower()
        try:
            filtered_operations.sort(key=lambda x: x.get("date"), reverse=(ascending_choice == "desc"))
            print(f"Операции отсортированы по дате ({ascending_choice}).")
        except KeyError:
            print("Ошибка: В некоторых операциях отсутствует поле 'date'.")

    # Фильтрация только рублевых транзакций
    ruble_choice = input("\nВыводить только рублевые транзакции? Да/Нет: ").lower()
    if ruble_choice == "да":
        filtered_operations = [op for op in filtered_operations if op.get("currency_code") == "RUB"]
        print("Список отфильтрован только по рублевым транзакциям.")

    # Поиск по слову в описании
    search_choice = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if search_choice == "да":
        search_string = input("Введите слово для поиска: ")
        filtered_operations = search_operations_by_description(filtered_operations, search_string)
        if not filtered_operations:
            print("Не найдено ни одной транзакции, соответствующей вашему запросу.")
            return
        print(f"Транзакции отфильтрованы по слову \"{search_string}\".")

    # Расчет количества операций по категориям
    categories = ["Перевод с карты на карту", "Перевод со счета на счет", "Открытие вклада", "Перевод организации"]
    category_counts = count_operations_by_category(filtered_operations, categories)
    print("\nКоличество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    # Вывод итогового списка транзакций
    if not filtered_operations:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(filtered_operations)}")

    for i, operation in enumerate(filtered_operations):
        date = operation.get("date", "").split("T")[0]  # Берем только дату
        description = operation.get("description", "Без описания")
        amount = operation.get("amount", "0")
        currency_code = operation.get("currency_code", "RUB")
        from_account = operation.get("from", "")
        to_account = operation.get("to", "")

        # Маскировка номеров счетов и карт
        def mask_account(account_str):
            if account_str.startswith("Счет"):
                return f"Счет **{account_str[-4:]}"
            elif account_str:
                return f"{account_str[:4]} {account_str[4:6]}** **** {account_str[-4:]}"
            return ""

        from_masked = mask_account(from_account)
        to_masked = mask_account(to_account)

        print(f"\n{i + 1}. {date} {description}")
        if from_masked:
            print(f"{from_masked} -> ", end="")
        print(f"{to_masked}")
        print(f"Сумма: {amount} {currency_code}")
