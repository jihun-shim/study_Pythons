import csv
#1. 리스트 데이터는 csv 파일로 저장하기
data = [[1, '김', '책임'],[2, '박', '선임'],[3, '주', '선임']]
with open('./data/imsi.csv', 'wt', encoding='utf-8') as f:
    cout = csv.writer(f)
    cout.writerow(data)

# 2. csv 파일을 읽어서 리스트 변수에 저장하기
data = []
with open('./data/imsi.csv', 'rt', encoding='utf-8') as fin:
    cin = csv.reader(fin)
    data = [row for row in cin if row]
print(data)





