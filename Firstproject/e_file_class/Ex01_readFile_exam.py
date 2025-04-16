""" [연습]
    함수 정의 : count_words
    인자 : filename

    인자로 받은 파일명을 open 하여 파일을 읽어서 단어를 수를 출력한다.
    존재하지 않는 파일명으로 예외가 발생해도 아무런 일을 하지 않는다
"""
from e_file_class.Ex01_readFile import contents


def count_words(filename):
    print(filename)# pass 대신 완성
    try:
        with open('./data/' + filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            words = contents.split()
            num = len(words)
    except FileNotFoundError as fe:
        print(fe)
        print('파일을 읽을 수 없습니다')
    else:
        print('파일명 : ' + filename + ', 총 단어수 : ' + str(num))
filenames = ['sample.xml', 'xxxx.xxx', 'temp.json']
for filename in filenames: # 하나의 파일 단위로 함수 호출
    count_words(filename)


try:
    fname = './data/' + filename
    with open(fname, encoding='utf-8') as file:
        contents = file.read