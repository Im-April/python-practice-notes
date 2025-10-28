# 문자열 포맷

print('a'+'b')
print('a','b')

# 방법 1
print('나는 %d살 입니다' % 20)
print('나는 %s을 좋아합니다.' % "파이썬")
print('Apple 은 %c로 시작해요' % 'A')
print('나는 %s색과 %s색을 좋아해요' % ('파란','빨간'))

# 방법 2
print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}을 좋아한다.'.format('빨간','파란'))
print('나는 {1}색과 {0}을 좋아한다.'.format('빨간','파란'))

# 방법 3
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age=20,color='빨간'))
print('나는 {color}색을 좋아하며, {age}살 입니다.'.format(age=20,color='빨간'))

# 방법 4
age = 20
color = '빨간'

print(f'나는 {age}살이며, {color}색을 좋아합니다')