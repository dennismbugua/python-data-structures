import array as arr

a = arr.array('i', [4,6,8,10,11])
print(f"The array before insertion is: ", end=" ")
for i in range(0, 5):
    print(a[i], end = " ")
print()

a.insert(3, 9)
print(f"Array after insertion is: ", end=" ")
for i in (a):
    print(i, end=" ")
print()

a.insert(6, 12)
print(f"second insertion is: ", end=" ")
for i in a:
    print(i, end=" ")
print()

a.append(14)
print(f"Array after appending is: ", end=" ")
for i in (a):
    print(i, end=" ")
print()

print(f"Popped element is: ", end=" ")
print(a.pop(0))

print(f"Print element after popping", end=" ")
for i in a:
    print(i, end=" ")
print()