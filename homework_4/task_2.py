import itertools

def infinite_number_generator(start=0):
    """Создание бесконечного генератора чисел, начиная с указанного значения."""
    for number in itertools.count(start):
        yield number

def apply_function_to_iterator(iterator, func):
    """Применение функции к каждому элементу в итераторе."""
    try:
        for item in iterator:
            yield func(item)
    except StopIteration:
        print("Итератор завершен.")

def combine_iterators(*iterators):
    """Объединение нескольких итераторов в один."""
    return itertools.chain(*iterators)

def main():
    # Задача 1: Создание бесконечного генератора чисел
    print("Бесконечный генератор чисел (первые 10 чисел):")
    number_gen = infinite_number_generator()
    for _ in range(10):
        print(next(number_gen), end=' ')
    print("\n")

    # Задача 2: Применение функции к каждому элементу в итераторе
    print("Применение функции (умножение на 2) к элементам:")
    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = apply_function_to_iterator(numbers, lambda x: x * 2)
    for num in doubled_numbers:
        print(num, end=' ')
    print("\n")

    # Задача 3: Объединение нескольких итераторов в один
    print("Объединение нескольких итераторов:")
    iterator1 = itertools.cycle([1, 2, 3])  # Бесконечный итератор
    iterator2 = itertools.cycle(['A', 'B', 'C'])  # Бесконечный итератор

    combined_iterator = combine_iterators(iterator1, iterator2)

    # Печатаем первые 6 элементов объединенного итератора
    print("Первые 6 элементов объединенного итератора:")
    for _ in range(6):
        print(next(combined_iterator), end=' ')
    print("\n")

if __name__ == "__main__":
    main()
