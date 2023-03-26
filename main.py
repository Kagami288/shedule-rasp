import json
import random

# Список предметов
subjects = {
    "7": {
        "name": "Литература",
        "rang": 5,
        "hours": 4,
        "isLetter": True
    },
    "8": {
        "name": "История",
        "rang": 4,
        "hours": 1,
        "isLetter": True
    },
    "9": {
        "name": "Рисование",
        "rang": 3,
        "hours": 1,
        "isLetter": True
    },
    "10": {
        "name": "Музыка",
        "rang": 3,
        "hours": 1,
        "isLetter": False
    },
    "11": {
        "name": "Труд",
        "rang": 2,
        "hours": 1,
        "isLetter": False
    }
}

# Определяем дни недели
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']

# Инициализируем расписание
schedule = {
    'Понедельник': [],
    'Вторник': [],
    'Среда': [],
    'Четверг': [],
    'Пятница': []
}

# Выбираем легкие дни
easy_days = ['Понедельник', 'Пятница']

# Выбираем сложные дни
hard_days = ['Среда', 'Четверг']

# Создаем список предметов для устных и письменных занятий
letter_subjects = []
non_letter_subjects = []

# Заполняем списки предметов для устных и письменных занятий
for key, subject in subjects.items():
    if subject['isLetter']:
        letter_subjects.append(int(key))
    else:
        non_letter_subjects.append(int(key))

# Формируем расписание на каждый день недели
for day in days:
    # Считаем, сколько часов свободно на этот день
    free_hours = 5

    # Если сегодня легкий день, то количество часов уменьшаем на 1
    if day in easy_days:
        free_hours -= 1

    # Если сегодня сложный день, то количество часов увеличиваем на 1
    if day in hard_days:
        free_hours += 1

    # Выбираем первый предмет
first_subject = random.choice(list(subjects.keys()))

# Создаем словарь с количеством часов для каждого дня
hours_per_day = {day: 0 for day in range(1, 6)}

# Создаем список для каждого дня недели
schedule = {day: [] for day in range(1, 6)}

# Определяем максимальное количество часов для всех дней
max_hours = 21

# Определяем максимальное количество предметов для одного дня
max_subjects_per_day = 5

# Определяем минимальное количество предметов на один день
min_subjects_per_day = 3

# Создаем список с номерами устных предметов
oral_subjects = [int(key) for key, val in subjects.items() if not val["isLetter"]]

# Создаем список с номерами письменных предметов
letter_subjects = [int(key) for key, val in subjects.items() if val["isLetter"]]

# Первый предмет должен быть письменным
while int(first_subject) in oral_subjects:
    first_subject = random.choice(list(subjects.keys()))

# Добавляем первый предмет в расписание
schedule[1].append(first_subject)
hours_per_day[1] += subjects[first_subject]["hours"]

# Добавляем остальные предметы
for day in range(1, 6):
    while hours_per_day[day] < min_subjects_per_day or len(schedule[day]) < min_subjects_per_day:
        # Выбираем предмет для добавления
        if hours_per_day[day] >= max_hours or len(schedule[day]) >= max_subjects_per_day:
            break
        subject = random.choice(list(set(subjects.keys()) - set(schedule[day])))
        # Учитываем ранг предмета
        if subjects[subject]["rang"] == 8:
            # Добавляем сложный предмет в середину недели
            if day in [3, 4]:
                if hours_per_day[day] + subjects[subject]["hours"] <= max_hours and len(schedule[day]) < max_subjects_per_day:
                    schedule[day].append(subject)
                    hours_per_day[day] += subjects[subject]["hours"]
            # Добавляем сложный предмет в начало или конец недели
            else:
                if hours_per_day[day] + subjects[subject]["hours"] <= max_hours and len(schedule[day]) < max_subjects_per_day:
                    if day == 1 or day == 5:
                        schedule[day].append(subject)
                        hours_per_day[day] += subjects[subject]["hours"]
                    else:
                        # Добавляем сложный предмет в следующий день, если это возможно
                            next_day = day + 1
                            if hours_per_day[next_day] + subjects[subject]["hours"] <= max_hours and len(schedule[next_day]) < max_subjects_per_day:
                                schedule[next_day].append(subject)
                                hours_per_day[next_day] += subjects[subject]["hours"]
                                if subjects[subject]["isLetter"]:
                                    letter_subjects.remove(subject)
                                    if len(letter_subjects) == 0:
                                        break