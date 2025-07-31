# a = "abcde"
# print(a[0],a[4])
# print(a[-1],a[-5])
# ------------------------------------------------

# a = "TEAMLAB MOOC, AWESOME Python"
# print(a[0:6],"AND",a[-9:])
# print(a[:])
# print(a[-50:50])
# print(a[::2],"AND",a[::-1])

# ------------------------------------------------

# a = "TEAM"
# b = "LAB"
# print(a + " " + b)
# print(a * 2 + " " + b * 2)

# if 'A' in a: print(a)
# else : print(b)

# ------------------------------------------------

# int_value = 2
# print("결과는" + int_value)

# ------------------------------------------------

# title = "TEAMLAB X Inflearn"
# title.upper() # 모두 대문자로 변환
# title.lower() # 모두 소문자로 변환

# ------------------------------------------------

# title = "TEAMLAB X Inflearn"
# title.title()
# title.capitalize()

# ------------------------------------------------

# title = "TEAMLAB X Inflearn"
# title.count('a')
# title.upper().count('a') # 변수의 문자열을 대문자로 변환 후 a 갯수를 반환
# title.isdigit() # 변수의 문자열이 숫자인지 여부를 반환
# title.startswith('a') # 변수의 문자열이 a 로 시작하는지 여부 반환

# ------------------------------------------------

# a = "It\'s OK"
# print(a)

# ------------------------------------------------

# f = open("메모장(파이썬프로그래밍 서적 연습)/yesterday.txt",'r')
# yesterday_lyric = f.readlines()
# f.close()

# contents = ""
# for line in yesterday_lyric:
#     contents = contents + line.strip() + "\n"

# n_of_yesterday = contents.upper().count('YESTERDAY')
# print('Number of a Word Yesterday :', n_of_yesterday)

# ------------------------------------------------

# print(1,2,3)
# print("a"+" "+"b"+" "+"c")
# print("%d %d %d" %(1,2,3))
# print("{} {} {}".format(1,2,3))

# ------------------------------------------------

# print("%s %s" %('one','two'))
# print("%d %d" %(1,2))

# ------------------------------------------------

# print("I eat %d apples" % 3)
# print("I eat %s apples" % "five")

# ------------------------------------------------

# print("Product : %s, Price per unit : %f." % ("Apples",5.243))

# ------------------------------------------------

# number = 3
# day = "three"
# print("I ate %d apples. I was sick for %s days." % (number,day))

# ------------------------------------------------

# print("I'm {0} years old.".format(20))

# ------------------------------------------------

# age = 40; name = 'Sungchul Choi'
# print("I'm {0}years old.".format(age))
# print("My name is {0} and {1} years old.".format(name,age))
# print("Product : {0}, Price per unit : {1:.2f}.".format("Apples",5.243))

# ------------------------------------------------

# print("%10d" %12)
# print("%-10d" %12)

# ------------------------------------------------

# print("%10.3f" % 5.94343)
# print("%10.2f" % 5.94343)
# print("%-10.2f" % 5.94343)

# ------------------------------------------------

# print("{0:>10s}".format("Apples"))
# print("{0:<10s}".format("Apples"))

# ------------------------------------------------

# print("{1:>10.5f}".format("Apples",5.243))
# print("{1:<10.5f}".format("Apples",5.243))

# ------------------------------------------------

# print("Product : %(name)5s Per price unit : %(price)5.5f" % {"name":"Apples","price":5.243})
# print("Product : {name:>5s} Per price unit : {price:5.5f}".format(name = "Apple",price = 5.243))

# ------------------------------------------------

# s = "hello"
# t = "my Python"

# print(s + "!" + t[2:])

# ------------------------------------------------

# value_1 = '5'
# value_2 = '5 - 2 - 10 - 10'.split('-')[-1]

# print(int(value_1) * 3 + float(value_2))

# ------------------------------------------------

# print("H-e-l-l-o-P-y-t-h-o-n"[::2])

# ------------------------------------------------

# course_name = 'This is New AI World'

# for i in course_name:
#     if i=='world':
#         i = course_name.lower()

# print(course_name)

# ------------------------------------------------

# number = 10
# day = 3
# print("I eat %d oranges every day." % number)

# ------------------------------------------------

# sentence = "Hello, my name is python?!"
# print(sentence[0]+sentence[5]+sentence[8:11])

# ------------------------------------------------

# first_word = "Python"
# second_word = "Language"
# print((first_word + second_word).capitalize())
# print(first_word.find("p"))
# print(second_word.isdigit())

# ------------------------------------------------

# sentence = 'Life Is Short You Need Python'
# a = sentence[-15:20]
# b = sentence.lower()
# c = sentence[:20]
# d = sentence[0:]
# e = sentence[:-1]

# print(d)

# ------------------------------------------------

# a = 10
# b = 20
# sum_result = f'a + b = {a + b}'
# print(sum_result)

# ------------------------------------------------

# word = 'word'
# print(f'|{word:<10}|')
# print(f'|{word:^10}|')
# print(f'|{word:>10}|')

# ------------------------------------------------

# name = "Hanbit"
# a = name.find("H")
# b = name.count("H") * 8
# c = len(name) * 2 + 3

# print("REMEMBER",str(a)+str(b)+str(c))

# ------------------------------------------------

# count = 0
# for i in range(10):
#     for j in range(0,i):
#         print("*",end='')
#         count = count + 1
#     print()


count = 1
for i in range(1,10,2):
    for j in range(0,i):
        print("*", end='')         
        count = count + 1
    print()