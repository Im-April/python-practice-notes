
# def profile(name, age, lang1, lang2, lang3, lang4,lang5) :
#     print(f'이름 : {name}\t나이 : {age}\t', end = " ")
#     print(lang1, lang2, lang3, lang4,lang5)

# 가변인자 이용 : 입력값의 개수가 정해져 있지 않을 때 유연하게 처리

def profile(name, age, *language) :
    print(f'이름 : {name}\t나이 : {age}\t', end = " ")
    for lang in language :
        print(lang, end=' ')
    print()

profile('유재석',20,'Python','C','Java',"C++","C#","JavaScript")
profile('김태호',25,'Kotlin','Swift','',"","")




