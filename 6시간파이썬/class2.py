# __init__

class Unit :
    def __init__(self,name,hp,damage): # 객체가 생성될 때 자동으로 호출되는 부분
        # init 함수에 정의된 self를 제외한 갯수만큼 보내주어야 객체를 만들 수 있다
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다.\n체력 : {self.hp}\n공격력 : {self.damage}')

# marine3 = Unit('마린') # Error
# marine34= Unit('마린',45) # Error