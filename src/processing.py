from typing import Any, List, Dict


def filter_by_state(data: List[Dict[str, Any]], state: str) -> List[Dict[str, Any]]:
    """Функция, которая фильтрует список словарей по указанному ключу"""
    sorted_list: List[Dict[str, Any]] = []
    for item in data:
        if item.get("state", "") == state:
            sorted_list.append(item)
    return sorted_list


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки списка банковских операций по дате (по умолчанию - убывание)"""
    sorted_list: List[Dict[str, Any]] = sorted(data, key=lambda x: x["date"], reverse=descending)
    return sorted_list
