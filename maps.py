#python program to demostrate maps

#fun - function to which map passes each element of given iterable
#iter - iteratable which is to be mapped
#map syntax => map(fun, iter)

#Returns double of n
"""def addition(n):
    return n * n"""

"""numbers = [1,2,3,4,5]
numbers1 = [6,7,8,9,10]
results = map(lambda x, y: x + y, numbers, numbers1)
print(list(results))"""




"""num1 = [1,2,3,4]
num2 = [5,6,7,8]
results = map(lambda x, y: x + y, num1, num2)
print(tuple(results))"""

numbers2 = [4,5,6,7,8,9]
results = map(lambda x: x * x, numbers2)
print(tuple(results))