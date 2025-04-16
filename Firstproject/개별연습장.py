#wikidocs.net/7014 예제연습

#01.) 파이썬 시작하기
# print('Hello World')
# #print는 정수, 실수, 문자열 등을 화면에 출력합니다. 문자열은 큰따옴표 또는 작은따옴표로 표현 가능합니다.
#
# print("Mary's cosmetics")
# print("'신씨가 소리질렀다.'도둑이야.")
# print('C:\Windows')
# print("안녕하세요 .\n만나서\t\t반갑습니다.")
# print("오늘은","일요일")
# #여러 값을 출력하려면 print 함수에서 쉼표로 구분해주면 됩니다. 따라서 오늘은 다음에 공백이 하나 있고 일요일이 출력됩니다.
# print("naver;kakao;sk;samsung")
# #print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력됩니다.
# #print("naver", "kakao", "samsung", sep=";")
# print('naver','kakao','sk','samsung',sep='/')
# print("first",end="");print("second")
# print(5/3)

# #02.) 파이썬 변수
# 삼성전자 = 50000
# 총평가금액 = 삼성전자 * 10
# print(총평가금액)
#
# 시가총액 = 298000000000000
# 현재가 = 50000
# PER = 15.79
# print(시가총액,type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# s = "hello"
# t = "python"
# print(s+"!"+" "+ t)
# print(s+"!", t)
#
# 2 + 2 *3
# print(2+2*3)
#
# a="132"
# print(type(a))

# num_str = "720"
# print(int(num_str))
# num_int = int(num_str)
# print(num_int+1, type(num_int))

# num=100
# print(str(num))
# result = str(num)
# print(result, type(result))
#
# num="15.79"
# result = float(num)
# print(result, type(result))
# print(float(num))

# if 4 < 3:
#     print("Hello World")
#
#
#
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")

# a=input('입력 :')
# print(a * 2)

# b=input('입력 :')
# print(int(b) + 10)3

b=input('입력 :')
if int(b) % 2 == 0:
        print("짝수")
else:
        print("홀수")



