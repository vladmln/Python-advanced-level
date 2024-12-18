from datetime import datetime, timedelta

def display_current_datetime():
    # Отображение текущей даты и времени
    now = datetime.now()
    print("Текущая дата и время:", now)

def calculate_date_difference(date1, date2):
    # Вычисление разницы между двумя датами
    delta = date2 - date1
    print(f"Разница между датами: {delta.days} дней")

def convert_string_to_datetime(date_string, date_format):
    # Преобразование строки в объект даты и времени
    try:
        date_object = datetime.strptime(date_string, date_format)
        print("Преобразованная дата и время:", date_object)
        return date_object
    except ValueError as e:
        print("Ошибка преобразования:", e)

def main():
    # Задача 1: Отображение текущей даты и времени
    display_current_datetime()

    # Задача 2: Вычисление разницы между двумя датами
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 12, 31)
    calculate_date_difference(date1, date2)

    # Задача 3: Преобразование строки в объект даты и времени
    date_string = "2023-10-15 14:30"
    date_format = "%Y-%m-%d %H:%M"
    convert_string_to_datetime(date_string, date_format)

if __name__ == "__main__":
    main()
