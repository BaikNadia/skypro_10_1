# Виджет банковских операций клиента

### Этот проект представляет собой инструмент для обработки данных банковских операций. Он включает функции для маскирования номеров счетов и карт, форматирования дат, фильтрации операций по состоянию и сортировки операций по дате.

Проект предоставляет следующие функции:


get_mask_card_number
get_mask_account
mask_account_card
get_date
filter_by_state
sort_by_date


Пример:

```markdown
## Функции

### get_mask_card_number

#### Описание:

Маскирует номер банковской карты, показывая первые 6 и последние 4 цифры.

#### Параметры:

- `card_number` (str): Номер банковской карты.

#### Возвращаемое значение:

- (str): Маскированный номер карты.

#### Пример:

```python
masked_card = get_mask_card_number("4567891234567890")
print(masked_card)  # Вывод: "4567 89** **** 7890"
```
## Произведено тестирование работы следующих функций:
### Модуль masks
Функция get_mask_card_number:

Тестирование правильности маскирования номера карты.
Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.

Функция get_mask_account:

Тестирование правильности маскирования номера счета.
Проверка работы функции с различными форматами и длинами номеров счетов.
Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.

### Модуль widget
Функция mask_account_card:

Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

Функция get_date:

Тестирование правильности преобразования даты.
Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.

### Модуль processing
Функция filter_by_state:

Тестирование фильтрации списка словарей по заданному статусу state.
Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
Параметризация тестов для различных возможных значений статуса state.

Функция sort_by_date:

Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
Проверка корректности сортировки при одинаковых датах.
Тесты на работу функции с некорректными или нестандартными форматами дат.