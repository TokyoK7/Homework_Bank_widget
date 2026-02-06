import pytest
from unittest.mock import patch, Mock
import os
from src.external_api import convert_amount_to_rub


def test_convert_amount_to_rub_rub():
    """Тест конвертации для транзакции в рублях"""
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 100.50


@patch.dict(os.environ, {"EXCHANGE_RATE_API_KEY": "test_key"})
@patch('src.external_api.requests.get')
def test_convert_amount_to_rub_usd(mock_get):
    """Тест конвертации для транзакции в USD"""
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "rates": {"RUB": 75.5}
    }
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 100.0 * 75.5
    mock_get.assert_called_once()


@patch.dict(os.environ, {"EXCHANGE_RATE_API_KEY": "test_key"})
@patch('src.external_api.requests.get')
def test_convert_amount_to_rub_eur(mock_get):
    """Тест конвертации для транзакции в EUR"""
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "rates": {"RUB": 85.0}
    }
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {"code": "EUR"}
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 50.0 * 85.0
    mock_get.assert_called_once()


def test_convert_amount_to_rub_invalid_structure():
    """Тест обработки транзакции с некорректной структурой"""
    transaction = {"invalid": "structure"}

    with pytest.raises(ValueError):
        convert_amount_to_rub(transaction)


def test_convert_amount_to_rub_missing_api_key():
    """Тест обработки отсутствия API ключа"""
    # Удаляем переменную окружения
    if "EXCHANGE_RATE_API_KEY" in os.environ:
        del os.environ["EXCHANGE_RATE_API_KEY"]

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    with pytest.raises(ValueError, match="API ключ не найден"):
        convert_amount_to_rub(transaction)
