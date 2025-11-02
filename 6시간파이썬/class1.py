# # 마린 : 공격 유닛, 군인, 총을 쏜다.
# name = '마린'
# hp = 40
# damage = 5
# print(f'{name} 유닛이 생성되었습니다.\n체력 : {hp}\n공격력 : {damage}')

# #탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음 (일반 모드, 시즈 모드)
# tank_name = '탱크'
# tank_hp = 150
# tank_damage = 35
# print(f'{tank_name} 유닛이 생성되었습니다.\n체력 : {tank_hp}\n공격력 : {tank_damage}')

# tank2_name = '탱크2'
# tank2_hp = 150
# tank2_damage = 35

# def attack(name, location, damage) :
#     print(f'{name} 유닛이 {location} 방향으로 공격합니다.\n[공격력 : {damage}]')

# attack(name,'1시',damage)
# attack(tank_name,'1시',tank_damage)
# attack(tank2_name,'1시',tank_damage)

# 클래스 : 붕어빵 틀
# 서로 연관있는 변수와 함수의 집합

# 클래스 만들기
class Unit :
    def __init__(self,name,hp,damage): # 필요한 값 정의
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다.\n체력 : {self.hp}\n공격력 : {self.damage}')

marine1 = Unit('마린',40,5)
marine2 = Unit('마린',40,5)
tank = Unit('탱크',150,35)

        