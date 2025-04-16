"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path

# (1) 해당 경로와 하위 목록들 확인
#p = Path('c:\Windows')
#print(p)

p = Path('..') # 부모 디렉토리
#print(p)
print(p.resolve()) #절대경로

test = []
for x in p.iterdir(): # p경로의 요소들을 반복
    if x.is_dir():
        test.append(x)
print(test)

j = list(p.glob('**/data/*.*')) # ** : 모든디렉토리, *.* : 모든 파일
print(j)


