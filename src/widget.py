from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Функция маскировки карты или счета"""
    if len(user_card) <= 0:
        raise ValueError("Ошибка ввода! Пожалуйста введите корректный номер карты или счета.")
    elif "Счет" in user_card:
        mask_acc_numb = f"{user_card[:4]} {get_mask_account(user_card[5:])}"
        return mask_acc_numb
    else:
        mask_card_numb = f"{user_card[:-16]}{get_mask_card_number(user_card[-16:])}"
        return mask_card_numb


    def get_date(date_of_operation: str) -> str:
        """Функция, которая возвращает строку в датой в формате ДД.ММ.ГГГГ"""

        return date_of_operation[8:10] + "." + date_of_operation[5:7] + "." + date_of_operation[0:4]


    print(get_date("2024-03-11T02:26:18.671407"))
