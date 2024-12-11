from typing import Any, Dict, List

def process_value(value: Any) -> str:
    """
    Преобразует значение в строковое представление учебного конфигурационного языка.
    """
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        return f"[{', '.join(map(process_value, value))}]"
    elif isinstance(value, dict):
        return f"dict(\n{',\n'.join([f'{k} = {process_value(v)}' for k, v in value.items()])}\n)"
    return str(value)

def process_key_value(key: str, value: Any) -> str:
    """
    Форматирует ключ и значение в формате учебного конфигурационного языка.
    """
    return f"{key} = {process_value(value)}"

def convert_to_custom_format(toml_data: Dict[str, Any]) -> str:
    """
    Конвертирует данные из TOML в формат учебного конфигурационного языка.
    """
    output = []
    for key, value in toml_data.items():
        output.append(process_key_value(key, value))
    return "\n".join(output)
