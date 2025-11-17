# 람다(lambda)
# lambda 매개변수 : 표현식

# 두 수를 더하는 함수

def hap(x,y) :
  return x+y

hap(1,2)

# 람다 형식으로 표현
(lambda x,y : x+y)(10,20)

# map 함수 사용
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))

# 함수 사용
def square(x) :
  return x ** 2

list(map(square, [1, 2, 3, 4, 5])) # map(함수, 이터러블)