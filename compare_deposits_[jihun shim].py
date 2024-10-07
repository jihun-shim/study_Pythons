# - refer : 예금상품비교
# - 예금 원금 따른 이자율 차이 (기간 33개월, 3개월 계산)
# - 변수 기준
#  + deposit_my_list = [4500000, 9800000]
#  + bank_rate_year = [0.024, 0.036, 0.042]
#  + bank_tax_interest_rate = [0, 0.154, 0.154]
# - Option : 어려운 경우 각 변수 값 아래 사용
#  + deposit_my_list = 4500000
#  + bank_rate_year = [0.024, 0.036]
#  + bank_tax_interest_rate = [0, 0.154]

deposit_my_list = [4500000,9800000]
bank_rate_year = [0.024, 0.036, 0.042]
bank_tax_interest_rate = [0, 0.154]


p = deposit_my_list
r = bank_rate_year
tax = bank_tax_interest_rate

#단리 = p* (1+(r*t)*(1-tax))

print('-원금 450만원 연 이자율 2.4% 적용 결과-')
print()
for t in range(3,34,3):
    a = p[0] * ( 1 + ( r[0]/12 * t ) * ( 1 - tax[0] ) ) 
    b = p[0] * ( 1 + ( r[0]/12 * t ) * ( 1 - tax[1] ) )
    print('세율 0% 적용 :', int(a), '원')
    print('세율 15.4% 적용 :', int(b), '원')
    print() 

print('-'*50)

print('-원금 450만원 연 이자율 3.6% 적용 결과-')
print() 
for t in range(3,34,3):
     c = p[0] * ( 1 + ( r[1]/12 * t ) * ( 1 - tax[0] ) ) 
     d = p[0] * ( 1 + ( r[1]/12 * t ) * ( 1 - tax[1] ) ) 
     print('세율 0% 적용 :', int(c),'원') 
     print('세율 15.4% 적용 :', int(d), '원')
     print()

print('-'*50)

print('-원금 450만원 연 이자율 4.2% 적용 결과-')
print() 
for t in range(3,34,3):
     e = p[0] * ( 1 + ( r[2]/12 * t ) * ( 1 - tax[0] ) ) 
     f = p[0] * ( 1 + ( r[2]/12 * t ) * ( 1 - tax[1] ) ) 
     print('세율 0% 적용 :', int(e),'원') 
     print('세율 15.4% 적용 :', int(f), '원')
     print()

print('-원금 980만원 연 이자율 2.4% 적용 결과-')
print()
for t in range(3,34,3):
    g = p[1] * ( 1 + ( r[0]/12 * t ) * ( 1 - tax[0] ) ) 
    h = p[1] * ( 1 + ( r[0]/12 * t ) * ( 1 - tax[1] ) )
    print('세율 0% 적용 :', int(g), '원')
    print('세율 15.4% 적용 :', int(h), '원')
    print() 

print('-'*50)

print('-원금 980만원 연 이자율 3.6% 적용 결과-')
print() 
for t in range(3,34,3):
     c = p[1] * ( 1 + ( r[1]/12 * t ) * ( 1 - tax[0] ) ) 
     d = p[1] * ( 1 + ( r[1]/12 * t ) * ( 1 - tax[1] ) ) 
     print('세율 0% 적용 :', int(c),'원') 
     print('세율 15.4% 적용 :', int(d), '원')
     print()

print('-'*50)

print('-원금 980만원 연 이자율 4.2% 적용 결과-')
print() 
for t in range(3,34,3):
     e = p[1] * ( 1 + ( r[2]/12 * t ) * ( 1 - tax[0] ) ) 
     f = p[1] * ( 1 + ( r[2]/12 * t ) * ( 1 - tax[1] ) ) 
     print('세율 0% 적용 :', int(e),'원') 
     print('세율 15.4% 적용 :', int(f), '원')
     print()