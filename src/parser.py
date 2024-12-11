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

