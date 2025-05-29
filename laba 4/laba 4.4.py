from datetime import datetime
date_string = input("Enter the date: ")
def dates(date_string):
    date = datetime.strptime(date_string, "%d.%m.%Y")
    week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    month = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
    day_week = week[date.weekday()]
    day_num = date.day
    name_month = month[date.month - 1]
    year = date.year
    full_date = f"{day_week}, {day_num} {name_month}, {year} год"
    return full_date
print(dates(date_string))


