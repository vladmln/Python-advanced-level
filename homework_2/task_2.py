class DataBuffer:
    def __init__(self):
        self.buffer = []  # Инициализируем пустой список для хранения данных

    def add_data(self, data):
        self.buffer.append(data)  # Добавляем данные в буфер
        print(f"Добавлено: {data}. Текущее состояние буфера: {self.buffer}")  # Выводим текущее состояние буфера
        if len(self.buffer) >= 5:  # Проверяем, если в буфере 5 или более элементов
            print("Переполнение буфера! Очищаем буфер.")
            self.clear_buffer()  # Очищаем буфер
            print("Буфер очищен. Текущее состояние буфера: []")  # Выводим состояние буфера после очистки

    def get_data(self):
        if not self.buffer:  # Проверяем, пуст ли буфер
            print("Буфер пуст. Нет данных для получения.")
            return None
        print("Данные в буфере:", self.buffer)  # Выводим данные из буфера
        return self.buffer  # Возвращаем данные из буфера

    def clear_buffer(self):
        self.buffer.clear()  # Очищаем буфер

# Пример использования класса
buffer = DataBuffer()

# Добавляем данные в буфер
buffer.add_data(1)
buffer.add_data(2)
buffer.add_data(3)
buffer.add_data(4)
buffer.add_data(5)  # Здесь произойдет переполнение буфера

# Получаем данные из буфера
data = buffer.get_data()  # Здесь буфер будет пуст, так как он был очищен
if data is not None:
    print("Полученные данные:", data)

# Добавляем еще данные в буфер
buffer.add_data(6)
buffer.add_data(7)
data = buffer.get_data()
if data is not None:
    print("Полученные данные:", data)
