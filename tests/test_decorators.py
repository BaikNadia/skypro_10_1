import pytest

from decorators import log


# Тест логирования в консоль
def test_log_with_console(capsys):
    @log()
    def test_function(x, y):
        return x + y

    # Вызываем функцию
    test_function(5, 10)

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()

    # Объединяем stdout и stderr
    combined_logs = captured.out + captured.err

    # Проверяем логи
    assert "Начало выполнения функции test_function" in combined_logs
    assert "Функция test_function успешно завершилась. Результат: 15" in combined_logs


# Тест логирования ошибок в консоль
def test_log_with_error_in_console(capsys):
    @log()
    def test_function(x, y):
        if y == 0:
            raise ZeroDivisionError("Деление на ноль")
        return x / y

    # Вызываем функцию с ошибкой
    with pytest.raises(ZeroDivisionError):
        test_function(10, 0)

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()

    # Объединяем stdout и stderr
    combined_logs = captured.out + captured.err

    # Проверяем логи
    assert "Начало выполнения функции test_function" in combined_logs
    assert "Ошибка при выполнении функции test_function." in combined_logs
    assert "Тип ошибки: ZeroDivisionError" in combined_logs
    assert "Аргументы: args=(10, 0)" in combined_logs
    assert "Сообщение: Деление на ноль" in combined_logs
