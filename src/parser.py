import toml
from typing import Any, Dict

def parse_toml(input_text: str) -> Dict[str, Any]:
    """
    Парсит строку в формате TOML и возвращает Python-структуру (словарь).
    В случае ошибки синтаксиса генерирует исключение.
    """
    try:
        return toml.loads(input_text)
    except toml.TomlDecodeError as e:
        raise ValueError(f"Ошибка синтаксиса в TOML: {e}")


def resolve_constants(data: Dict[str, Any], constants: Dict[str, str]) -> Dict[str, Any]:
    """
    Рекурсивно заменяет ссылки на константы в структуре данных.
    """
    if isinstance(data, dict):
        return {k: resolve_constants(v, constants) for k, v in data.items()}
    elif isinstance(data, list):
        return [resolve_constants(item, constants) for item in data]
    elif isinstance(data, str):
        for const_name, const_value in constants.items():
            data = data.replace(f"${const_name}$", const_value)
        return data
    return data
