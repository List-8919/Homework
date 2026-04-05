# Импорт модуля re
import re

from src.masks import get_mask_account, get_mask_card_number


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
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Счет 35383033474447895560"))


def get_date(formated_date: str) -> str:
    """Функция преобразует дату в формат 'DD.MM.YYYY'"""
    date_split_list = formated_date.split('T')
    formated_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", date_split_list[0])
    return formated_date


print(get_date("2024-03-11T02:26:18.671407"))
