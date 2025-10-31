absent = [2,5] # 결석
no_book = [7] # 책을 가지고 오지 않음

for student in range(1,11) :
    if student in absent :
        continue
    if student in no_book :
        print(f'오늘 수업 종료 {student}번 학생 교무실로 오세요')
        break
    print(f'{student}번 책을 읽으세요')