import os
from typing import Dict, Any
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()


def convert_amount_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма транзакции в рублях (float)
    """
    try:
        # Получаем сумму и валюту из транзакции
        amount = float(transaction["operationAmount"]["amount"])
        currency_code = transaction["operationAmount"]["currency"]["code"]

        # Если транзакция уже в рублях
        if currency_code == "RUB":
            return amount

        # Если транзакция в USD или EUR - конвертируем
        if currency_code in ["USD", "EUR"]:
            api_key = os.getenv("EXCHANGE_RATE_API_KEY")
            if not api_key:
                raise ValueError("API ключ не найден в переменных окружения")

            # Получаем курс валют
            url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB"
            headers = {"apikey": api_key}

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()
            rate = data["rates"]["RUB"]

            # Конвертируем сумму
            return amount * rate

        # Для других валют возвращаем исходную сумму (или можно вызвать исключение)
        return amount

    except (KeyError, ValueError, TypeError) as e:
        # Обрабатываем ошибки структуры данных или преобразования типов
        raise ValueError(f"Ошибка при обработке транзакции: {str(e)}")
    except requests.exceptions.RequestException as e:
        # Обрабатываем ошибки запроса к API
        raise ConnectionError(f"Ошибка при получении курса валют: {str(e)}")
