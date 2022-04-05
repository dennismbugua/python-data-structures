#Creating an array
import array as arr

a = arr.array('i', [1,2,3])

print("The newly created array is: ", end=" ")
for i in range(0, 3):
    print(a[i], end = " ")
print()

b = arr.array('d', [2.5,3.1,3.5,3.9])
print(f"The arrays are: ")
for d in range(0,3):
    print(b[d], end=", ")