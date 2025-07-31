# color = ['red','blue','green','yellow']
# result= ''
# for s in color:
#     result += s
# print(result)

# ------------------------------------------------

# color = ['red','blue','green','yellow']
# result = ' '.join(color)
# print(result)

# ------------------------------------------------

# items = 'zero one two three'.split()
# print(items)

# ------------------------------------------------

# example = 'python,jquery,javascript'
# print(example.split(","))

# a, b, c = example.split(",")
# print(a, b, c)

# example = 'theteamlab.univ.edu'
# subdomain, domain, tld = example.split('.')
# print(subdomain, domain, tld)

# ------------------------------------------------

# colors = ['red','blue','green','yellow']
# result = ''.join(colors)
# print(result)
# result = ' '.join(colors)
# print(result)
# result = ', '.join(colors)
# print(result)
# result = '-'.join(colors)
# print(result)

# ------------------------------------------------

# result = []
# for i in range(10):
#     result.append(i)

# print(result)

# result = [i for i in range(10)]
# print(result)

# ------------------------------------------------

# result = []
# for i in range(10):
#     if i % 2 == 0:    
#         result.append(i)
#     else : 
#         result.append(10)
        
# print(result)

# result = [i for i in range(10) if i % 2 == 0]
# print(result)

# result = [i for i in range(10) if i % 2 == 0 else 10]
# result = [i if i % 2 == 0 else 10 for i in range(10)]
# print (result)
# ------------------------------------------------

# # 응용하여 만든 함수!
# result = []
# def number(random): 
#     for i in range(random):
#         if i % 2 == 0:
#             result.append(i)
#         else :
#             result.append(10)
#     return result

# magic_number = int(input())
# print(number(magic_number))

# ------------------------------------------------

# word_1 = "Hello"
# word_2 = "World"
# result = [i + j for i in word_1 for j in word_2]
# print(result)


# word_1 = "Hello"
# word_2 = "World"

# result = []
# for i in word_1:
#     for j in word_2:
#         result.append(i+j)
# print(result)
    
# ------------------------------------------------

# case_1 = ["A","B","C"]
# case_2 = ["D","E","F"]
# result = [i + j for i in case_1 for j in case_2 if not (i==j)]
# print(result)

# case_1 = ["A","B","C"]
# case_2 = ["D","E","F"]
# result = []
# for i in case_1:
#     for j in case_2:
#         if not(i==j):
#             result.append(i+j)
# print(result)

# ------------------------------------------------

# words = 'The quick brown fox jumps over the lazy dog'.split()
# print(words)

# stuff = [[w.upper(),w.lower(),len(w)]for w in words]
# print(stuff)


# words = 'The quick brown fox jumps over the lazy dog'.split()

# stuff = []
# for w in words:
#     i = [w.upper(),w.lower(),len(w)]
#     stuff.append(i)

# print(stuff)

# ------------------------------------------------

# case_1 = ["A","B","C"]
# case_2 = ["D","E","A"]
# result = [[i + j for i in case_1] for j in case_2]
# print(result)

# case_1 = ["A","B","C"]
# case_2 = ["D","E","A"]
# result = []
# for j in case_2:
#     result_2 = []
#     result.append(result_2)
#     for i in case_1:
#         result_2.append(i+j)

# print(result)

# ------------------------------------------------

# def sclar_vector_product(scalar, vector):
#     result = []
#     for value in vector:
#         result.append(scalar * value)
#     return result

# iteration_max = 10000

# vector = list(range(iteration_max))
# scalar = 2

# for _ in range(iteration_max):
#     print(sclar_vector_product(scalar, vector))

# ------------------------------------------------

# iteration_max = 10000

# vector = list(range(iteration_max))
# scalar = 2

# for _ in range(iteration_max):
#     print([scalar * value for value in range(iteration_max)])

# ------------------------------------------------

# for i,v in enumerate(['tic','tac','toe']):
#     print(i,v)

# ------------------------------------------------

# {i:j for i,j in enumerate('TEAMLAB is an academic institue located in South Korea.'.split())}

# result = {}
# for i,j in enumerate('TEAMLAB is an academic institue located ins South Korea.'.split()):
#    result.update({i:j})
# print(result)

# ------------------------------------------------

# alist = ['a1','a2','a3']
# blist = ['b1','b2','b3']

