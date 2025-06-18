numbers = [3, 7, 1, 5, 6, 4, 8, 9, 2]
def ar_num(numbers):
    min_indx = numbers.index(min(numbers))
    max_indx = numbers.index(max(numbers))
    num = numbers[min_indx:max_indx + 1]
    print(num)
    sum_num = sum(num)
    print(f"Сумма: {sum_num}")
    mult_num = 1
    for nums in num:
        mult_num *= nums
    print(f"Произведение: {mult_num}")
ar_num(numbers)