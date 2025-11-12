# 다중 상속
# 여러 부모 클래스를 동시에 상속

class Flyer:
    def fly(self):
        print("하늘을 날아요!")

class Swimmer:
    def swim(self):
        print("물에서 헤엄쳐요!")

class Walker:
    def walk(self):
        print("땅 위를 걸어요!")

# 다중 상속
class Duck(Flyer, Swimmer, Walker):
    def quack(self):
        print('꽥꽥')

class Penguin(Swimmer, Walker):  # 날지는 못함
    def slide(self):
        print("배로 미끄러져요!")


duck = Duck()
duck.fly()
duck.swim()
duck.walk()
duck.quack()

penguin = Penguin()
penguin.swim() 
penguin.walk() 
penguin.slide() 