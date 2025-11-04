# 상속

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

# 메딕 : 의무병

firebet1 = AttackUnit('파이어벳',50,16)
firebet1.attack('5시')
firebet1.damaged(25)
firebet1.damaged(25)