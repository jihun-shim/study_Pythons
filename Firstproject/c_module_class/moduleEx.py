from mypackage.mymodule import get_weather
import mypackage.exmodule as ex

today=get_weather()
print('오늘의 날씨는', today)

print(ex.sum(3,4))
print(ex.sum(3,4.5))
ex.sum(3,'z')

from mypackage.exmodule import sum as ex
print(ex(4,5))

from mypackage.package2.exmodule import get_date
today =get_date()
print('오늘은', today, '요일 입니다.')


def covert_c_to_f(celsius_value):
    return celsius_value * 9.0 / 5 + 32
    test_value = 0

import fah_converter as fah

print ("Enter a celsius value: ")
celsius = float(input())
fahrenheit = fah.covert_c_to_f(celsius)
print ("That's ", fahrenheit, " degrees Fahrenheit")

def sum_func(a, b):
    return a + b
def multiply_func(a,b):
    return a * b
def minus_func(a,b):
    return a -b
def devide_func(a,b):
    return a / b

import calculator

user_input = input("사칙연산 프로그램: ").split(" ")
first_val , second_val = int(user_input [0]), int(user_input [2])
fourcal = user_input[1]
if fourcal == "+":
    result = sum_func(first_val , second_val)
elif fourcal == "-":
    result = minus_func(first_val , second_val)
elif fourcal == "/":
    result =devide_func(first_val , second_val)
else:
    result =multiply_func(first_val , second_val)
print("실행 결과는", result)
