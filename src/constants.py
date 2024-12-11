# Константы и вычисления для учебного конфигурационного языка

# Пример хранения значений констант
constants = {}

def declare_constant(name: str, value: str) -> None:
    """
    Объявляет константу на этапе трансляции.
    """
    constants[name] = value

def calculate_constant(expression: str) -> str:
    """
    Вычисляет значение константы, если она была ранее объявлена.
    Использует символ $имя$ для подстановки значений.
    """
    # Заменяем все вхождения $имя$ на фактическое значение из constants
    for name, value in constants.items():
        expression = expression.replace(f"${name}$", value)
    return expression
