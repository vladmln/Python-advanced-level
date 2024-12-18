# my_package/sum_calculator.py

class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("Все элементы списка должны быть числами.")
        return sum(numbers)
