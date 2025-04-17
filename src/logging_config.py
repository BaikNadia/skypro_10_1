import logging
import os

def setup_logger(module_name: str):
    """
    Настройка логгера для указанного модуля с уровнем логирования DEBUG.

    :param module_name: Название модуля (например, 'masks' или 'utils').
    :return: Logger для указанного модуля.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = f"{log_dir}/{module_name}.log"

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования как DEBUG

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
