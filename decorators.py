import functools
import logging
import os


def log(filename=None):
    """
    Декоратор для логирования начала, конца и результатов выполнения функции.

    :param filename: Имя файла для записи логов (если None, логи выводятся в консоль).
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Создаем логгер для функции
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if filename:
                # Проверяем, существует ли директория для файла
                log_dir = os.path.dirname(filename)
                if log_dir and not os.path.exists(log_dir):
                    os.makedirs(log_dir)

                # Настройка записи в файл
                handler = logging.FileHandler(filename)
            else:
                # Настройка вывода в консоль
                handler = logging.StreamHandler()

            # Форматирование логов
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                # Логируем начало выполнения функции
                logger.info(f"Начало выполнения функции {func.__name__} с аргументами args={args}, kwargs={kwargs}")

                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение и результат
                logger.info(f"Функция {func.__name__} успешно завершилась. Результат: {result}")
                return result
            except Exception as e:
                # Логируем ошибку
                logger.error(f"Ошибка при выполнении функции {func.__name__}. "
                             f"Тип ошибки: {type(e).__name__}, Аргументы: args={args}, kwargs={kwargs}, Сообщение: {str(e)}")
                raise  # Передаем исключение дальше
            finally:
                # Удаляем обработчик после выполнения функции
                logger.removeHandler(handler)

        return wrapper

    return decorator
