from random import randint

def merge(left, right):
    if not len(left):
        return left
    if not len(right):
        return right
    
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    while(len(result) < totalLen):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
    
    return result

def mergesort(arr):
    if len(arr) < 2:
        return arr
    
    middle = len(arr)//2

    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    merged = merge(left, right)
    return merged

random_list = [randint(1, 25) for i in range(10)]
print(random_list)
sorted_list = mergesort(random_list)
print(sorted_list)