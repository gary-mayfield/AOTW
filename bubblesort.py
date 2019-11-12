from random import randint

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

random_list = [randint(1, 25) for i in range(10)]
print(random_list)
bubbleSort(random_list)
print(random_list)