"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록을 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

#1)--------------------------
a = -1
if a :
     print('ture')
else :
     print('false')
#2) 논리 연산자를 이용한 조건-------
a=10
b=-1

if a and b :
    print('true2')

if a or b :
    print('true3')

#정리 필요
print(a and b) #b 값에 의해 결과가 결정되기 때문에 b값을 지정
print(a or b) #a로 부터 결과가 결정 되기 때문에 b값을 수행하지 않음

print('-'*50)
# 3)---------------------------
#find() 함수는 못찾으면 -1을 리턴하고, 첫번째 인자라면 0(거짓)을 리턴

word = 'korea'
if word.find('z') > -1:
    print('>' + word)

if word.find('k') > -1:
    print('2>' + word)

if word.find('z') > -1:
    print('3>' + word)

#블럭을 맞춰야 함, 한 칸이라도 달라지면 실행되지 않는다.

a=10
if not a:
    print('inside if'+str(a))
    print('outside if'+str(a))




