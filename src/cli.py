import argparse
from parser import parse_toml
from converter import convert_to_custom_format

def main():
    parser = argparse.ArgumentParser(description="Конвертер TOML в учебный конфигурационный язык")
    parser.add_argument('output_file', type=str, help="Путь к выходному файлу")
    args = parser.parse_args()

    # Чтение данных TOML с ввода
    print("Введите данные TOML (пустая строка завершает ввод):")
    
    input_text = ""
    while True:
        line = input()
        if line == "":  # Пустая строка завершает ввод
            break
        input_text += line + "\n"
    
    try:
        # Парсинг TOML
        toml_data = parse_toml(input_text)
        
        # Преобразование в формат учебного конфигурационного языка
        converted_data = convert_to_custom_format(toml_data)
        
        # Запись результата в файл
        with open(args.output_file, 'w') as f:
            f.write(converted_data)
        print(f"Конфигурация успешно преобразована и записана в {args.output_file}")
    
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
