# 주민번호를 입력받아 관련정보를 출력하기

jumin = input('주민번호 입력->')

#1. 성별 출력 (041201-3182555)

# if jumin= [0:9]=1 ,'남자':
# print('남자' %1)
# print('여자' %2)

if(jumin[7]  == '1') or (jumin[7] == '3'):
    print('남자입니다.')
else:
    print('여자입니다.')

#2. 나이 출력

from datetime import date

# 1) 현재년도
today = date.today()
#print(today.year)
# 2) 성별코드
# 3) 주민번호의 앞 두자리 추출

if (jumin[7]  == '1') or (jumin[7] == '2'):
    age1=int(jumin[0:2])+1900
    print(((today.year) - (age1)) + 1 )

    #age= ((today.year) - (int(jumin[0:2])+1900)) + 1

else:
    age2=int(jumin[0:2])+2000
    print(((today.year) - (age2) ) + 1 )

   # age= ((today.year) - (int(jumin[0:2])+2000)) + 1

#print(age,'세 입니다.')

#3. 출생지역 출력 (8번쨰 자리의 값)
#   0 - 서울
#   1 - 인천/경기
#   3,4 - 충청도
#   5 - 전라도
#   7, 8 - 경상도
#   9 - 제주도

location = jumin[8]
birtharea=''

if location == '0':
    birthare = '서울'
elif location == '1':
    birthare ='인천/경기'
elif location == '3' or location == '4':
    birthare = '충청도'
elif location == '5':
    birthare = '전라도'
elif location == '7' or location == '8':
    birthare = '경상도'
elif location == '9':
    birthare = '제주도'
else:
    birthare = '강원도'

print('출생지역은' +' '+ birthare + '입니다')

