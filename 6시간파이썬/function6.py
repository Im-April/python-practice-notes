# 지역변수와 전역변수

gun = 10

def checkpoint(solidiers) :
    global gun # 전역 공간에 있는 gun 사용
    gun = gun-solidiers
    print(f'함수 내 에서는 남은 총 : {gun}')


print(f'전체 총 : {gun}')
checkpoint(2)
print(f'남은 총 : {gun}')

def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print(f'함수 내 남은 총 : {gun}')
    return gun

print(f'전체 총 : {gun}')
gun = checkpoint_ret(gun,2)
print(f'남은 총 : {gun}')