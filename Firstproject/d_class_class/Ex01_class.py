"""
     1) 클래스 기초 : 객체화(인스턴스) 하기위한 틀이되는 요소

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
     ` 대문자로 생성
"""
'''
class Sample:
    # 데이터 초기화 할 떄 반드시 생성자(함수)를 만들어야 한다. 기본 생성자와 소멸자는 내장 되어있다
    def __init__(self): # 자신의 클래스명 = self
        self.age = 24
        self.name = '홍동우'
        print('__init__호출됨')
    # 소멸자(함수)
    def __del__(self):
        self.age = 0
        self.name = ''
        print('__del__호출됨')

s = Sample() #객체화
print(s.age)
print(s.name)
print(dir(s))
'''


"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
    static  함수 :  클래스명 접근을 하며 객체끼리의 공유하고자 하는 메소드
    
    - 클래스 함수와 print(s.name)스태틱 함수는 둘 다 클래스명 접근
    - 클래스 함수는 cls를 이용하여 객체를 이용할 수 있다

"""
'''
s.name = '박길동'
print(s.name)
print('--------------------')
b = Sample()
print(b.name)
'''

class Book:
    cnt = 0

    def __init__(self, title): # 값을 초기화하면서 객체화를 하고 싶다면 정의가 필요(오버로딩 overloading)
        self.title = title

    def output(self):
        print('제목 : ' , self.title)
        self.cnt +=1
        print('총 개수 : ', self.cnt)

    @classmethod
    def output2(cls):
        cls.cnt += 1
        print('총 개수 : ', cls.cnt)

    @staticmethod # 다른 언어처럼 만들었지만 불편해서 다시 @classmeth 만든 느낌?
    def ouput3():
        pass


# b0 = Book()
# b0.output()
#
# b1 = Book('어린왕자')
# b1.output()
#
# b2 = Book('노인과 바다')
# b2.output()

b1 = Book('어린왕자')
b1.output2()

b2 = Book('노인과 바다')
b2.output2()


'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''

class Animal:
    def move(self):
        print('동물은 움직인다')
    def ex(self):
        print('부모 함수')


class Wolf(Animal):
    def move(self):
        print('늑대는 4발로 달린다')

w = Wolf() #객체화 (인스턴스화)
w.move()
w.ex()

# Human 인간은 두발로 걷습니다.

class Human:
    def move(self):
        print('인간은 2발로 걷는다.')

h = Human()
h.move()

class WolfHuman(Wolf, Human):
    def move(self):
        super().move() # super() : 부모클래스명 (부모 메소드(함수)가 호출되게 하려면)
        print('늑대인간은 2발로 빨리 달린다.')

w = WolfHuman()
w.move()



