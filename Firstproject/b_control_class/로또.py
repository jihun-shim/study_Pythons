import random

lotto = [ n for n in range(1, 46)]
#print(lotto)


#for n in range(30000):
    # 1 ~ 44 사이의 임의의 숫자를 발생
# sum = 0
# while True:
#     sum +=1
#     room = random.randint(1,44)
#
      #lotto [0] 와 lotto[?]의 값을 바꾸기
      # imsi = lotto[0]
      # lotto[0] = lotto[room]
      # lotto[0] = imsi
#
#     lotto[0], lotto[room] = lotto[room], lotto[0]
#
#     if sum == 30000: break
#     else: continue
#
#for n in range(5):
     # print(lotto[n], end = '\t')
#----------------------------------------------
print()

for m in range(5):
    print(m+1, ' . ', end='\t')
    for n in range(30000):
        room = random.randint(1,44)
        lotto[0], lotto[room] = lotto[room], lotto[0]

    for n in range(5):
        print(lotto[n], end = '\t')
    print()

#-----------------------------------------------
print()

for n in range(30000):
    room = random.randint(1,44)
    lotto[0], lotto[room] = lotto[room], lotto[0]

lottosort=[] # 로또번호 정렬을 위한 변수
for n in range(5):
    #print(lotto[n], end = '\t')
    lottosort.append(lotto[n])

lottosort.sort()
print(lottosort)


    # lotto [0] 와 lotto[?]의 값을 바꾸기
    # imsi = lotto[0]
    # lotto[0] = lotto[room]
    # lotto[0] = imsi