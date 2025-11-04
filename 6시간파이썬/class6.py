# 다중 상속

# 일반 유닛
class Unit :
    def __init__(self,name,hp): 
        # 멤버 변수 : 클래스 내에서 선언된 변수
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self,name,hp,damage): 
        # Unit 상속
        Unit.__init__(self, name, hp)
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self,flying_speed)

# 드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송해줌. 공격 불가

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlybleAtteackUnit('발키리',200,6,5)
valkyrie.fly(valkyrie.name,'3시')