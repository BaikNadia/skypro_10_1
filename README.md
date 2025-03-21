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
