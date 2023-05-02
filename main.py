import random

class Subject:
    def __init__(self, name, rank, hours, is_written):
        self.name = name
        self.rank = rank
        self.hours = hours
        self.is_written = is_written

class ScheduleGenerator:
    def __init__(self):
        self.days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        self.subjects = [
            Subject("Математика", 8, 5, True),
            Subject("Русский", 7, 4, True),
            Subject("Английский", 7, 1, True),
            Subject("Природоведение", 6, 2, True),
            Subject("Информатика", 6, 1, True),
            Subject("Литература", 5, 4, True),
            Subject("История", 4, 1, True),
            Subject("Рисование", 3, 1, True),
            Subject("Музыка", 3, 1, False),
            Subject("Труд", 2, 1, False),
            Subject("Физическая культура", 1, 3, False)
        ]
        self.written_subjects = [s for s in self.subjects if not s.is_written]
        self.oral_subjects = [s for s in self.subjects if s.is_written]
        self.min_subjects_per_day = 1
        self.max_subjects_per_day = 3
        self.max_hours_per_week = 21

    def generate(self):
        schedule = {day: [] for day in self.days}
        hours_left = self.max_hours_per_week
        subjects_left = self.subjects.copy()
        for day in self.days:
            is_light_day = (day == "Понедельник" or day == "Пятница")
            is_hard_day = (day == "Среда" or day == "Четверг")
            min_subjects = self.min_subjects_per_day if not is_light_day else 2
            max_subjects = self.max_subjects_per_day if not is_hard_day else 4
            num_subjects = random.randint(min_subjects, max_subjects)
            while num_subjects > 0:
                available_subjects = [s for s in subjects_left if s.hours <= hours_left and s not in schedule[day]]
                if not available_subjects:
                    break
                subject = self.choose_subject(available_subjects, is_light_day, is_hard_day)
                schedule[day].append(subject)
                subjects_left.remove(subject)
                hours_left -= subject.hours
                num_subjects -= 1
            if is_light_day and num_subjects == 2:
                written_subject = self.choose_subject(self.written_subjects, is_light_day, is_hard_day)
                schedule[day].append(written_subject)
                subjects_left.remove(written_subject)
                hours_left -= written_subject.hours
                num_subjects -= 1
            if num_subjects == 1 and self.oral_subjects in subjects_left:
                oral_subject = self.choose_subject(self.oral_subjects, is_light_day, is_hard_day)
                schedule[day].append(oral_subject)
                subjects_left.remove(oral_subject)
                hours_left -= oral_subject.hours
        return schedule

    def choose_subject(self, subjects, is_light_day, is_hard_day):
        if len(subjects) == 1:
            return subjects[0]
        if is_hard_day:
            subjects = sorted(subjects, key=lambda s: s.rank, reverse=True)
        elif is_light_day:
            subjects = sorted(subjects, key=lambda s: s.rank)
        return subjects[0]

# пример использования
generator = ScheduleGenerator()
schedule = generator.generate()
for day, subjects in schedule.items():
    print(day + ":")
    for subject in subjects:
        print(" - " + subject.name)