# for a,b in zip(alist,blist):
#     print(a,b)

# ------------------------------------------------

# a, b, c = zip((1,2,3),(10,20,30),(100,200,300))
# print(a, b, c)

# ------------------------------------------------

# print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])

# result=[]
# for x in zip((1,2,3),(10,20,30),(100,200,300)):
#     result.append(sum(x))
# print(result)

# ------------------------------------------------

# alist = ['a1','a2','a3']
# blist = ['b1','b2','b3']

# for i,(a,b) in enumerate(zip(alist,blist)):
#     print(i,a,b)

# ------------------------------------------------

# mylist = ['pen','pencil','sharp']
# result = list(enumerate(mylist))
# print(result)

# ------------------------------------------------

# colors = ['orange','pink','brown','black','white']
# result = '&'.join(colors)
# print(result)

# ------------------------------------------------

# kor_score = [70,79,80,90,80]
# math_score = [42,80,30,50,90]
# eng_score = [53,77,50,70,55]
# midterm_score = [kor_score,math_score,eng_score]
# print("score :",midterm_score[2][1])

# ------------------------------------------------

# user_dict = {}
# user_list = ["students","superuser","professor","employee"]
# user_dict = {value_2 : value_1 for value_1, value_2 in enumerate(user_list) }
# print(user_dict)

# user_dict = {}
# user_list = ["students","superuser","professor","employee"]
# user_dict = {value_2 : value_1 for value_1, value_2 in enumerate(user_list) }

# for value_1, value_2 in enumerate(user_list):
#     user_dict.update({value_2 : value_1})

# print(user_dict)

# ------------------------------------------------

# alphabet = ["a","b","c","d","e","f","g","h"]
# nums = [i for i in range(20)]
# answer = [alpha + str(num) for alpha in alphabet for num in nums if num%2==0]
# print(len(answer))

# alphabet = ["a","b","c","d","e","f","g","h"]

# nums = [i for i in range(20)]

# nums = []
# for i in range(20):
#     nums.append(i)

# answer = [alpha + str(num) for alpha in alphabet for num in nums if num%2==0]

# answer = []
# for alpha in alphabet:
#     for num in nums:
#         if num%2==0:
#             answer.append(alpha+str(num))

# print(len(answer))

# ------------------------------------------------

# name = "Hanbit University"
# student = ["Hong","Gil","Dong"]
# split_name = name.split()
# join_student = ''.join(student)
# print(join_student[-4:]+split_name[1])   

# ------------------------------------------------

# animal = ['Fox','Dog','Cat','Monkey','Horse','Panda','Owl']
# print([ani for ani in animal if 'o' not in ani])

# animal = []
# for ani in animal:
#     if 'o' not in ani:
#         animal.append(ani)

# ------------------------------------------------

# result = [i for i in range(10) if i%2==0]
# print(result)

# result = []
# for i in range(10):
#     if i%2==0:
#         result.append(i)
# print(result)

# items = 'zero one two three'.split("two")
# result = [i for i in range(10)]
# print(result)

# result = []
# for i in range(10):
#     result.append(i)
# print(result)


# items = 'zero one two three'.split()
# print(items)

# example = 'cs50.gachon.edu'
# subdomain, domain, tld = example.split('.')
# print(subdomain)

# ------------------------------------------------

# dog_song = "my dog has brown eyes, my dog is cute"
# print({i:j for j,i in enumerate(dog_song.split())})

# result = {}
# for j,i in enumerate(dog_song.split()):
#     result.update({i:j})
# print(result)

# ------------------------------------------------

# kor_score = [49,79,20,100,80]
# math_score = [43,59,85,30,90]
# eng_score =[49,79,48,60,100]
# midterm_score = [kor_score,math_score,eng_score]
# print(midterm_score[0][2])

# ------------------------------------------------

# a = [1,2,3]
# b = [4,5,]
# c = [7,8,9]
# print([[sum(k),len(k)] for k in zip(a,b,c)])

# result = []
# for k in zip(a,b,c):
#     result.append([sum(k),len(k)])
# print(result)

# ------------------------------------------------

week = ['mon','tue','wed','thu','fri','sat','sun']
rainbow = ['red','orange','yellow','green','blue','navy','purple']
list_data = [week,rainbow]

print(list_data[0][4])

# ------------------------------------------------



