# def linear_search(list, target):
#     for i in range(0, len(list)):
#         if list[i] == target:
#             yield i
#     return None

# def verify(index):
#     if index is not None:
#         print(f"Target found")
#     else:
#         print(f"Target not found")

# numbers = [1,2,3,4,5,6,7,8,9,10]
# result  = linear_search(numbers, 6)
# verify(result)

# def f(x, l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
    
    
# f(2)
# f(3, [3,2,1])
# f(3)

# alphabet = 'abcd'
# for i in range(len(alphabet)):
#     alphabet[i].upper()
# print(alphabet)

# def lifeSkills(val, list=[]):
#     list.append(val)
#     return list

# list1 = lifeSkills('NodeJS')
# list2 = lifeSkills('Java',[])
# list3 = lifeSkills('reactJS')
# print("%s" % list1)
# print("%s" % list2)
# print("%s" % list3)



# def add(c, k):
#     c.test = c.test + 1
#     k = k + 1
    
# class Plus:
#     def __init__(self):
#         self.test = 0
# def main():
#     p = Plus()
#     index = 0
    
#     for i in range(0, 25):
#         add(p, index)
        
#     print("p.test=", p.test)
#     print("index=", index)
# main()




# a = [1,2,3,4,]
# b = [sum(a[0:x+1]) for x in range(0, len(a))]
# print(b)

# print(2**(3**2), (2**3)**2, (2**3)**3)

# data = [10,20,30,40,50]
# data.pop()
# print(data)
# data.pop(2)
# print(data)


f = None
for i in range(5):
    with open("app.log", "w") as f:
        if i>2:
            break
print(f.closed)








