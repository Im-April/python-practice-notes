# 집합
# 중복 안됨, 순서 없음

my_set = {1,2,3,3}
print(my_set)

java = {'유재석','김태호','양세형'}
python = set(['유재석','박명수'])

# 자바와 파이썬을 모두 할 수 있는 사람
print(java & python)
print(java.intersection(python)) # 교집합 값

# 자바를 할 수 있거나 파이썬도 가능한 개발자
print(java | python)
print(java.union(python)) # 합집합 값

# 차집합
# 자바는 할 줄 알지만 파이썬을 모르는 개발자
print(java - python)
print(java.difference(python))

# 파이썬을 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)

# 김태호가 java를 까먹음 ;;
java.remove('김태호')
print(java)
