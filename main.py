import json
import random
import copy

with open('subjects.json') as f:
    subjects_o = json.load(f)
week_o = {
    'Понедельник': [],
    'Вторник': [],
    'Среда': [],
    'Четверг': [],
    'Пятница': []
}

def name_rang(sub):
    list_N = []
    list_N.append(sub.get('name'))
    list_N.append(sub.get('rang'))
    return list_N
week = copy.deepcopy(week_o)
week_rang = copy.deepcopy(week)

# week['Понедельник'] = ["Рус","Мат"]
# week_rang['Понедельник'] = [1,2]
# for day in week:
#     print(week_rang[day])

# week['Понедельник'].extend(name_rang(subjects['1']))
# print(week['Понедельник'])

# week['Понедельник'].append(subjects['1'].get('name'))
# week['Понедельник'].append(subjects['1'].get('rang'))
# print(week['Понедельник'])
# print(week['Понедельник'][0])

# for key in subjects:
#     print (subjects[key].get('name'), ' Часы: ', subjects[key].get('hours'))

# for day in week:
#     num = random.randint(4,5)
#     if len(week[day-1])==5:
#         num = 4
#     for i in num:
#         for key in subjects:
#             if subjects[key].get('hours')==len(week):
#                 day.append(subjects[key]['name'])
#                 subjects[key]['hours'] = subjects[key].get('hours') - 1
#                 continue
#         rand_sub = random.choice(subjects)
#         if subjects['hours'] != 0:
#             day.append(subjects[key]['name'])
#             subjects[key]['hours'] = subjects[key].get('hours') - 1
#             continue
# sum_rang = 0
# for day in week:
#     for num in day:
#  f week_rang['Понедельник'] and week_rang['Пятница'] < week_rang['Вторник'] < week_rang['Среда'] and week_rang['Четверг']:
#     check = True
# else:
#     check = False
#     week = copy.deepcopy(week_o)
#     week_rang = copy.deepcopy(week)
#        for sub in subjects:
#             if num == sub['name']:
#                 sum_rang = sum_rang + sub['hours']
#     week_rang[day] = sum_rang
#     sum_rang = 0

def check_study(week):
    for day in week:
        if len(day) == 5:
            return False
    return True

# a=0
# for sub in subjects_o:
#     a = a + subjects_o[sub]['hours']
# print(a)

it = 0
check = False
while check == False:
    subjects = copy.deepcopy(subjects_o)
    it = it + 1
    print("Итерация: ", it)
    for day in week:
        num = random.randint(5,6)
        if check_study(week):
            num = 5
        for i in range(num):
            for key in subjects:
                if subjects[key].get('hours')==len(week):
                    week[day].append(subjects[key]['name'])
                    subjects[key]['hours'] = subjects[key].get('hours') - 1
                    break
                local_check = False
                if i == len(week[day]):
                    break
                while local_check == False:
                    if i == len(week[day]):
                        break
                    rand_sub = random.choice(list(subjects.keys()))
                    if subjects[rand_sub]['hours'] != 0:
                        week[day].append(subjects[rand_sub]['name'])
                        subjects[rand_sub]['hours'] = subjects[rand_sub].get('hours') - 1
                        local_check = True
                        break
    sum_rang = 0
    for day in week:
        sum_rang = 0
        for num in week[day]:
            for sub in subjects:
                if num == subjects[sub]['name']:
                    sum_rang = sum_rang + subjects[sub]['rang']
                    week_rang[day] = sum_rang
    if week_rang['Понедельник'] and week_rang['Пятница'] < week_rang['Вторник'] < week_rang['Среда'] and week_rang['Четверг']:
        print("Расписание готово")
        check = True
    else:
        check = False
        week = copy.deepcopy(week_o)
        week_rang = copy.deepcopy(week)

for day in week:
    print(day + ":")
    for num in week[day]:
        print(" - " + num)