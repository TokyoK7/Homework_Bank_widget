from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Функция маскировки карты или счета."""
    if not user_card.strip():
        raise ValueError("Ошибка ввода! Пожалуйста введите корректный номер карты или счета.")

    if "Счет" in user_card:
        # Для счетов: "Счет 73654108430135874305" -> "Счет **4305"
        account_number = user_card[5:]  # Берем все после "Счет "
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"
    else:
        # Для карт: "Visa Classic 6831982476737658" -> "Visa Classic 6831 98** **** 7658"
        card_name = user_card[:-16].strip()  # Название карты (может быть несколько слов)
        card_number = user_card[-16:]  # Последние 16 цифр
        masked_number = get_mask_card_number(card_number)
        return f"{card_name} {masked_number}"


def get_date(date_of_operation: str) -> str:
    """Функция, которая возвращает строку с датой в формате ДД.ММ.ГГГГ."""
    return f"{date_of_operation[8:10]}.{date_of_operation[5:7]}.{date_of_operation[:4]}"
