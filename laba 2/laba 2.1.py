import random
numbers = [random.randint(1, 100) for num in range(10)]
min_value = min(numbers)
min_index = numbers.index(min_value)
print(f"Коллекция: {numbers}")
print(f"Мин. число: {min_value}")
print(f"Индекс мин. числа: {min_index}")