array = []
array_1 = ["hello", "pixel", "http://.leto"]
for num in range(len(array_1)):
    if array_1[num].startswith("http://."):
        array.append(array_1[num])
print(array)


