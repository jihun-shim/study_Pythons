# a = [1,2,3,4,5]
# a.append(10)
# print(a)
# a = [1,2,3,4,5,10]
# a.append(20)
# print(a) 
# print(a.pop())
# print(a.pop())
# print(a)

# ------------------------------------------------

# word = input("Input a word : ")
# world_list = list(word)
# print(world_list)

# result = []
# for _ in range(len(world_list)):
#     result.append(world_list.pop())

# print(result)
# print(word[::-1])

# ------------------------------------------------

# a = [1,2,3,4,5]
# a.append(10)
# a.append(20)
# print(a.pop(0))
# print(a.pop(0))
# print(a)

# ------------------------------------------------

# s = set([1,2,3,1,2,3])
# print(s)

# s.add(1)
# print(s)

# s.remove(1)
# print(s)

# s.update([1,4,5,6,7])
# print(s)

# s.discard(3)
# print(s)

# s.clear()
# print(s)

# ------------------------------------------------

# s1 = set([1,2,3,4,5])
# s2 = set([3,4,5,6,7])

# print(s1.union(s2)) # s1과 s2의 합집합
# print(s1 | s2)

# print(s1.intersection(s2)) # s1과 s2의 교집합
# print(s1 & s2)

# print(s1.difference(s2)) # s1과 s2의 차집합
# print(s1 - s2)

# ------------------------------------------------

# student_info = {20140012:'Sungchul', 20140059:'Jiyong', 20140058:'Jaehong'}
# print(student_info)
# print(student_info[20140012])

# student_info[20140039] = 'Wonchul'
# print(student_info)

# ------------------------------------------------

# country_code = {}
# country_code = {"America":1, "Korea":82, "China":86, "Japan":81}
# print(country_code)

# print(country_code.keys()) # 키만 보고 싶을때

# country_code["German"] = 49
# print(country_code.values()) # 값만 보고 싶을때

# print(country_code.items()) # 키와 값쌍 모두 보여주기

# for k,v in country_code.items():
#     print("Key :", k)
#     print("Value :", v)

# print("Korea" in country_code.keys())
# print(82 in country_code.values())
# ------------------------------------------------

# deque 모듈

# from collections import deque

# deque_list = deque()
# for i in range(5):
#     deque_list.append(i)

# print(deque_list)

# print(deque_list.pop())
# print(deque_list.pop())
# print(deque_list.pop())
# print(deque_list.pop())
# print(deque_list)

# ------------------------------------------------

# from collections import deque
# deque_list = deque()
# for i in range(5):
#     deque_list.appendleft(i)

# print(deque_list)

# ------------------------------------------------

# from collections import deque

# deque_list = deque()
# for i in range(5):
#     deque_list.append(i)

# print(deque_list)
# deque_list.rotate(2)
# print(deque_list)
# deque_list.rotate(2)
# print(deque_list)

# print(deque(reversed(deque_list)))

# deque_list.extend([5,6,7])
# print(deque_list)
# deque_list.extendleft([5,6,7])
# print(deque_list)
# ------------------------------------------------

# OrderedDict 모듈

# d = {}
# d['x'] = 100
# d['l'] = 500
# d['y'] = 200
# d['z'] = 300

# for k,v in d.items():
#     print(k,v)

# ------------------------------------------------

# from collections import OrderedDict

# d = OrderedDict()
# d['x'] = 100
# d['l'] = 500
# d['y'] = 200
# d['z'] = 300

# for k,v in d.items():
#     print(k,v)

# ------------------------------------------------

# def sort_by_key(t):
#     return t[0]

# from collections import OrderedDict

# d = dict()
# d['x'] = 100
# d['y'] = 200
# d['z'] = 300
# d['l'] = 500

# for k, v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
#     print(k,v)

# ------------------------------------------------

# defaultdict 모듈

# d = dict()
# print(d["first"])

# from collections import defaultdict

# d = defaultdict(lambda : 0)
# print(d["first"])

# ------------------------------------------------

# from collections import defaultdict

# s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
# d = defaultdict(list)

# for k,v in s:
#     d[k].append(v)

# print(d.items())

# ------------------------------------------------

# Counter 모듈

# from collections import Counter

# text = list("gallahad")
# print(text)

# c = Counter(text)
# print(c)

# print(c["a"])

# ------------------------------------------------

# from collections import Counter

# text = """A press release is the quickest and easiest way to get free
# publicity. If well written, a press release can result in multiple published
# articles about your firm and its products. And that can mean new prospects
# contacting you asking you to sell to them. ···""".lower().split()  #

# print(Counter(text))

# ------------------------------------------------

# from collections import Counter

# c = Counter({'red' : 4, 'blue' : 2}) # 딕셔너리 형태의 매개변수 
# print(c)
# print(list(c.elements()))

# ------------------------------------------------

# from collections import Counter

# c = Counter(cats = 4, dogs = 8) # 키워드 형태의 매개변수
# print(c)
# print(list(c.elements()))

# ------------------------------------------------

# from collections import Counter

# c = Counter( a = 4, b = 2, c = 0, d = -2) # 사칙연산
# d = Counter( a = 1, b = 2, c = 3, d = 4)

# c.subtract(d)
# print(c)

# ------------------------------------------------

# from collections import Counter

