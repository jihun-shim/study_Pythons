# for d in range(2,10):
#     for dd in range(1,10):
#         print(d,'x',dd,'=',str(d*dd))
#     print()

# # 초기 값 설정
# 원금 = 4500000  # 원금
# 이자율 = [0.024, 0.036]  # 이자율 목록 (2.4%, 3.6%)
# 세금율 = [0, 0.154]  # 세금율 목록 (0%, 15.4%)
# 기간 = 33  # 총 기간 (개월)

# # 3개월씩 단리 계산을 진행합니다.
# 기간_단위 = 3
# 총_단위 = 기간 // 기간_단위

# # 결과를 저장할 리스트
# 결과 = []

# for i in range(len(이자율)):
#     # 각 이자율과 세금율에 대해 단리 계산
#     해당_이자율 = 이자율[i]
#     해당_세금율 = 세금율[i]
#     총이자 = 0
    
#     for _ in range(총_단위):
#         이자 = 원금 * 해당_이자율 * (기간_단위 / 12)  # 단리 이자 계산 (기간을 년 단위로 환산)
#         세금 = 이자 * 해당_세금율  # 세금 계산
#         실이자 = 이자 - 세금  # 실수령 이자
#         총이자 += 실이자
    
#     최종_원리금 = 원금 + 총이자
#     결과.append((f"이자율 {해당_이자율 * 100}% 세후 최종 원리금:", round(최종_원리금, 2)))

# # 결과 출력
# for r in 결과:
#     print(r[0], r[1])

# deposit_my_list = 4500000
# bank_rate_year = [0.024, 0.036]
# bank_tax_interest_rate = [0, 0.154]

# p = deposit_my_list
# r = bank_rate_year
# tax = bank_tax_interest_rate

# def func(p,r,t,tax):  
#     cal = p * ( 1 + (( r * t ) * ( 1 - tax) ) )    
#     return

# func(4500000,0.024,0,3)
# print(cal)

#  for t in range(3,34,3):
#     print(p[0] * ( 1 + ( r[0]/12 * t ) * ( 1 - tax[0] ) ) )


# # cal('입니다')
# 리스트 = ['dog', 'cat', 'parrot']
# for qustn in 리스트:
#        print(qustn[0].upper()+qustn[1:])

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for qustn in 리스트:
#     스플릿 = qustn.split(".")
#     print(스플릿[0])

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for qustn in 리스트 :
#        split = qustn.split(".")
#        if (split[1]=="h") or (split[1]=="c"):
#               print(qustn)

# for i in range(100) :
#     print(99-i)

# for i in range(10):
#     print(i/10)

# 구구단 3단을 출력하라.
# # for i in range(1,10):
# #     print(3, 'x', i, '=',3*i)

# 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
# # for i in range(1,10,2):
# #     print(3, 'x', i, '=',3*i)

# 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# # hab =  0 #hab 이라는 변수에 0을 저장하고, for 문을 통해 모든 값에 대해 누적합니다.
# # for i in range(1,11):
# #     hab += i #hab += i 는 아래 코드를 축약해서 작성한 것입니다.
# #     print("합 :",hab)

# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# # sum=0
# # for i in range(1,11,2):
# #     sum += i
# #     print(sum) 

# 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# # gob=1
# # for i in range (1,11):
# #     gob *= i
# # print('곱 : ',gob)

# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print (price_list[i])

# price_list = [32100, 32150, 32000, 32500]
# for i, data in enumerate(price_list):
#     print(i, data)

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print((len(price_list) - 1) - i, price_list[i])

# price_list = [32100, 32150, 32000, 32500]
# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])

# my_list = ["가", "나", "다", "라"]
# for i in [0,1,2]:
#     print(my_list[i],my_list[i+1])
# for i in range( len(my_list) - 1 ) :
#   print(my_list[i], my_list[i+1])   
# for i in range( len(my_list) - 1 ) :
#   print(my_list[i], my_list[i+1])   

# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print(my_list[i],my_list[i+1],my_list[i+2])

my_list = ["가", "나", "다", "라"]

# # print(my_list[3], my_list[2])
# # print(my_list[2], my_list[1])
# # print(my_list[1], my_list[0])

# for i in range(len(my_list)-1,0,-1):
#     print(my_list[i],my_list[i-1])

# my_list = [100, 200, 400, 800]
# for i in [0,1,2]:
#     print(abs(my_list[i+1]-my_list[i]))
# for i in range(len(my_list) - 1):
#     print(abs(my_list[i+1] - my_list[i]))   
# 

# my_list = [100, 200, 400, 800, 1000, 1300]
# print((my_list[0] + my_list[1] + my_list[2])/3)
# print((my_list[1] + my_list[2] + my_list[3])/3)
# print((my_list[2] + my_list[3] + my_list[4])/3)
# print((my_list[3] + my_list[4] + my_list[5])/3)
# for i in [1,2,3,4]:
#        for i in range(1,len(my_list)-1):    
#               print((my_list[i-1] + my_list[i] + my_list[i+1])/3)


# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility=[]

# for i in (len(low_prices)):
#     volatility.append(high_prices[i]-low_prices[i])

# print(volatility)

# stock = {"시가" : [100,200,300],"종가" : [80,210,330]}
# stock = {"10/10" : [80, 110, 70, 90],"10/11" : [210,230,190,200]}

# apart = [ [101, 102], [201, 202], [301, 302] ]
# print(apart[0][0],"호", apart[0][1],"호", apart[1][0],"호",apart[1][1],"호",apart[2][0],"호",apart[2][1],"호")

# for row in apart:
#     for col in row:
#        print(col, "호")

apart = [ [101, 102], [201, 202], [301, 302] ]

# for row in apart[::-1]:
#     for col in row:
#         print(col, "호")

# for row in apart[::-1]:
#     for col in row[::-1]:
#         print(col, "호")

# for row in apart:
#     for col in row:
#         print(col, "호")
#         print("-----")

# for row in apart:
#     for col in row:
#         print(col, "호")
# print("-"*5)

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# result = []
# for line in data:
#     sub =[]
#     for column in line:
#        sub.append(column*1.00014)
#     result.append(sub)
# print(result)   

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# for i in ohlc[1:]:
#        print(i[3])

# for i in ohlc[1:]:
#     if i[3]>150:
#        print(i[3])
# for i in ohlc[1:]:
#     if i[3]>=i[0]:
#        print(i[3])

# volatility = []
# for i in ohlc[1:]:
#     volatility.append (i[1]-i[2])
# print(volatility)

# for i in ohlc[1:]:
#     if i[3] > i[0]:
#        print(i[1]-i[2])

sum=0
for i in ohlc[1:]:
       sum += (i[3]-i[0])
        print(sum)