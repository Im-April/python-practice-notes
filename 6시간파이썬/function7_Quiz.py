"""
표준 체중을 구하는 프로그램을 작성하세요
* 표준체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
    - 함수명 : std_weight
    - 전달값 : 키(height), 성별(gender)

조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg입니다.
"""

def std_weight(height, gender) :
    height_m = height/100

    if gender == '남자' :
        print(f'키 {height}cm {gender}의 표준 체중은 {height_m*height_m*22:.2f}kg 입니다.')
        return height_m*height_m*22
    else :
        print(f'키 {height}cm {gender}의 표준 체중은 {height_m*height_m*21:.2f}kg 입니다.')
        return height_m*height_m*21

std_weight(175,'남자')