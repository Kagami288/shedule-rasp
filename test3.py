import random
from typing import List, Tuple
import json
with open('subjects.json') as f:
    subjects = json.load(f)
def create_schedule() -> List[List[None]]:
    schedule = []
    for day in range(5):
        day_schedule = [None] * 7
        schedule.append(day_schedule)
    return schedule

def get_subjects() -> List[str]:
    with open('subjects.json') as f:
        subjects = json.load(f)
    return list(subjects.keys())

def is_valid_hours(schedule: List[List[str]]) -> bool:
    total_hours = sum([subjects[subject]['hours'] for day in schedule for subject in day if subject])
    return total_hours <= 21

def is_valid_vokal(schedule: List[List[str]]) -> bool:
    oral_subjects = [subject for day in schedule for subject in day if subject and subjects[subject]['isLetter']]
    return not oral_subjects or oral_subjects[-1] in schedule[4]

def is_valid_subjects_per_day(schedule: List[List[str]]) -> bool:
    subjects_per_day = [len([subject for subject in day if subject]) for day in schedule]
    return 3 <= min(subjects_per_day) <= max(subjects_per_day) <= 4

def get_rank_score(schedule: List[List[str]]) -> int:
    score = sum([subjects[s]['rang'] for s in get_subjects() for day in schedule for subject in day if subject == s])
    return score

def check_valid_rasp(schedule: List[List[str]]) -> int:
    if not is_valid_hours(schedule):
        return -1
    if not is_valid_vokal(schedule):
        return -1
    if not is_valid_subjects_per_day(schedule):
        return -1
    return get_rank_score(schedule)

def generate_generated_rasp(size: int) -> List[List[List[str]]]:
    generated_rasp = []
    subjects = get_subjects()
    for i in range(size):
        schedule = create_schedule()
        for subject in subjects:
            day = random.randint(0, 4)
            hour = random.randint(0, 6)
            while schedule[day][hour] is not None:
                day = random.randint(0, 4)
                hour = random.randint(0, 6)
            schedule[day][hour] = subject
        generated_rasp.append(schedule)
    return generated_rasp

def select_parents(generated_rasp: List[List[List[str]]]) -> Tuple[List[List[str]], List[List[str]]]:
    check_valid_raspes = [check_valid_rasp(schedule) for schedule in generated_rasp]
    max_check_valid_rasp = max(check_valid_raspes)
    weights = [check_valid_rasp / max_check_valid_rasp for check_valid_rasp in check_valid_raspes]
    parent1 = random.choices(generated_rasp, weights=weights)[0]
    parent2 = random.choices(generated_rasp, weights=weights)[0]
    return parent1, parent2

def crossover(parent1: List[List[str]], parent2: List[List[str]]) -> List[List[str]]:
    child = create_schedule()
    for day in range(5):
        for hour in range(7):
            if parent1[day][hour] == parent2[day][hour]:
                child[day][hour] = parent1[day][hour]
            else:
                subject = random.choice([parent1[day][hour], parent2[day][hour]])
                child[day][hour] = subject
    return child

def generateRasp(schedule: List[List[str]]) -> List[List[str]]:
    subject = random.choice(get_subjects())
    day = random.randint(0, 4)
    hour = random.randint(0, 6)
    while schedule[day][hour] is not None:
        day = random.randint(0, 4)
        hour = random.randint(0, 6)
    schedule[day][hour] = subject
    return schedule

def print_schedule(schedule):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    for i, day_schedule in enumerate(schedule):
        print(days[i])
        for hour in day_schedule:
            if hour is None:
                continue
            else:
                print(subjects[hour]['name'])
        print()
generated_rasp = generate_generated_rasp(10)

print_schedule(generated_rasp[0])
