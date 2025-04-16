# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다 ***


s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)

s1={3,4,5,6}        #set 생성
print(s1)

print(s.intersection(s1))   #교집합
print(s & s1)
print(s.union(s1))          #합집합
print(s | s1)
print(s-s1)                #차집합



