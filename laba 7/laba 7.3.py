number = [10, 20, 5, 6, 8, -9, 22, 33, 11]
num = []
for i in number:
    if i > 0 and 10 <= i <= 99:
        num.append(i)
num.sort()
print(number)
print(num)