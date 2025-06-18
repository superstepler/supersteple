array = [1,-2,3,6,3,8,-9]
plus = 1
minus = 0
for i in array:
    if i > 0:
        if plus == 1:
            plus = i
    if i < 0:
        minus = i
print(f"Положительный: {plus}")
print(f"Отрицательный: {minus}")