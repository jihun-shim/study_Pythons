# def calculate_rectangle_area(x,y):
#     return x * y

# rectangle_x = 10
# rectangle_y = 20
# print("사각형 x의 길이", rectangle_x ,'cm')
# print("사각형 x의 길이", rectangle_y ,'cm')

# print("사각형의 넓이:", calculate_rectangle_area(rectangle_x,rectangle_y),'cm²')
# ------------------------------------------------

# def f(x):
#     return 2*x + 7

# def g(x):
#     return x**2

# x = 2 
# print(f(x) + g(x) + f(g(x)) + g(f(x))) 

# ------------------------------------------------

# def a_rectangle_area():
#     print(5*7)
# def b_rectangle_area(x,y):
#     print(x*y)
# def c_rectangle_area():
#     return (5*7)
# def d_rectangle_area(x,y):
#     return (x*y)

# a_rectangle_area()
# b_rectangle_area(5,7)
# print(c_rectangle_area())
# print(d_rectangle_area(5,7))

# ------------------------------------------------

# def f(x):
#     y=x
#     x=5
#     return y*y

# x = 3
# print(f(x))
# print(x)

# ------------------------------------------------

# def spam(eggs):
#     eggs.append(1)
#     eggs = [2,3]

# ham = [0]
# spam(ham)
# print(ham)

# ------------------------------------------------

# def test(t):
#     print(x)
#     t = 20
#     print("In Function:", t)

# x = 10
# test(x)
# print("In Main:", x)
# print("In Main:", t)
# ------------------------------------------------

# def f():
#     s = "I love London"
#     print(s)

# s = "I love Paris"
# f()
# print(s)

# ------------------------------------------------

# def f():
#     global s
#     s = "I love London"
#     print(s)

# s = "I love Paris"
# f()
# print(s)

# ------------------------------------------------

# def calculate(x,y):
#     total = x + y
#     print("In Function")
#     print("a:",str(a), "b:",str(b), "a+b:",str(a+b), "total:",str(total))
#     return total

# a = 5
# b = 7
# total = 0
# print("In Program - 1")
# print("a:",str(a),"b",str(b),"a+b:",str(a+b))

# sum = calculate(a,b)
# print("After Calculate")
# print("Total:",str(total),"Sum:",str(sum))

# ------------------------------------------------

# def factorial(n):
#     if n == 1:
#         return 1
#     else :
#         return n * factorial(n-1)

# print(factorial(int(input('Input your number for Factorial Calculation :'))))

# ------------------------------------------------
# 키워드 인수
# def print_something(my_name, your_name):
#     print("Hello {0} My_name is {1}".format(your_name,my_name))

# print_something("Sungchul","TEAMLAB")
# print_something(your_name = "TEMALAB", my_name="Sungchul")

# ------------------------------------------------
# 디폴트 인수
# def print_something_2(my_name,your_name="TEAMLAB"):
#     print("Hello {0} My name is {1}".format(your_name, my_name))

# print_something_2("Sungchul","TEAMLAB")
# print_something_2("Sungchul")

# ------------------------------------------------

# 가변 인수
# def asterisk_test(a, b, *args):
#     return a + b + sum(args)

# print(asterisk_test(1,2,3,4,5))

# def asterisk_test(a,b,*args):
    # print(args)

# print(asterisk_test(1,2,3,4,5))

# def asterisk_test_2(*args):
#     x, y, *z = args
#     return x, y, z

# print(asterisk_test_2(3,4,5))

# def asterisk_test_2(*args):
#     x, y, *z = args
#     return x, y, z

# print(asterisk_test_2(3,4,5,10,20,30))
# ------------------------------------------------

# 키워드 가변인수
# def kwargs_test(**kwargs):
#     print(kwargs)
#     print("First value is {first}".format(**kwargs))
#     print("Second value is {second}".format(**kwargs))
#     print("Third value is {third}".format(**kwargs))

# kwargs_test(first = 3, second = 2, third = 1)

# ------------------------------------------------

# def kwargs_test (one, two, *args, **kwargs):
#     print(one + two + sum(args))
#     print(kwargs)

# kwargs_test(3, 4, 5, 6, 7, 8, 9, first = 3, second = 4, third = 5)

# ------------------------------------------------

# a = 5
# if (a > 3):
#     print("Hello World")
#     print("Hello TEAMLAB")

# if (a > 4):
#     print("Hello World")
#     print("Hello TEAMLAB")

# if (a > 5):
#     print("Hello World")
#     print("Hello TEAMLAB")

# def print_hello():
#     print("Hello World")
#     print("Hello TEAMLAB")

# a = 5
# if (a > 3):
#     print_hello()
# if (a > 4):
#     print_hello()
# if (a > 5):
#     print_hello()

# ------------------------------------------------

# import math
# a = 1; b = -2; c = 1

# print((-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
# print((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))

# def qudratic_equation(a,b,c):
#     print((-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
#     print((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))

# qudratic_equation(a = 1, b = -2, c = 1)

# def get_result_qudratic_equation(a, b, c):
#     values = []
#     values.append((-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
#     values.append((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
#     return values

# print(get_result_qudratic_equation(a = 1, b = -2, c = 1))

# ------------------------------------------------

# 연습문제

# def test(k):
#     print("Input is", k)

# k = 100
# test(k)

# def counter(*args):
#     count = len(args)
#     return count

# print(counter(["test","hello","oooo"]))

# def f(x):
#     y = x
#     x = 7
#     return y * x

# x = 4
# print(f(3))
# print(x)

# def print_hi():
#     print("Hi")

# name = 'jiho'
# def call_my_name():
#     print(name)
#     name = 'sehoon'

# call_my_name()

# country = ["Korea","Japan","China"]
# country.append("Remove")
# print(country.remove("Remove"))

# def say_myself(name, old, woman=True):
#     print("나의 이름은 %s 입니다." %name)
#     print("나이는 %d 살입니다." %old)
#     if woman:
#         print("여자입니다.")
#     else:
#         print("남자입니다.")

# say_myself("최주영", 20)

# def exam_func():
#     x = 10
#     print("Value:", x)

# x = 20
# exam_func()
# print("Value:", x)

# def get_abbr(data_list):
#     result = []

#     for x in data_list:
#         result.append(x[:3])
    
#     return result

# print(get_abbr(['Seoul','Anyang','Incheon','Jeju']))

# test_data = 3
# def hi(a):
#     b = a*3
#     return b

# print(hi(test_data))

# new_list=[]
# def sotring_function(list_value):
#     new_list = list_value.sort()
#     new_list.append()
#     return new_list

# sotring_function([5,4,3,2,1])
# print(new_list)

# def sotring_function(list_value):
#     list_value.sort()
#     return list_value

# print(sotring_function([5,4,3,2,1]))
'''
def sotring_function(list_value):
    list_value.sort()
    print(list_value)

sotring_function([5,4,3,2,1])
'''

# a = 111
# b = 222

# def function_1():
#     print(a)
#     print(b)

# def function_2():
#     a = 333
#     print(b)
#     print(a)

# function_1()
# function_2()

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
