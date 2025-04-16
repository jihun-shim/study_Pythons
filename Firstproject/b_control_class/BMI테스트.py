#키, 몸무게 입력받기(int 변환)
height = int(input('키(cm): '))
weight = int(input('몸무게(kg): '))
bmi = weight // ((height*0.01)**2)

#BMI 계산 (변수에 담기)
#BMI 범위에 따른 조건식에서 메세지 담기
def getresult(bmi):
 if bmi > 20  and bmi < 24.9 :
    result= '정상입니다.'
 elif bmi > 25 and bmi < 29.9 :
    result= '과체중입니다.'
 elif bmi > 30 :
    result= '비만입니다.'
 else:
    result='저체중입니다.'
 return result

#출력
print(getresult(bmi))