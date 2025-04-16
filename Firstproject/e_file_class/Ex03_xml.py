# import xml.etree.ElementTree as et
#
# # temp.xml 확인
# tree = et.ElementTree(file='./data/temp2.xml')
#
# root = tree.getroot()
# #print(root)
# print(root.tag)
#
# for child in root:
#     #print(child.tag)
#     for grandchild in child:
#         print(grandchild.tag, '/', grandchild.text)
        #print(grandchild.tag(태그명), '/',grandchild.attrib(속성),'/', grandchild.text(실제데이터))




#[연습] sample.xml 파일에서 각 항목별 총합과 전체 항목의 총합 구하기

import xml.etree.ElementTree as et

# temp.xml 확인
# sampletree = et.ElementTree(file='./data/sample.xml')
#
# sampleroot = sampletree.getroot()
# #print(root)
# print(sampleroot.tag)
#
# for child in sampleroot:
#     print(child.tag)
#
#     for grandchild in child:
#
#         print(grandchild.tag, '전체총합',grandchild.text)

sampletree = et.ElementTree(file='./data/sample.xml')
sampleroot = sampletree.getroot()

totalprice = 0

# # 함수를 생성
# def subtotal(alist):
#     price = 0
#     cnt = 0
#     for child in alist:
#         for childsub in child:
#             if childsub.tag == 'price':
#                 price += int(childsub.text)
#             if childsub.tag == 'count':
#                 cnt += int(childsub.text)
#     return price*cnt
#
# fruit = [n for n in sampleroot if n.tag == 'fruit']
# item = [n for n in sampleroot if n.tag == 'item']
#
# fruittotal = subtotal(fruit)
# itemtotal = subtotal(item)
#
# print(f"fruit 의 합계 : {fruittotal}")
# print(f"item 의 합계 : {itemtotal}")
# print(f"총 합계 : {fruittotal + itemtotal}")



# # root, tag 명, tag 속성, tag 값 가져올 수 있다

total_price = 0
fruit_price = 0
item_price = 0

for child in sampleroot:
    #print(child.tag, '/', child.attrib)
    gChild_count = 0
    gChild_price = 0
    name = ''

    for grandchild in child :
        #print(grandchild.tag, '/', grandchild.text)
        if grandchild.tag == 'name':
            name = grandchild.text
        if grandchild.tag == 'count' :
            gChild_count = int(grandchild.text)
        if grandchild.tag == 'price' :
            gChild_price = int(grandchild.text)

        if gChild_count and gChild_price:
            print("총 " + name +" 가격 : " + str(gChild_count * gChild_price))
            total_price += (gChild_count * gChild_price)
            if child.tag == 'fruit':
                fruit_price += (gChild_count * gChild_price)
            if child.tag == 'item':
                item_price += (gChild_count * gChild_price)


print("총 가격 : " + str(total_price))
print("총 과일 가격 : " + str(fruit_price))
print("총 아이템 가격 : " + str(item_price))