from datetime import datetime
today = datetime.today()
day = today.strftime("%A")
month = today.strftime("%B")
user_name = input("Введите имя: ")
print(f"{day}\n{month}\n{user_name}")