def read_numbers_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()
        
        for line in data:
            line = line.strip()  # Убираем пробелы и символы новой строки
            try:
                # Пробуем преобразовать строку в число
                number = float(line.replace(',', '.'))  # Заменяем запятую на точку для корректного преобразования
                print(number)
            except ValueError:
                # Если не удалось преобразовать строку в число, просто игнорируем её
                print(f"Строка '{line}' не является числом и будет проигнорирована.")
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

# Пример использования функции
read_numbers_from_file('homework_2/data.txt')
