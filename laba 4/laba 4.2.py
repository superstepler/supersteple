array = [int(input("Enter number: ")) for num in range(14)]
array.append(sum(array))
for num in array:
    print(num)