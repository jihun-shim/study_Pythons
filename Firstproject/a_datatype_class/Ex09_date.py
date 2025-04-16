"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""
#from datetime import date, datetime, timedelta
from datetime import date

#날짜 구하기
today = date.today()
print(today)

# 년,월,일
print(' 년도 : ', today.year)
print(' 월 : ', today.month)
print(' 일 : ', today.day)

from datetime import datetime

current_time = datetime.today()
print(current_time)

# 날짜 계산
from datetime import timedelta
today = date.today()
print('어제 :', today + timedelta(days=-1))
print('일주일 전 :', today + timedelta(days=-7))
print('10일 후 :', today + timedelta(days=10))

# 날짜 출력 형식(strftime()함수 이용)
today = datetime.today()
print(today.strftime('%m%d%Y')) #y-년도 두자리 Y-년도 네자리
print(today.strftime('%Y %m %d %H%M%S')) #y-년도 두자리, Y-년도 네자리, 시,분,초 대문자 H,M,S

# 문자열을 날짜 형식으로 변환(strptime())
str = "2024-09-30 17:50:00" # 남쌤 종강하는 날
mydate = datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))



