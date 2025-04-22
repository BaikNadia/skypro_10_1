from dotenv import load_dotenv

from src.masks import get_mask_card_number, get_mask_account
from src.utils import read_json_file

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
