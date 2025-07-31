# ------------------------------------------------
# def f(x,y):
#     return x + y

# print(f(1,4))

# f = lambda x, y : x + y
# print(f(1,4))

# ------------------------------------------------

# print((lambda x: x + 1)(5))

# ------------------------------------------------

# f = lambda x, y : x + y
# print(f(1,4))

# def f(x,y):
#     return x + y
# print(f(1,4))

# f = lambda x : x ** 2
# print(f(3))

# def f(x):
#     return x**2
# print(f(3))

# f = lambda x : x / 2
# print(f(3))
# print(f(3,5)) # 매개변수의 차이로 인한 오류

# def f(x):
#     return x / 2
# print(f(3))

# ------------------------------------------------

# ex = [1,2,3,4,5]
# # f = lambda x : x ** 2

# def f(x):
#     i = x**2
#     return i 

# print(list(map(f,ex)))

# ------------------------------------------------

# ex = [1,2,3,4,5]

# f = lambda x : x ** 2
# for value in map(f,ex):
#     print(value)

# def f(x):
#     i = x ** 2
#     return i

# for value in map(f,ex):
#     print(value)

# ------------------------------------------------

# ex = [1,2,3,4,5]
# print([x ** 2 for x in ex])

# result = []
# for x in ex:
#     result.append(x**2)
# print(result)

# ------------------------------------------------

# ex = [1,2,3,4,5]
# f = lambda x, y : x + y
# print(list(map(f,ex,ex)))

# def f(x,y):
#     i = x + y
#     return i

# print(list(map(f,ex,ex)))

# ------------------------------------------------

# print([x+y for x,y in zip(ex,ex)])

# result = []
# for x,y in zip(ex,ex):
#     i = x + y
#     result.append(i)

# print(result)

# ------------------------------------------------

# ex = [1,2,3,4,5]
# print(list(map(lambda x : x ** 2 if x % 2 == 0 else x, ex)))

# def f(x):
#     if x % 2 == 0:
#         return x**2
#     else:
#         return x

# print(list(map(f,ex)))


# print([x ** 2 if x % 2 == 0 else x for x in ex])

# result = []
# for x in ex:
#     if x % 2 == 0:
#         result.append(x**2)
#     else:
#         result.append(x)
# print(result)

# ------------------------------------------------

from functools import reduce
print(reduce(lambda x, y : x + y,[1,2,3,4,5]))

def f(x,y):
   i = x + y
   return i

print(reduce(f,[1,2,3,4,5]))

ex = [1,2,3,4,5]
y = 0
for i in ex:
   y += i
print(y)

x = 0
for y in [1,2,3,4,5]:
   x += y
print(x)
# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
