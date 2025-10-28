jumin = '990120-1234567'

print(f'성별 : {jumin[7]}')
print(f'년도 : {jumin[:2]}') # 0부터 2 직전까지
print(f'월 : {jumin[2:4]}')
print(f'일 : {jumin[4:6]}')
print(f'생년월일 : {jumin[:6]}')
print(f'뒤 7자리 : {jumin[7:]}')
print(f"뒤 7자리 (뒤에부터) : {jumin[-7:]}")