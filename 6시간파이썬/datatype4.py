# 변수 사용하기
# 애완동물을 소개해주세요

animal = '강아지'
name = '마루'
age = 2
hobby = '산책'
is_adult = age >= 4


print('우리집에는 '+animal+'가 있는데 이름은 '+name+'입니다.')
print(name+'은/는',str(age)+'살 이며,',hobby+'를 아주 좋아합니다.')
# 콤마를 사용하면 str() 사용 안해도 되지만 .. 띄어쓰기가 된다.

print(name+'은/는 어른일까요 ?',is_adult)
