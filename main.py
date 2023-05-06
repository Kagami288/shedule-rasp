import json
import random

with open('subjects.json') as f:
    subjects = json.load(f)
schedule = {
    'Понедельник': [],
    'Вторник': [],
    'Среда': [],
    'Четверг': [],
    'Пятница': []
}
print()