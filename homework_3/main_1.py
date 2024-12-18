# main.py

from my_package.sum_calculator import SumCalculator

def main():
    numbers = [1, 2, 3, 4, 5]  # Пример списка чисел
    try:
        total = SumCalculator.calculate_sum(numbers)
        print(f"Сумма чисел в списке: {total}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
