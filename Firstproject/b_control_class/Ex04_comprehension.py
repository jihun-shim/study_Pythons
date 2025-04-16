"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터(반복자)로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""

# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,6):
    alist.append(n)
print(alist)

alist = list(range(1,6))
print(alist)


#------------------------------------------------
#(1) 리스트 컴프리핸션
# blist = [1,2,3,4,5]


blist = [n for n in range(1,6)]
print(blist)

blist = [n-1 for n in range(1,6)]
print(blist)

blist = [n**2 for n in range(1,6)]
print(blist)

clist = [n for n in range(1,6) if n%2 == 1]
print(clist)

rows = range(1,4)
cols = range(1,3)
dlist = [(r,c) for r in rows for c in cols]
print(dlist)

for r, c in dlist:
    print(r,c)

#-------------------------------------------
# (2) 딕셔러니 컨프리핸션
a = {x : x**2 for x in (2,3,4)}
print(a)

word = 'LOVE LOV'
wcnt = {c:word.count(c) for c in word}
print(wcnt)

#------------------------------------------------
# (3) 셋 컨프리핸션
#1~5까지 홀수값으로 셋 생성
aset = { h for h in range(1,6) if h%2==1}
print(aset)

print()
data = [1,2,3,2,1,4,9]

# 리스트
dl=[q for q in data]
print(dl)

# 셋 (중복 안 됨)
sl={q for q in data}
print(sl)

# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
glist = (h for h in range(1,6) if h%2==1)
print(type(glist)) #튜플은 컨프리핸션이 없다
print(list(glist))

num= [ n-1 for n in range(1,12)]
print(num)


alist = []
alist.append('*'*5)
print(alist)

alist = []
for n in range(1,6):
    alist.append(n)
print(alist)

alist = list(range(1,6))
print(alist)



