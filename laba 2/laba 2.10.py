array = []
while True:
    words = input("Введите элементы: ")
    if words == "":
        break
    else:
        array.append(words)
long = max(array, key=len)
short = min(array, key=len)
print(f"Самый длинный: {long}\nСамый короткий: {short}")