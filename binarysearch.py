from random import shuffle

def binarysearch(arr, left, right, element):
    if right >= left:
        total = left + right
        middle = (total)//2
        if arr[middle] == element:
            return middle
        
        elif arr[middle] > element:
            return binarysearch(arr, left, middle - 1, element)
        
        else:
            return binarysearch(arr, middle + 1, right, element)
    else:
        return -1



_list = [i for i in range(1,100)]
#shuffle(_list)
print(_list)
element = int(input("Select an element "))
index = binarysearch(_list, 0, len(_list) - 1, element)
print("Index of %s is %s" %(element, index))
