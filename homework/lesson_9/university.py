from student import Student


students = [
    Student('Ray Scott', 6.2),
    Student('Cynthia Williams', 8.5),
    Student('Thomas Collins', 3.7),
    Student('Emily Coleman', 7.5),
    Student('Kelly Morris', 9.4),
    Student('Leonard Austin', 9.0),
    Student('Brian Hunter', 6.0),
    Student('Jennifer Murphy', 7.9),
    Student('Russell Parks', 5.8)
]


def calc_sum_scholarship(student_list):
    return sum([student.get_scholarship() for student in student_list])


def get_excellent_student_count(student_list):
    return len([student for student in student_list if student.is_excellent()])


total_scholarship = calc_sum_scholarship(students)
print(f'Total scholarship is: {total_scholarship}')

excellent_student_count = get_excellent_student_count(students)
print(f'Number of excellent students is: {excellent_student_count}')
