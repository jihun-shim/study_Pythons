try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
        print("Not divided by 0")
finally:
    print("종료되었습니다.")

sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
    break
alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
 print(b[a])

alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
 print(a/int(b[0]))

