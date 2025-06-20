array = [1,2,3,4,5,6,7,8]
num_1 = 0
num_2 = 0
for i in array:
    if i % 2 == 0:
        num_1 += 1
    elif i % 2 != 0:
        num_2 += 1
print(num_1)
print(num_2)

