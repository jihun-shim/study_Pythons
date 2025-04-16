#[문제]
# 1 ~ 100 까지의 2자리 정수로 이루어진 복권이 있다고 가정.
# 2자리가 전부 일치하면 1등, 1자리가 일치하면 2등, 맞는 숫자가 없으면 상금은 없습니다.
# 복권은 1 ~ 100사이의 난수를 발생하여 복권번호로 사용하라

# 복권번호 (1~99사이)를 입력 -> 89
# 결과) 상금은 없습니다.

#함수는 위치 상관 없음,
# 제어문, 함수 구분

# import random
# lottery = random.randint(1,100)
#
# jackpot = int(input('당첨번호 : '))
#     if jackpot == lottery:
#      print('당첨')
#
# if len (lucky) == 2
#     lucky
#
#     else:
#      print('꽝')
#
import random

while True:
    lucky= input('두자리 번호 입력(01~99) :')


    if len(lucky) ==2: #항상 두자리 출력
        lucky = int(lucky)
        break

    else:
        print("두자리 숫자를 입력하세요")

def lottery(number):
        l = random.randint(1,99)
        print(f"복권 번호: {l:02d}")
        # l:변수,
        # 0 : 숫자가 두자리 미만일때 앞에 0채우기
        # 2 :  최소 두자리
        # d : 정수형

        if l == lucky:
            return '1등 입니다!'
        elif ((l // 10)  == (lucky // 10)) or ((l % 10) == (lucky % 10)):
            return '2등 입니다!'
        else:
            return '꽝~'

result = lottery(lucky)
print(result)
