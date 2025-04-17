import logging
import os

def setup_logger(module_name: str):
    """
    Настройка логгера для указанного модуля.

    :param module_name: Название модуля (например, 'masks' или 'utils').
    :return: Logger для указанного модуля.
    """
    # Создаем директорию logs, если она не существует
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Имя файла лога
    log_file = f"{log_dir}/{module_name}.log"

    # Создаем логгер
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования

    # Создаем обработчик для записи в файл
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")  # Перезаписываем файл при каждом запуске
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
