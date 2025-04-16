import json

f = open('./data/temp.json', 'r', encoding='utf-8')
json_data = f.read()
print(json_data)
print('--------------------------')
data = json.loads(json_data)
print(data)

for item in data :
    #print('>', item)
    #딕셔너리 개념으로 생각하고 자료를 얻어오기
    print(data[item])
    for val in data[item]:  # No, job의 값도 출력한다면
        print(data[item][val])



