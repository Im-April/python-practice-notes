# while

customer = '난 직원이고 넌'
index = 5

while index >= 1 :
    print(f'\'{customer}\' 고객님 커피가 준비되었습니다. {index}번 남았어요')
    index -= 1
    if index == 0 :
        print('커피는 폐기되었습니다')

# 무한 루프
# customer = '꼴에 스벅오신'
# index = 1

# while True :
#     print(f'\'{customer}\' 고객님 커피가 준비되었습니다. {index}번 호출')
#     index += 1

customer = '고곡곡곡곡'
person = 'Unknown'

# 조건이 만족하면 계속 반복
while person != customer :
    print(f'\'{customer}\' 고객님 커피가 준비되었습니다.')
    person = input('이름이 어떻게 되세요? : ')