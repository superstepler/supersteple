string = str(input("Введите строку: "))
if string.startswith("abc"):
    string = "www" + string[3:]
else:
  string = string + "zzz"
print(string)


