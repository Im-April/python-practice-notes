python = 'Python is Amazing'
print(python.lower()) # 모두 소문자로
print(python.upper()) # 모두 대문자로
print(python[0].isupper()) # 대문자인지 확인
print(len(python)) # 문자열 길이
print(python.replace('Python','Java')) # 글자를 바꿔줌

index = python.index('n') # 위치 확인 (가장 앞에 있는 부분만)
print(index)

index = python.index('n',index+1) # 탐색 시작 위치 선정
print(index)

print(python.find('n'))
print(python.find('java')) # 없는 문자를 넣으면 -1이 나온다
# print(python.index('java')) 이건 오류가 난다.

print(python.count('n')) # n이 몇 번 등장하는지 확인