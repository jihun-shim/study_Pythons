a=10
print(a)

b="안녕~파이썬"
print(b)

print('헬로우')

""" 여러줄 주석 """
''' 여러줄 주석 '''
# 한 줄 주석

c = 10

print("헬로우")
print('헬로우')
# 단어는 '' "" 에 항상 입력
a=5
b=2

print(a + b )
print(a - b )
print(a * b )
print(a / b )
print(a // b)
print(a % b )
print(a ** b)

msg = '오늘도 행복도 하다'
'''오
오늘
늘도
행복
오도행
다'''
print(msg[0])
print(msg[:2])
print(msg[1:6])
print(msg[0:6:2])
print(msg[-1])
print(msg[:])

now='2020-02-22 : 12:05:12'
print(now[0:4],'년',now[5:7],'월',now[8:10],'일')

msg = "우리는 독도를 지킨다"

print(msg.replace('독도',"대한민국"))
print(msg.split())
print(msg.split())

msg='{}님 오늘도 행복하세요~'
print(msg.format('홍동우'))
msg='{1}님 오늘도 행복하세요~{0}(으)로 부터'
print(msg.format('대한민국','홍동우'))


name = '홍길동'
age = 22
height = 170.456

print('%s님은 %d세이고 , 신장은 %10.3f cm 입니다.' %(name,age,height))

arr = [1,2,3,4,5]
arr.append(10)
print(arr)
arr.append('hello')
print(arr)
print(arr[0])
print(arr[-2])
print(arr[-1].upper())
print(arr[6][0])

#           append()    : 요소 추가
#           sort()      : 리스트 정렬
#           reverse()   : 역순으로 뒤집기
#           index()     : 위치 반환
#           insert()    : 리스트에 요소 삽입
#           remove()    : 요소 제거
#           pop()       : 맨 마지막 요소를 꺼내기
#           count()     : 요소 개수 세기
#           extend()    : 리스트에 리스트를 더하기\
#           clear()     : 모든 요소를 제거


"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록을 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""
"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]        True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                      False
        숫자형       0이아닌 숫자     True ***
                    0                      False
                    None                   False

"""