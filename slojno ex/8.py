array = [2, 7, 11, 15, 3]
target = 5
for i in range(len(array)):
    first_num = array[i]
    for j in range(i + 1, len(array)):
        second_num = array[j]
        if first_num + second_num == target:
            print(first_num)
            print(second_num)