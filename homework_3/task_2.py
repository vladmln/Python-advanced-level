import re
from collections import Counter

def count_unique_words(input_string):
    # Удаляем знаки препинания и приводим строку к нижнему регистру
    cleaned_string = re.sub(r'[^\w\s]', '', input_string).lower()
    
    # Разбиваем строку на слова
    words = cleaned_string.split()
    
    # Используем Counter для подсчета уникальных слов
    word_count = Counter(words)
    
    # Выводим количество уникальных слов
    unique_word_count = len(word_count)
    print(f"Количество уникальных слов: {unique_word_count}")

# Пример использования функции
input_string = "Hello world!"
count_unique_words(input_string)
