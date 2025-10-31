# 한줄 for문

# 출석 번호 앞에 100을 붙이기로 함 -> 101,102,103 ...
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생들 이름을 길이로 변환
student_name = ['Alice','Jane','Sunny']
print(student_name)
student_name = [len(i) for i in student_name]
print(student_name)

# 학생 이름을 대문자로
student_name = ['Alice','Jane','Sunny']
print(student_name)
student_name = [i.upper() for i in student_name]
print(student_name)