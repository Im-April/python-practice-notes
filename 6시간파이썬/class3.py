class Unit :
    def __init__(self,name,hp,damage): 
        # 멤버 변수 : 클래스 내에서 선언된 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다.\n체력 : {self.hp}\n공격력 : {self.damage}')

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit('레이스',80,5)
print(f'유닛 이름 : {wraith1.name}\t공격력 : {wraith1.damage}')

# 마인드컨트롤(상대방 유닛을 내 유닛으로 만들수 있음)
wraith2 = Unit('빼앗은 레이스',80,5)
wraith2.clocking = True # 클래스 외부에서 변수 추가 할당

if wraith2.clocking == True :
    print(f'{wraith2.name}는 현재 클로킹 상태입니다.')