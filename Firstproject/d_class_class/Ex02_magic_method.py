"""
    매직 메소드

(1) Binary Operators
        Operator	Method
        +	    object.__add__(self, other)
        -	    object.__sub__(self, other)
        *	    object.__mul__(self, other)
        //	    object.__floordiv__(self, other)
        /	    object.__div__(self, other)
        %	    object.__mod__(self, other)
        **	    object.__pow__(self, other[, modulo])
        >>	    object.__lshift__(self, other)
        <<	    object.__rshift__(self, other)
        &	    object.__and__(self, other)
        ^	    object.__xor__(self, other)
        |	    object.__or__(self, other)  
        
(2) Comparison Operators
        Operator	Method
        <	    object.__lt__(self, other)
        <=	    object.__le__(self, other)
        ==	    object.__eq__(self, other)
        !=	    object.__ne__(self, other)
        >=	    object.__ge__(self, other)
        >	    object.__gt__(self, other)
                
(3) Extended Assignments
        Operator	Method
        +=	    object.__iadd__(self, other)
        -=	    object.__isub__(self, other)
        *=	    object.__imul__(self, other)
        /=	    object.__idiv__(self, other)
        //=	object.__ifloordiv__(self, other)
        %=	    object.__imod__(self, other)
        **=	object.__ipow__(self, other[, modulo])
        <<=	object.__ilshift__(self, other)
        >>=	object.__irshift__(self, other)
        &=	    object.__iand__(self, other)
        ^=	    object.__ixor__(self, other)
        |=	    object.__ior__(self, other)
          
(4) Unary Operators
        Operator	Method
        -	        object.__neg__(self)
        +	        object.__pos__(self)
        abs()	    object.__abs__(self)
        ~	        object.__invert__(self)
        complex()	object.__complex__(self)
        int()	    object.__int__(self)
        long()	    object.__long__(self)
        float()	object.__float__(self)
        oct()	    object.__oct__(self)        
        hex()	    object.__hex__(self)
"""
class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ('이름 : {} \n나이 : {} \n'.format(self.name, self.age))

    def __add__(self, other):
        self.age += other

    def __ge__(self, other):
        if self.age > other:
            return '성인입니다'
        else:
            return '미성년입니다'

    def __bool__(self):
        if self.name == '홍동우' :
            return True
        else:
            return False



s = Sample('홍길동',21)
print(s) #문자열로 반환하는 경우 __str()__가 자동 호출

s + 10
print(s)

print(s >= 20) # 나이가 20이상이면 성인입니다. 그외는 미성년입니다.

# __bool__ 메소드가 없는 상태에서
if s:
    print('홍동우 본인입니다.')
else:
    print('홍동우 본인이 아닙니다.')