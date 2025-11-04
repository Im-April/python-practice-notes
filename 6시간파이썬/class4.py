class Unit :
    def __init__(self,name,hp,damage): 
        # 멤버 변수 : 클래스 내에서 선언된 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다.\n체력 : {self.hp}\n공격력 : {self.damage}')


class AttackUnit :
    def __init__(self,name,hp,damage): 
        # 멤버 변수 : 클래스 내에서 선언된 변수
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location) :
        print(f'{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 : {self.damage}]')

    def damaged(self, damage) :
        print(f'{self.name} : {damage} 데이미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.damage} : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0 :
            print(f'{self.name} : 파괴되었습니다.')

# 공격 유닛, 화염방사
firebet1 = AttackUnit('파이어벳',50,16)
firebet1.attack('5시')
firebet1.damaged(25)
firebet1.damaged(25)