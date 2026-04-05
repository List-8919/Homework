def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    card_str = str(card_number)
    mask = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

    return mask


def get_mask_account(account_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    account_str = str(account_number)
    return f"**{account_str[-4:]}"


print(get_mask_account("73654108430135874305"))
print(get_mask_card_number("Visa Platinum 7000792289606361"))
