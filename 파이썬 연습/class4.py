# super 사용

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. {self.age}살 입니다.')

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age) # 부모의 __init__ 호출
        self.school = school

    def introduce(self):
        super().introduce() # 부모의 introduce 먼저 호출
        print(f'{self.school}에 다니고 있어요')

student = Student("김철수", 15, "OO중학교")
student.introduce()