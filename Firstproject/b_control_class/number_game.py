#숫자 맞추기 게임
import random

com = random.randint(1,100)
#print(com)

sum = 0
while True:
    sum +=1
    inputsu = int(input('숫자 입력->'))
    if(inputsu > com):
        print('더 작은 수야~')
        continue
    elif (inputsu < com):
        print('더 큰수 수야~')
        continue
    else:
        print('오~맞췄어!')
        break

print(sum, '번 만에 맞추었네~!!')

#1. 1~45 [1,2,3,...45]
#반복 30000번
#2.