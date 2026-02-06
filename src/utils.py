import json
import os
from typing import List, Dict, Any


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу с транзакциями

    Returns:
        Список словарей с данными транзакций или пустой список в случае ошибки
    """
    try:
        # Проверяем существование файла
        if not os.path.exists(file_path):
            return []

        # Проверяем, что файл не пустой
        if os.path.getsize(file_path) == 0:
            return []

        # Открываем и читаем файл
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверяем, что данные - это список
        if not isinstance(data, list):
            return []

        return data

    except FileNotFoundError:
        # Файл не найден
        return []
    except json.JSONDecodeError:
        # Ошибка декодирования JSON
        return []
    except Exception:
        # Любая другая ошибка
        return []
