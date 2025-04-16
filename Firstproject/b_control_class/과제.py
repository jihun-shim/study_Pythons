#(1)----------------------------------
even_filter = [1, 2, 4, 5, 8, 9, 10]
even_filter = {h for h in even_filter if h % 2 == 0}
print(even_filter)

#(2)----------------------------------얘는 도저히 감이 안와서 옆에 분들 참조 하였습니다 ...
def is_prime_number(n):
 if n < 2:
  return False
 for i in range(2, n):
  if n % i == 0:
   return False
  return True

print(is_prime_number(60))
print(is_prime_number(61))


#(3)----------------------------------
for a in range(10,0,-1):
    print(a, end=', ' if a > 1 else '\n')


#(4)----------------------------------

i ='*'
while i <= '*****':
 print(i)
 i+='*'



