import argparse
from parser import parse_toml, resolve_constants
from converter import convert_to_custom_format

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Конвертер TOML в учебный конфигурационный язык")
    parser.add_argument('output_file', type=str, help="Путь к выходному файлу")
    args = parser.parse_args()

    print("Введите данные TOML (пустая строка завершает ввод):")
    input_text = ""
    while True:
        line = input()
        if line == "":
            break
        input_text += line + "\n"
    
    try:
        # Парсинг TOML
        toml_data = parse_toml(input_text)

        # Выделение констант
        constants = toml_data.pop("constants", {})
        
        # Замена констант в данных
        resolved_data = resolve_constants(toml_data, constants)
        
        # Преобразование в кастомный формат
        converted_data = convert_to_custom_format(resolved_data)

        # Запись результата в файл
        with open(args.output_file, 'w') as f:
            f.write(converted_data)
        print(f"Конфигурация успешно преобразована и записана в {args.output_file}")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
