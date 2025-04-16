"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + ctrl + F10

    [도움말] ctrl + q

"""

""" 여러줄 주석 """
# 한줄 주석

print("헬로우")
print('hello')
print("""안녕""")
print('''올라''')
# 실행 : shift + alt + F10

'''
변수란
    파이션의 모든 자료형을 객체로 취급한다
    a = 7
            7을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스(주소)이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
'''

#파이썬의 예약어 확인
# import keyword # keyword 모듈 로딩
# print(keyword.kwlist)
# # print(len(keyword.kwlist))
#
# print('--------------------')

# a=7
# b=7
# print(type(7))
# print(a is 7)
# print(b is 7)
# print(a is b) # 동일한 객체를 가리키는 것으로 판단
#
# print(id(7)) # 동일한 주소를 참조
# print(id(a))
# print(id(b))

# 여러 변수 선언
a,b=5,10

print(a,b) # 여러값을 ,로 구분
print(a+b)
print('a=',a,'b=',b)

#변수 삭제
del b
print('b=',b) # 에러 발생
