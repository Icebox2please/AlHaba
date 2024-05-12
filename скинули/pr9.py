# class Student:
#     def student1(self):
#         name ='Камиль'
#         course= 'Третий курс'
#         weight = 'Ящик пива корона светлая'
#         college = 'КФУ'
#         print(f'{name}\n {course}\n {weight}\n {college}\n')

#     def student2(self):
#         name ='Оля'
#         course= 'Четвертый'
#         weight = '49'
#         college = 'Да'
#         print(f'{name}\n {course}\n {weight}\n {college}\n')

#     def stident3(self):
#         name ='Олег'
#         course= 'Первый'
#         weight = '57'
#         college = 'КФУ'
#         print(f'{name}\n {course}\n {weight}\n {college}\n')
    
#     def student4(self):
#         name ='Виталий'
#         course= 'Выпустился'
#         weight = '1 тонна'
#         college = 'Традиционный универсисет по поглощению пива и чипсов'
#         print(f'{name}\n {course}\n {weight}\n {college}\n')

# real_nigger = Student()
# real_nigger.student2()

class Student:
    def __init__(self, name, age, college, group):
        self.name = name
        self.age = age
        self.college = college
        self.group = group

def print_student_info(student):
    print(f"Имя: {student.name}")
    print(f"Возраст: {student.age}")
    print(f"Колледж: {student.college}")
    print(f"Группа: {student.group}")
    print()

student_1 = Student("Олег", 25, "КФУ", '228')
student_2 = Student("Аня", 21, "Узбекский университест имени Махача Кала", "141-983")
student_3 = Student("Пивандепало", 23, "Красное&Белое", "Нет" )

print("Информация о студенте:")
print_student_info(student_3)

