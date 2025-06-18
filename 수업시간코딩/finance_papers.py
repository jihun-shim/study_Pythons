# 금융 상품 관련 문제 리스트
questions = [
    {
        "question": "정기 예금의 주요 특징은 무엇인가요?",
        "options": ["A. 높은 유동성", "B. 고정 금리", "C. 만기 기간 없음", "D. 높은 위험"],
        "answer": "B"
    },
    {
        "question": "다음 중 정부가 발행하는 증권 유형은 무엇인가요?",
        "options": ["A. 국채", "B. 회사채", "C. 뮤추얼 펀드", "D. 정기 예금"],
        "answer": "A"
    },
    {
        "question": "대출에서 APR은 무엇의 약자인가요?",
        "options": ["A. 연이율", "B. 평균 지급률", "C. 누적 지급 비율", "D. 연간 지급 비율"],
        "answer": "A"
    },
    {
        "question": "다음 중 가장 안전한 투자 옵션은 무엇인가요?",
        "options": ["A. 주식", "B. 채권", "C. 저축 계좌", "D. 부동산"],
        "answer": "C"
    },
    {
        "question": "복리의 주요 이점은 무엇인가요?",
        "options": ["A. 세금 절감", "B. 빠른 자산 축적", "C. 유동성 증가", "D. 고정 금리"],
        "answer": "B"
    }
]


sum=0
result=[]

for que in questions:
    print('**',que['question'],'**')
    for opt in que['options']:
         print(opt)
    user=input('당신의 답변 (A, B, C 또는 D) :')
    if  user == que['answer'] :
        print('정답입니다!')
        result.append('정답')
        sum += 1         
    else :
        print('틀렸습니다.')
        result.append('오답')    
    
print('**퀴즈 완료! 당신의 총 점수는:' , sum ,'/5' , '**')