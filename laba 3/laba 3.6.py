import random
array = [random.randint(-100, 100) for num in range(20)]
def number(array):
    multi = 1
    for num in range(len(array)):
        if num % 2 != 0:
            multi *= array[num]
    return multi
print(array)
print(f"Произведение чисел: {number(array)}")