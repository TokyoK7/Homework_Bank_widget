card_number_str = input("Введите номер карты: ")
account_num = input("Введите номер счета: ")


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""

    return f"**{account_number[-4:]}"

print(get_mask_card_number(card_number_str))
print(get_mask_account(account_num))
