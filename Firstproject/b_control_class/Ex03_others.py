
str = 'HELLO'                # 문자열
li = ['a','b','c']        # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = dict(k=5, j=6)       # 딕셔너리

#(1)unpacking : 각 요소를 분해 (딕셔너리는 안됨)
c1, c2, c3 = li
print(c2)

for key,value in di. items():
    print(key, ' : ', value)

#(2) 리스트의 요소가 튜플인 경우(리스트 [] 튜플 ())
alist = [(1,2), (3,4), (5,6)]
for (first, second) in alist:
    print(first, "+", second, '=', first+second)

#(3) 여러 시퀀스 순회하기 : zip()
days = ['월','화','수']
doit = ['잠자기','공부','한잔','해장']
print(zip(days, doit)) # 하나의 객체로 생성만
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

for yoil, halil in zip(days, doit):
    print(yoil, halil)



