class fitness:
    def __init__(self, code_user, year, num_month, duration):
        self.code_user = code_user
        self.year = year
        self.num_month = num_month
        self.duration = duration

fitness_cen = [fitness("001", 2022, 1, 13), fitness("002", 2022, 2, 43), fitness("003", 2022, 3, 72),
               fitness("004", 2023, 4, 36), fitness("005", 2023, 5, 94),
               fitness("006", 2023, 6, 57), fitness("007", 2024, 7, 82),
               fitness("008", 2024, 8, 67), fitness("009", 2024, 9, 74),
               fitness("010", 2025, 10, 99)]

year_durations = {}
for i in fitness_cen:
    if i.year in year_durations:
        year_durations[i.year] += i.duration
    else:
        year_durations[i.year] = i.duration
max_duration = 0
max_year = 0
for year, duration in year_durations.items():
    if duration > max_duration:
        max_duration = duration
        max_year = year
print(f"Год с наибольшей суммарной продолжительностью: {max_year}, Продолжительность: {max_duration}")