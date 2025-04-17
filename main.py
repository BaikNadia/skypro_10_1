from src.utils import read_json_file
from src.masks import get_mask_card_number, get_mask_account
from dotenv import load_dotenv
import os



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
