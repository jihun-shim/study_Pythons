
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 : #조건을 만족하는 (참인)동안 반복을 수행
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

# for entry in a: # a는 반복이 안되지만 b부터 e까지는 반복된다.
#    print(entry)

for entry in b:
    print(entry,end='')

for entry in c:
    print(entry)

for entry in d:
    print(entry)

for entry in e.keys():
    print(entry)

for entry in e.items():
    print(entry)

#range(10) : 0~9 , range(1,11) : 1~10
#1~10까지 출력
for a in range(1,11) :
    print(a, end=' ')

# 1~10까지 합계 구하기
print()
sum = 0
for i in range(1,11,2) : #홀수 짝수
    #print(i, end=' ')
    sum += i
print(sum)

#구구단 2단 출력
# for i in range(1,10): #1~9까지
#     print(dan,'*',i,'=',dan*i)
for i in range(1,10):
    print('2*',i,'*',str(2*i))

# dan=2
# for s in range(1,10):
#     print('%s * %s= %s' %(dan,s,(s*dan)))

#구구단 2~9단까지 이중 반복문으로 출력------------------------------
for d in range(2,10):
    for dd in range(1,10):
        print(d,'x',dd,'=',str(d*dd))
    print()
#---------------------------------------------


# =========================================================
# while

a = 1
while True:  # 무한루프
   if a == 1:
       print(a)
       break

# 1~10까지 출력(while)
i = 1
while i<=10:
    print(i)
    i+=1

#1~10까지 합계 구하기 (while)
s = 1
sum = 0
while s<=10:
    #print(s)
    sum+=s
    s += 1
print('total : ',sum)


a = ['x', 'y', 'z']
while a:    # 요소만큼 반복함
    data = a.pop()
    if data == 'y': break
    print(data)
# else:
#     print("end")




    i ='*'
    while i <= '*****':
        print(i)
        i+='*'



