#Вам нужно создать класс Diary (Электронный дневник), который поможет
#ученику хранить свои оценки по разным предметам.
#методы:
#add_grade(self, subject, grade) – добавляет оценку по предмету (оценки от 2 до
#5)
#get_average(self, subject) – возвращает средний балл по предмету
#get_all_average(self) – возвращает средний балл по всем предметам
#get_bad_subjects(self) – возвращает список предметов, где средний балл ниже
#3.5
#reset_diary(self) – очищает весь дневник


class Diary:
    def __init__(self):
        self.__grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.__grades:
            self.__grades[subject] = []
        self.__grades[subject].append(grade)
        print(f"Добавлена оценка {grade} по предмету '{subject}'")

    def get_average(self, subject):
        grades = self.__grades[subject]
        return sum(grades) / len(grades)

    def get_all_average(self):
        all_grades = []
        for grades_list in self.__grades.values():
            all_grades.extend(grades_list)
        
        return sum(all_grades) / len(all_grades)

    def get_bad_subjects(self):
        bad_subjects = []
        for subject in self.__grades:
            avg = self.get_average(subject)
            if avg < 3.5:
                bad_subjects.append(subject)
        return bad_subjects

    def reset_diary(self):
        self.__grades.clear()
        print("Дневник очищен")

my_diary = Diary()
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Химия", 2)
my_diary.add_grade("Химия", 3)
print(my_diary.get_average("Биология"))
print(my_diary.get_average("Химия"))
print(my_diary.get_all_average())
print(my_diary.get_bad_subjects())
my_diary.reset_diary()