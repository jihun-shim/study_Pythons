
# [추가] 함수도 객체이다
def case1():
    print('case-1')

def case2():
    print('case-2')

def case3():
    print('case-3')

f = {'case1' : case1, 'case2' : case2, 'case3' : case3}
a = 'case3'
f[a] # a['case3'] : 문자열
f[a]() #case3()형태로 함수를 호출하게 됨 (함수가 값으로 사용되었을때는 ()를 붙여서 호출)
#---------------------------------------
# 글로벌 변수와 지역변수
temp = '글로벌'
def func():
    print(temp)

func()

temp2 = '글로벌'
def func2():
    #print(temp2) # 오류(지역변수는 선언을 먼저 해야 함)
    temp2 = '지역'
    print(temp2) # 지역변수

func2()
print(temp2) # 전역 (글로벌 변수)

'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
'''
def func_mul (n,n1):
    return n * n1

#호출
print(func_mul(15,28))

func_mul = lambda n,n1 : n * n1 # func_mul이 함수명
print(func_mul(15,28))


la = lambda s,s1 : s + s1
print(la(1,2))
print('---------------------------------')

#-----------------------------------------------------------
"""  맵 & 리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합*하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""
ex = [1,2,3,4,5]
calc = lambda x : x*2
res = list(map(calc, ex))  # list(map(함수, 자료))
print(res)

# 컴프리핸션과 비교
res = [x*2 for x in ex]
print(res)

from functools import reduce
ex = range(1,5)
f = lambda x, y : x * y
print(reduce(f, ex))



