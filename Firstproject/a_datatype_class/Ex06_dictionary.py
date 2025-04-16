"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt)
print(dt[1]) #1은 키값이고 인덱스가 아님
print(dt['3'])

dt = {1:'one', 2:'two', '3':'three', 1:'first'} # 키값이 같다면 값은 덮어씀
print(dt)

dt = {1:'one', 2:'two', '3':'three', 3:'삼'}
print(dt['3'])
dt['3'] = '차차차'
print(dt)

# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}
print(dt2[3,4])

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
dt2['korea'] = 'seoul' #사전에 추가
print(dt2)
dt2['korea'] = '한국'
print(dt2)

# 여러개 추가할 때
dt2.update({ 5: 'kim', (0,4): 'hong'})
print(dt2)

#dict() 함수로 딕셔너리 생성
dt3 = dict(ten='ten',one='one') #dict()함수를 이용할때 숫자형이 키가 될 수 없다.
print(dt3)

print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt2[5])     #없는 키를 입력하면 예외발생
print(dt2.get(7)) #None : 키가 없는 경우
print(dt2.get(7,'없음'))
print()


# Key와 Value만 따로 검색
print(dt2.keys())
print(dt2.values())
print(dt2.items())