# c = Counter( a = 4, b = 2, c = 0, d = -2)
# d = Counter( a = 1, b = 2, c = 3, d = 4)
# print(c + d) # 덧셈
# print(c & d) # 교집합
# print(c | d) # 합집합 * 값이 큰 것으로 대체

# ------------------------------------------------

# from collections import namedtuple

# Point = namedtuple('Point',['x','y']) # namedtuple 모듈
# p = Point(11, y = 22)
# print(p)
# print(p.x,p.y)
# print(p[0]+p[1])

# ------------------------------------------------

# from collections import defaultdict
# from collections import OrderedDict

# text = """A press release is the quickest and easiest way to get free publicity. If well
# written, a press release can result in multiple published articles about your
# firm and its products. And that can mean new prospects contacting you asking
# you to sell to them. ···""".lower().split()

# # 1. 문장의 단어 개수를 파악하는 코드를 작성한다.
# # 2. defaultdict 모듈을 사용한다.
# # 3. 단어의 출현 횟수를 기준으로 정렬된 결과를 보여주기 위해 OrderedDict 모듈을 사용한다.

# word_count = defaultdict(lambda:0)
# for word in text:
#     word_count[word]+=1
# print(word_count)
# d = word_count

# for k,v in OrderedDict(sorted(d.items(), key=lambda t:t[1], reverse=True)).items():
#     print(k,v)

# ------------------------------------------------

# scroe_dic = {'Kim' : 80, 'Lee' : 85, 'Ahn' : 83, 'Choi' : 90}
# first_key = list(scroe_dic.keys())[0]
# scroe_dic[first_key] = 90
# print(scroe_dic.values())

# ------------------------------------------------

# from collections import deque

# deque_list = deque(['a','b','c'])

# print(deque_list)

# ------------------------------------------------

# from collections import Counter

# text = 'Hello, this is python world'
# c = Counter(text)
# print(c['l'])

# ------------------------------------------------

# dictionary = {"a":1, "b":2, "c":3}
# dictionary.setdefault('b',4)
# dictionary.setdefault('d',5)
# dictionary["c"] = dictionary["d"]
# dictionary["b"] = dictionary["c"]
# dictionary["d"] = dictionary["b"]
# print(dictionary)

# ------------------------------------------------

# box = [1,'red',3,(),[],None]
# print(len(box))

# ------------------------------------------------

# fruits = ('apple','banana','cherry','strawberry')
# fruits[0]='orange'
# print(fruits)

# ------------------------------------------------

# print(3**5)
# print(15%4)
# a = 4
# a -= 3
# print(a)

# a = {'prof.choi' : 'The best'}
# print(type(a))

# ------------------------------------------------

# def quiz_2(list_data):
#     a = set(list_data)
#     return (list(a)[1:5])

# list_1 = [0,3,1,7,5,0,5,8,0,4]

# print(quiz_2(list_1))

# ------------------------------------------------

# fruit_name = ('python korea',)
# print(type(fruit_name))

# ------------------------------------------------

# list_1 = [0,3,1,7,5,0,5,8,0,4]

# def quiz_2(list_data):
#     a = set(list_data)
#     return (list(a)[1:5])
# print(quiz_2(list_1))

# ------------------------------------------------

# country_code = {"America":1, "Korea":82, "China":86, "Japan":81}
# print(country_code.values())
# print(country_code)
# print(country_code.keys())
# print(85 in country_code.values())
# print("Korea" in country_code.keys())

# ------------------------------------------------

# a = ""
# midterm_set = set([1, 5, 7, 4, 3, 2, 1, 1, 2, 3])
# for i in midterm_set:
#     a = a + str(i)
# print(a)

# ------------------------------------------------

# def delete_a_list_element(list_data, element_value):
#     if element_value in list_data:
#         list_data.remove(element_value)
#         return list_data
#     else:
#         return "False"
    
# list_data = ['a', 1, 'gachon', '2016.0']
# element = float(2016)
# result = delete_a_list_element(list_data, element)
# print(result)

# ------------------------------------------------

# def add_number(original_list):
#     original_list += [1]
# mylist = [1,2,3,4]
# add_number(mylist)
# print(set(mylist))

# ------------------------------------------------

# a = [3, "apple", 2016, 4]
# b = a.pop(0)
# c = a.pop(1)
# print(b+c)

# ------------------------------------------------

# def week_seven(sentence1):
#     cells = set(sentence1.replace(' ','').lower())
#     return cells

# sentence_a = "The quick brown fox jumps over the lazy dog"
# sentence_b = "I love you"
# print(len(week_seven(sentence_a) - week_seven(sentence_b)))

# ------------------------------------------------

# tuple_1 = (1,2,3)
# tuple_2 = (4,5,6)

# def quiz_1(data_1, data_2):
#     result = []
#     for i in (tuple_1 + tuple_2):
#         result.append(i)

#     return (result)

# print(quiz_1(tuple_1,tuple_2))

# ------------------------------------------------

# dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}

# dict_keys = list(dict_1.keys())
# dict_values = list(dict_1.values())

# dict_2 = dict()

# for i in range(len(dict_keys)):
#     dict_2[dict_values[i]] = dict_keys[i]

# print(dict_2[2])

# ------------------------------------------------
