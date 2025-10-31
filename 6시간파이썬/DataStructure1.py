# 리스트 : 순서를 가지는 객체의 집합

# 지하철 칸 별로 10명, 20명, 30명이 있음
subway = [10,20,30]
print(subway)

subway = ['유재석','조세호','박명수']
print(subway)

# 조세호님은 몇 번째 타고 있나?
print(subway.index('조세호'))

# 다음 역에 하하가 탔다
subway.append('하하')
print(subway)

# 정형돈씨가 유재석과 조세호 사이에 태워봄
subway.insert(1,'정형돈') # 인덱스, 객체
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 빼보자
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇명인지 ..
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 정렬하기
num_list = [5,2,4,3,1]
num_list.sort() # 오름차순
print(num_list)

# 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)


# 다양한 자료형과 함께 사용
mix_list = ['조세호',20,True]
print(mix_list)

# 리스트 확장
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)