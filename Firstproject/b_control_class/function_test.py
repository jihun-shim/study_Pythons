# 1. 문자열을 입력받아 모든 문자를 대문자로 변환하여 반환하는 함수를 생성하고 호출
# 오류뜨면 괄호 부터 체크!!!

def abc(a):
    return a.upper()

ABC = input('입력 :')
print(abc(ABC.upper( ) ) )

# def abc(a):
#     return a.upper()
# str = input('입력 :')
# print(abc(str))


# 2. 가로/세로 길이를 입력받아 넓이를 구하는 함수
# print('넓이 : ', get_area(4, 5))      # 넓이 : 20 출력
def get_area(a,b):
    return a * b
print('넓이 : ', get_area(4, 5))

# 3.주민번호 형태를 가지고 호출하면
jumin = input('주민번호 입력->')
#    1) 성별을 반환하는 함수 (get_sex[juminNO])
def get_sex(juminNO):
    if (juminNO[7] == '1') or (juminNO[7] == '3'):
        return '남자입니다.'
    else:
        return '여자입니다.'


#    2) 나이를 반환하는 함수 (get_age[juminNO])
from datetime import date
today = date.today()
def get_age(juminNO):
    if (juminNO[7] == '1') or (juminNO[7] == '2'):
        age1 = int(juminNO[0:2]) + 1900
        return(((today.year) - (age1)) + 1)
    else:
        age2 = int(juminNO[0:2]) + 2000
        return(((today.year) - (age2)) + 1)

#    3) 지역을 반환하는 함수 (get_location[juminNO]
location = jumin[8]
birtharea=''
def get_location(juminNO):
    if location == '0':
        birthare = '서울'
    elif location == '1':
        birthare = '인천/경기'
    elif location == '3' or location == '4':
        birthare = '충청도'
    elif location == '5':
        birthare = '전라도'
    elif location == '7' or location == '8':
        birthare = '경상도'
    elif location == '9':
        birthare = '제주도'
    else:
        birthare = '강원도'

    return('출생지역은' + ' ' + birthare + '입니다')

# 생성한 함수를 호출하여 테스트
print(get_sex(jumin))
print(get_age(jumin))
print(get_location(jumin))
#print('개인정보 - 성별 : ', get_sex(jumin), ' , 나이 : ', get_age(jumin) , ', 출생지역 get_location(jumin))


# 4. 리스트 형태의 값을 받아 처리하는 함수
# 호출 예)
# fruit = ['orange', 'mango', 'apple']
# 1) get_fruit(fruit)         # 리스트의 모든 과일 [목록/갯수]가 출력됨 len사용
fruit = ['orange', 'mango', 'apple']
def get_fruit(fruit):
# return ('orange', 'mango', 'apple') 굳이 필요 없음
# for item in fruit:
#     print(item)
# print('--------------------')
# print(' 과일 총 개수 : ', len(fruit))
#
# # 2) print(isfruit('mango'))    # True 출력
# fruit = input('망고입력->')
# def isfruit(fruit):
#     if('mango'):
#         return ('Ture')
#     else:
#         return ('False')
# print(isfruit(fruit))
#
# # 3) print(isfruit('Grapefruit '))    # False 출력
# fruit = input('자몽입력->')
# def isfruit(fruit):
#     if('grapefruit'):
#         return ('False')
#     else:
#         return ('true')
# print(isfruit(fruit))

# get_fruit(fruit)

def isfruit(trufal):
    return trufal in fruit
print('-------------------------')
print(isfruit('mango'))
print(isfruit('Grapefruit'))