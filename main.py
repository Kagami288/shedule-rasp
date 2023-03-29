import random
import pandas as pd

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
classes = ['1 класс','2 класс','3 класс','4 класс',]

schedule = {}
for day in days:
    schedule[day] = {}
    for c in classes:
        schedule[day][c] = []

for day in days:
    for c in classes:
        for i in range(4):
            if len(schedule[day][c]) >= 4:
                break
            subject = random.choice(['Математика', 'Русский язык', 'Литература', 'Иностранный язык', 'Физкультура', 'Музыка', 'Изобразительное искусство', 'Технология'])
            schedule[day][c].append(subject)



df = pd.DataFrame(schedule)
df.to_excel('output.xlsx')