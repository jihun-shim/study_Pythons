# ------------------------------------------------

# print("Tell me your age?")
# myage = int(input())
# if myage < 30: 
#     print("Welcome to the Club.")
# else: 
#     print("Oh! No. You are not accepted.")
# ------------------------------------------------

# score = int(input("Enter your score : "))

# if score >= 90 :
#     grade = 'A'
# elif score >= 80 :
#     grade = 'B'
# elif score >= 70 :
#     grade = 'C'
# elif score >= 60 :
#     grade = 'D'
# else :
#     grade = 'F'

# print(grade)  

# ------------------------------------------------

# print("당신이 태어난 연도를 입력하세요.")
# birth_year = int(input())
# age = 2020 - birth_year + 1

# if age <= 26 and age >= 20 :
#     result = "대학생"
# elif age < 20 and age >= 17:
#     result = "고등학생"
# elif age < 17 and age >= 14:
#     result = "중학생"
# elif age < 14 and age >= 8:
#     result = "초등학생"
# else :
#     result = "출력"

# print(result)

# ------------------------------------------------

# for looper in [1,2,3,4,5]:
#     print(looper)

# for looper in range(1,100,3): # (처음시작, 마지막번호, 증가값)
#     print(looper)

# for i in 'abcdefg':
#     print(i)

# for i in ['americano','latte','frappuccino']:
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

# ------------------------------------------------

# i = 1
# while i < 10:
#     print(i)
#     i += 1

# for i in range(10):
#     if i == 5: 
#         break
#     print(i)
# print('End of program')

# 0
# ------------------------------------------------

# print("구구단 몇 단을 계산할까?")
# user_input = input()
# print('구구단', user_input, '단을 계산한다.')
# gugudan = int(user_input)

# for i in range(1,10):
#     result = gugudan * i
#     print(user_input, 'x', i, '=', result)


# print("구구단 몇 단을 계산할까?")
# user_input =  input()
# print("구구단", user_input, "을 계산한다.")
# int_input = int(user_input)
# for i in range(1,10):
#     result = int_input * i
#     print(user_input,'x',i,'=',result)
# ------------------------------------------------

# sentence = "I love you"
# reverse_sentence = ' '
# for char in sentence:
#     reverse_sentence = char + reverse_sentence
# print(reverse_sentence)

# ------------------------------------------------

# decimal = 10
# result = ' '
# while(decimal > 0):
#     remainder = decimal % 2
#     decimal = decimal // 2
#     result = str(remainder) + result 
# print(result)

# ------------------------------------------------

# import random
# guess_number = random.randint(1,100)
# print('숫자를 맞춰보세요.')
# real_number=int(input())
# while (guess_number != real_number): # if문으로 들어가지 않음 이유는 무엇?    
#     if guess_number < real_number:
#         print('숫자가 너무 큽니다.')
#     elif guess_number > real_number:
#         print('숫자가 너무 작습니다.')
#     real_number=int(input())
# else:
#     print('정답 입니다. 입력한 숫자는', guess_number ,'입니다.')

# ------------------------------------------------

# print('구구단 몇 단을 계산할까요?(1~9)')
# gugudan = int(input())
# print('구구단',gugudan,'단을 계산합니다.' )
# while (gugudan != 0):
#     for i in range(1,10):
#         result = gugudan * i
#         print(gugudan,'x',i,'=',result)
#     print('구구단 몇 단을 계산할까요?(1~9)')
#     gugudan = int(input())
# else:
#     print('구구단 게임을 종료 합니다.')
# ------------------------------------------------
# print("구구단은 몇 단을 계산할까요?(1~9)")
# x = 1
# while (x is not 0):
#     x = int(input())
#     if x == 0: break
#     if not (1 <= x <=9):
#         print("잘못 입력했습니다", "1부터 9 사이 숫자를 입력하세요.")
#         continue
#     else:
#         print("구구단" + str(x) + "단을 계산합니다.")
#         for i in range(1,10):
#             print(str(x) + "x" + str(i) + "=" + str(x*i))
#         print("구구단 몇 단을 계산할까요(1~9)?")
# print("구구단 게임을 종료합니다.")

# ------------------------------------------------
'''
kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
midterm_score = [kor_score,math_score,eng_score]

student_score = [0,0,0,0,0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else:
    a,b,c,d,e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)
'''
# ------------------------------------------------

# def addition(x, y):
#     return x + y

# def multiplication(x, y):
#     return x * y

# def divided_by_2(x):
#     return x / 2

# if __name__=='__main__':
#     print(addition(10,5))
#     print(multiplication(10,5))
#     print(divided_by_2(50))

# ------------------------------------------------
'''
def addition(x, y):
    return x + y

def divided_by_2(x):
    return x / 2

def main():
    base_line = float(input("밑변의 길이는?"))
    upper_edge = float(input("윗변의 길이는?"))
    height = float(input("높이는?"))

    print("넓이는:",divided_by_2(addition(base_line,upper_edge)*height))

if __name__=='__main__':
    main()
'''
# ------------------------------------------------

# test = '5'
# for i in range(int(test)):
#     print('test')

# ------------------------------------------------

# my_list = ['i','like','studying','python']
# new_list = []
# i = len(my_list)
# if i == 4:
#     new_list.append(my_list[::2])
# print(new_list)

# ------------------------------------------------

# num = [1,2,3,4,5,6]
# total = 1
# for n in num:
    # total * total

# ------------------------------------------------

# a = int(input('자연수 a를 입력하세요 : '))
# if type(a/10) == int:
#     print('a는 10의 배수 입니다.')
# else :
#     print('a는 10의 배수가 아닙니다.')
# b = int(input('정수 b를 입력하세요. : '))
# if (0-b) < 0:
#     print('b는 양수입니다.')
# else :
#     print('b는 음수 입니다.')


# ------------------------------------------------

# numbers = ['10','11','12','13','14','15','16','17']
# total=0
# for number in numbers:
#     if int(number) % 5 == 0:
#         total += int(number)
#     else :
#         total += 10
# print(total)
# ------------------------------------------------
'''
money = 1500
snack = 500
water = 1000
while money != 0:
    if money > 1000:
        money -= water
    elif 0 < money <= 1000:
        money -= snack*2
    else:
        money = money + 500
print(money)
'''
# ------------------------------------------------
# if 4 == '4':
#  print(True)
# else:
#  print(False)

# ------------------------------------------------
'''
list_data_a = [1,2]
list_data_b = [3,4]

for i in list_data_a:
    for j in list_data_b:
        result = i + j
print(result)
'''
# ------------------------------------------------
'''
list_1 = [[1,2],[3],[4,5,6]]
a,b,c = list_1
list_2 = a + b + c

print(list_2)
'''
# ------------------------------------------------
