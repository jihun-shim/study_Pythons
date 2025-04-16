# 두 수를 곱하는 함수 생성
from statistics import multimode


def func_mul (n,n1):
    return n * n1

#호출
print(func_mul(15,28))

# 튜플 데이터를 받아서 튜플의 정보를 출력하는 함수 생성
def get_tuple(t):
    for s in t:
        print(s, end='\t')
    return

get_tuple((1,2,3,4,5))

print()
t = (12,15,16,18)
get_tuple(t)

# 함수 관련 변수의 범위(글로벌 변수)