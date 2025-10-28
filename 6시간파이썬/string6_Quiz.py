"""
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하세요

예) http://naver.com
규칙 1 : http:// 부분 제외 => naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성 
"""

site = 'http://naver.com'

rule1 = site[7:]
rule2 = rule1[:-4]
rule3 = rule2[:3]
count_word = len(rule2)
e_count = rule2.count('e')

print(rule3+str(count_word)+str(e_count)+'!')

print('-'*30)
print('강사님 풀이')

url = 'http://naver.com'
my_str = url.replace('http://',"") # 규칙 1
print(my_str)

my_str = my_str[:my_str.index('.')]
print(my_str) # 규칙 2

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e'))+'!'
print(password)