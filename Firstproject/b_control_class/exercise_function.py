
"""
[ 연습문제 ]

- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
    [ 출력 결과 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

- 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
    [ 출력 결과 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

# - 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
#     [ 출력 결과 ]
#         print(count_vowel("pythonian"))


1. 10부터 1씩 감소하여 다음의 형태로 출력
결과) 10,9,8,7,6,5,4,3,2,1

2. 수를 입력받아 다음의 결과로 출력
결과)
수 입력 -> 5
*
**
***
****
*****
"""

def for_test () :
    for num in range(10):
        if num < 9:
            print("%d"%(10-num),end=', ')
        else:
            print("%d"%(10-num))
    return

def for_test2 () :
    for num in range(10):
        print("%d"%(10-num),end=', ' if num < 9 else '\n' ) # inline으로 처리 하기 위해 검색해 보았습니다
    return

def star_test (star_cnt = -1) :
    if star_cnt < 0 : # 음수 예외 처리
        return print("wrong input number")
    for line_num in range(star_cnt):
        for star_print_cnt in range(line_num+1):
            print("*",end="")
        print()
    return

def even_filter (test_list=None) :
    if test_list is None: # 빈 리스트 예외
        return print("empty list") # 더 좋은 방법 찾아 보기
    return  [x for x in test_list if x % 2 == 0]

def is_prime_number( prime_num = 0) : # 1에 대한 예외 처리 필요, 잘못된 값 예외처리 필요
    prime_num = abs(prime_num)
    if prime_num < 2 :
        return print("wrong input number")
    for num in range(2, prime_num) :
        if prime_num % num == 0 :
            return False
    return True

# for_test()
# star_test(5)
# print(even_filter([1, 2, 4, 5, 8, 9, 10]))
# print(is_prime_number(60))
# print(is_prime_number(61))
# print(is_prime_number(11))
# print(is_prime_number(7))
# print(is_prime_number(2))
# print(is_prime_number(3))
# print(is_prime_number(4))
# print(is_prime_number(353))
# for_test2()
#
# print(even_filter([]))
# print(even_filter())
# # star_test(7)
# # star_test(11)
# # star_test(1)
# # star_test(2)
# star_test(0)
# star_test()
#®
# star_test(-11)
# star_test(-11)
#
# #star_test(-11.1) # 소수는 range 에서 에러남
# #star_test(11.1)
#
# print(is_prime_number(0))
# print(is_prime_number(1))
# print(is_prime_number(2))
# print(is_prime_number(-1))

print('-'*45)
# print('-'*20 +'menu'+ '-'*20)
print('1. 10부터 1씩 감소하여 다음의 형태로 출력')
for_test2()
print()

print('3. 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수')
print('print(even_filter([1, 2, 4, 5, 8, 9, 10])) =', even_filter([1, 2, 4, 5, 8, 9, 10]))
print()

print('4. 주어진 수가 소수인지 아닌지 판단하는 함수')
print('print(is_prime_number(60)) =', is_prime_number(60))
print('print(is_prime_number(61)) =', is_prime_number(61))
print()

print('2. 수를 입력받아 다음의 결과로 출력')
input_num = eval(input('수 입력 ->')) # 더 좋은 예외 처리 방법 찾아보기
if isinstance(input_num, int) : # float은 처리 가능
    star_test(input_num)
else :
    print("wrong input number")



print('-'*45)
