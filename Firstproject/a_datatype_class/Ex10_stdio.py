"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int()/ float() / str() 자료형 변환(권장)
"""

name = input('이름입력->')
print('당신은 %s입니다.' % name)
print('당신의 이름은 {0}입니다.'.format(name))

age = int(input('나이입력'))
print('나이 :',age+1)
height = eval(input('키입력'))
print('키 :',height)

print(eval('1+2'))




#----------------------------------
# 단을 입력받아 구구단을 구하기

# dan = int(input('단 입력->'))
# for i in range(1,10): #1~9까지
#     print(dan,'*',i,'=',dan*i)


#-----------------------------------------
# print() 함수
# print('안녕''친구')  #연산자 없이도 문자열 연결
# print('안녕'+'친구') #문자열 연결
# print('안녕','친구') #문자열 띄어쓰기
#
# #for i in range(5):
#     print(1, end=' ') #end 속성을 이용 기능(기본값 : 개행문자)

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0         1      2      3
