from masks import get_mask_card_number, get_mask_account

# Импорт модуля re
import re

def mask_account_card(account_card: str) -> str:
    """
Принимает один аргумент — строку, содержащую тип и номер карты или счета,
и возвращает строку с замаскированным номером.
    """
    if "Счет" in account_card:
        letters_count = "".join(re.findall(r"\D+", account_card))
        numbers_count = "".join(re.findall(r"\d+", account_card))
        return f"{letters_count} {get_mask_account(numbers_count)}"
    else:
        letters_card = "".join(re.findall(r"\D+", account_card))
        numbers_card = "".join(re.findall(r"\d+", account_card))
        return f"{letters_card} {get_mask_card_number(numbers_card)}"

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

from datetime import datetime

def get_date(date: str) -> str:
    """Функция преобразует дату в формат 'DD.MM.YYYY'"""
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")
print(get_date("2024-03-11T02:26:18.671407"))