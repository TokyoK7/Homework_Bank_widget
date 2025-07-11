def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX."""
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счёта в формате **XXXX."""
    if len(account_number) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"

