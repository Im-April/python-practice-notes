# 간단한 클래스 만들기

class Dog:
    def __init__(self,name,age): # 객체가 만들어질 때 자동으로 실행되는 초기화 함수
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name}가 멍멍!')


# 클래스로 객체 만들기
my_dog = Dog('마루',2)
your_dog = Dog('뽀삐',5)

my_dog.bark()
your_dog.bark()