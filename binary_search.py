def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print(f"Target not found")

"""Numbers need to be sorted in binary search. If numbers are not sorted, it may return not found even if the value exists"""
numbers = [11,2,3,14,1,6,4,38,19,10]
numbers.sort()
result  = binary_search(numbers, 10)
verify(result)