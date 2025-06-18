class Task:
    def __init__(self,datestart, datefinish,description):
        self.datestart = datestart
        self.datefinish = datefinish
        self.description = description

task = [Task("2020-01-01","2020-12-31", "class_1"), Task("2021-01-01","2021-12-31", "class_2"),Task("2022-01-01","2022-12-31", "class_3"),
        Task("2023-01-01","2023-12-31", "class_4"), Task("2024-01-01","2024-12-31", "class_5")]

last_task = task[0]
for t in task:
    if t.datefinish > last_task.datefinish:
        last_task = t
print(f"Начало: {last_task.datestart}, Конец: {last_task.datefinish}, Описание: {last_task.description}")

