def season_events(number_of_month):
    month = ["Январь", "Февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    if number_of_month in [1, 2, 12]:
        event = "За окном падал белый снег"
    elif number_of_month in [3, 4, 5]:
        event = "Птицы пели прекрасные песни"
    elif number_of_month in [6, 7, 8]:
        event = "Солнце светило ярче, чем когда-либо"
    else:
        event = "Урожай был невероятным"
    return print(f"You were born in {month[number_of_month - 1]}, {event}")

try:
    number_of_month = int(input("enter the month of your birth: "))
except ValueError:
    print("Error")
season_events(number_of_month)


