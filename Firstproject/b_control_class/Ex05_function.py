"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언(정의)하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""

#(0) 매개변수,리턴값도 없는 함수
def func():
    print('함수를 호출하셨군요 ~')

func()
print(func()) #함수가 아무값도 반환(리턴)하지 않으면 None이 반환

#(1) 리턴값이 있는 함수
def func1(arg1, arg2):
    return arg1 + arg2

sum = func1(3,4) #sum = 7 리턴값이 있는 함수는 담을 변수가 필요

# (2) 여러개의 리턴값을 갖는 함수
def func2(arg1, arg2):
    return arg1+5, arg2-5

print(func2(10, 20))
a, b= func2(10,15) #unpacking
print(a+b)


#func3("안녕","홍동우") # 안녕!!! 홍동우님~!
#func3("헬로우", "홍길동")

def func3(arg1, arg2):
    return arg1+'!!! '+ arg2+'님~!'

print(func3('안녕','홍동우'))
print(func3('헬로우','홍길동'))

#(3) 키워드 인자
print(func3(arg2='홍동우',arg1='하이'))

#(4) 기본 매개변수값 지정하기
print()
def func4(arg1, arg2="홍동우"):
    print(arg1+'!!! '+ arg2+'님~!')

#func4("안녕") # 오류
func4("안녕")
func4('헬로우','홍길동')

def func5(i1, i2, i3=100):
    print(i1+i2+i3)

func5(1,2)
func5(1,2,3)

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('A')
buggy('B')
buggy('C')
#print(result) # 함수내에서 선언된 변수는 사용할 수 없음
buggy('Z',[1,2,3,4])
buggy('가')

# *** 기본 인자값은 함수가 실행될 때 실행하지 않고, 함수를 정의할 때 지정한다

# (5) 위치 인자 모으기 : *
def func(i1, i2, i3=0, *args): # * - positional argument
    sum = i1 + i2 + i3
    for i in args:
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))

'''
1번째와 2번째는 인자가 반드시 들어가고 3번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 4번째 인자부터는 정확히 모른다면?
print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # 7,8,9가 튜플로 들어간다
'''
print("---------------------------")
# (6) 키워드 인자 모으기 : **
def func(i, j, k=100, *args, **kwargs):
    # print()
    # print(args)
    # print(kwargs)
    sum = i + j + k
    for i in args:
        sum += i
    for j in kwargs.values():  #키워드 인자는 딕셔너리로 사용
        sum += j
    return sum

func(10,20)
func(1,2,3)
func(1,2,3,4,5,6)
func(1,2,3,a=10,b=11,c=12)
func(1,2,3,4, a=10,b=11,c=12)
print(func(1,2,3,4, a=10,b=11,c=12))

