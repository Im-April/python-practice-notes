# 기본 상속

# 부모 클래스
class Animal :
    def __init__(self, name) :
        self.name = name

    def speak(self) :
        print(f'{self.name}가 소리를 냅니다.')

    def move(self):
        print(f'{self.name}가 움직입니다.')

# 자식 클래스
class Dog(Animal): # Animal을 상속받음
    def speak(self): # 메서드 오버라이딩
        print(f'{self.name}가 멍멍!')

    def fetch(self): # 새로운 메서드 추가
        print(f'{self.name}가 공을 물어옵니다.')

class Cat(Animal):
    def speak(self):
        print(f'{self.name}가 야옹!')
    
    def climb(self):
        print(f'{self.name}가 나무를 탑니다.')

# 사용하기
dog = Dog("바둑이")
dog.speak()  # 바둑이가 멍멍! (오버라이딩된 메서드)
dog.move()   # 바둑이가 움직입니다 (부모에게서 상속받음)
dog.fetch()  # 바둑이가 공을 물어옵니다 (Dog만의 메서드)

cat = Cat("나비")
cat.speak()  # 나비가 야옹~
cat.move()   # 나비가 움직입니다
cat.climb()  # 나비가 나무를 탑니다