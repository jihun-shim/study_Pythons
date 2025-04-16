"""
    collections 모듈: 파이썬의 내장 모듈
    (1) deque : 스택과 큐를 모두 지원하는 모듈
    (2) OrderedDict : 순서를 가진 딕셔러니 객체
    (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
                  같은 이름의 키의 값을 하나로 만들 때 사용
    (4) Counter : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
    (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
"""

#-------------------------------------
# (1) deque : 스택과 큐를 모두 지원하는 모듈
#           - 리스트와 비슷한 형식으로 데이타를 저장한다.
#           - append() 함수로 기존 리스트처럼 데이터가 인덱스 번호와 저장된다

from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.pop() #스택구조
deque_list.pop()
print(deque_list)

deque_list.insert(1,100)
print(deque_list)

# -------------------------------------------
# (2) OrderedDict 모듈 : 순서를 가진 딕셔러니 객체
#                기본적인 딕셔너리는 순서를 보장하지 않는 객체이다

d = {} #기본 딕셔너리
d['x'] = 100
d['b'] = 200
d['h'] = 300
d['g'] = 400
for k, v in d.items():
    print(k, v)     #순서대로 나오는 듯 보이지만, 순서를 보장하지 않는다.

from collections import OrderedDict
d = OrderedDict()
d['x'] = 100
d['b'] = 200
d['h'] = 300
d['g'] = 400
for k, v in d.items():
    print(k, v)

#----------------------------------------------
# (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
#                   같은 이름의 키의 값을 하나로 만들 때 사용

# d=dict()
# print(d['first'])
# [에러발생] - 생성하지 않은 키를 호출

from collections import defaultdict
d = defaultdict(lambda : 0) #어떤키가 들어와도 초기값(value)으로 0으로 설정 (return 0)
print(d['first'])

s = [('yellow',1), ('blue',2),('yellow',5),('red',3),('blue',2)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items())


#---------------------------------------------------
# (4) Counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
from collections import Counter
text = list('goooooooood')
c = Counter(text)
print(c)

# 딕셔너리 형식을 초기값으로 하여 Counter를 생성
c = Counter({'yellow': 1, 'blue': 2})
print(c)
print(list(c.elements())) # 함수 : Ctrl + Q로 도움말 정보

#-------------------------------------------------
# (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
from collections import namedtuple
MyPoint = namedtuple('MyPoint', ['x','y'])
p = MyPoint(100,200)
print(p)
print(p.x, p.y)
print(p.x + p.y)