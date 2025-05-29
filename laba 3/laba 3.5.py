import random
array = [random.randint(-100, 100) for num in range(20)]
def positive_number(array):
    number = 0
    for num in array:
        if num > 0:
            number += 1
    return number
print(array)
print(f"Положительные числа: {positive_number(array)}")