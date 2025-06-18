'''
-월금리 계산-
신한은행 신한주택대출(아파트) : 0.005675
신한은행 우리 WON 갈아타기 직장인대출 : 0.004308
BNK BNK모바일주택담보대출 : 0.005441
신한은행 신한 MY CAR 신차 대출 : 0.004508
국민은행 KB 스타 아파트 담보대출 혼합금리(주택자금) : 0.003325
주식회사 카카오뱅크 일반신용대출 : 0.003541
신한은행 신한은행 쏠편한 직장인대출S I : 0.003975
'''


loan_products =[ 
    {"company": "신한은행", "product": "신한주택대출(아파트)", "base_rate": 3.42, "additional_rate": 3.99, "preferred_rate": 0.60} ,'\n' ,
    {"company": "우리은행", "product": "우리 WON 갈아타기 직장인대출", "base_rate": 3.97, "additional_rate": 2.60, "preferred_rate": 1.40}, '\n' ,
    {"company": "BNK", "product": "BNK모바일주택담보대출", "base_rate": 3.14, "additional_rate": 3.99, "preferred_rate": 0.60},'\n' ,
    {"company": "신한은행", "product": "신한 MY CAR 신차 대출", "base_rate": 3.41, "additional_rate": 2.60, "preferred_rate": 0.60},'\n' ,
    {"company": "국민은행", "product": "KB 스타 아파트 담보대출 혼합금리(주택자금)", "base_rate": 3.15, "additional_rate": 2.24, "preferred_rate": 1.40},
    {"company": "주식회사 카카오뱅크", "product": "일반신용대출", "base_rate": 3.32, "additional_rate": 1.53, "preferred_rate": 0.60} ,
    {"company": "신한은행", "product": "신한은행 쏠편한 직장인대출S I", "base_rate": 4.87, "additional_rate": 1.30, "preferred_rate": 1.40}
]

'''
print('-전체 상환 총액이 낮은 상품-')
print('')
 for i in loan_product:
'''
#
print(loan_products)

