# 딕셔너리
# {키:값}
# 키는 중복 불가

cabinet = {3:'유재석', 100:'김태호'}
print(cabinet)
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5]) -> keyError
print(cabinet.get(5)) # None이 출력
print(cabinet.get(5,"사용가능")) # 값이없을 때 사용가능 출력

print(3 in cabinet) # 객체가 캐비닛에 있는지 True / False
print(5 in cabinet)

cabinet = {"A-3":'유재석', 'B-100':'김태호'}
print(cabinet['A-3'])

# 새로운 손님 추가
print(cabinet)
cabinet['C-20'] = '조세호'
print(cabinet)

# 값 바꾸기
cabinet['A-3'] = '김종국'
print(cabinet)

# 간 손님
del cabinet['A-3']
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)