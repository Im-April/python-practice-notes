# 일반 유닛
class Unit :
    def __init__(self,name,hp, speed): 
        # 멤버 변수 : 클래스 내에서 선언된 변수
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location) :
        print(f'[지상 유닛 이동]')
        print(f'{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]')

# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self,name,hp,speed,damage): 
        # Unit 상속
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location) :
        print(f'{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 : {self.damage}]')

    def damaged(self, damage) :
        print(f'{self.name} : {damage} 데이미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.damage} : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0 :
            print(f'{self.name} : 파괴되었습니다.')

# 날 수 있는 기능
class Flyable: 
    def __init__(self,flying_speed) :
        self.flying_speed = flying_speed
    
    def fly(self,name,location) :
        print(f'{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]')


# 공중 공격 유닛 클래스
class FlybleAtteackUnit(AttackUnit,Flyable) :
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0으로 취급
        Flyable.__init__(self,flying_speed)

    def move(self, location) :
        print('[공격 유닛 이동]')
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit) :
    def __init__(self, name, hp, location):
        pass # 그냥 넘어감

# 서플라이 디폿 : 건물, 1개 건물 = 8유닛
sypply_depot = BuildingUnit('서플라이 디폿',500,'7시')

def game_start() :
    print('[알림] 게임이 시작됩니다.')

def game_over() :
    pass

game_start()
game_over() # 그냥 넘어감