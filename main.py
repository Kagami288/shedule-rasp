import json
import random
import copy

with open('subjects.json') as f:
    subjects = json.load(f)
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


it = 0
check = False
while check == False:
    it = it + 1
    print("Итерация: ", it)
    for day in week:
        num = random.randint(4,5)
        if day != 'Понедельник':
            if len(week[day-1])==5:
                num = 4
        for i in range(num):
            for key in subjects:
                if subjects[key].get('hours')==len(week):
                    week[day].append(subjects[key]['name'])
                    subjects[key]['hours'] = subjects[key].get('hours') - 1
                    break
        local_check = False
        while local_check == False:
            rand_sub = random.choice(subjects)
            if rand_sub['hours'] != 0:
                week[day].append(rand_sub['name'])
                subjects[rand_sub]['hours'] = subjects[rand_sub].get('hours') - 1
                local_check = True
    sum_rang = 0
    for day in week:
        for num in day:
            for sub in subjects:
                if num == sub['name']:
                    sum_rang = sum_rang + sub['hours']
    week_rang[day] = sum_rang
    sum_rang = 0
    if week_rang['Понедельник'] and week_rang['Пятница'] < week_rang['Вторник'] < week_rang['Среда'] and week_rang['Четверг']:
        print("Расписание готово")
        check = True
    else:
        check = False
        week = copy.deepcopy(week_o)
        week_rang = copy.deepcopy(week)
for day in week:
    print(day)