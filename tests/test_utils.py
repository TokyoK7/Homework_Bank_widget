import pytest
import json
import tempfile
import os
from src.utils import load_transactions


def test_load_transactions_valid_file():
    """Тест загрузки корректного JSON-файла"""
    # Создаем временный файл с данными
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        data = [
            {"id": 1, "state": "EXECUTED", "operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}},
            {"id": 2, "state": "CANCELED", "operationAmount": {"amount": "50.0", "currency": {"code": "USD"}}}
        ]
        json.dump(data, f)
        file_path = f.name

    try:
        result = load_transactions(file_path)
        assert len(result) == 2
        assert result[0]["id"] == 1
    finally:
        os.unlink(file_path)


def test_load_transactions_file_not_found():
    """Тест обработки отсутствующего файла"""
    result = load_transactions("non_existent_file.json")
    assert result == []


def test_load_transactions_empty_file():
    """Тест обработки пустого файла"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        file_path = f.name

    try:
        result = load_transactions(file_path)
        assert result == []
    finally:
        os.unlink(file_path)


def test_load_transactions_not_list():
    """Тест обработки файла, где данные не список"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump({"key": "value"}, f)
        file_path = f.name

    try:
        result = load_transactions(file_path)
        assert result == []
    finally:
        os.unlink(file_path)
