from src.utils import read_json_file

if __name__ == "__main__":
    file_path = "data/operations.json"
    transactions = read_json_file(file_path)

    if transactions:
        print(f"Прочитано {len(transactions)} транзакций.")
    else:
        print("Не удалось прочитать транзакции.")
