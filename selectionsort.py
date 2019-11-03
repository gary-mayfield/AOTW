from random import randint

def selectionSort(data):
    for i in range(len(data)):
        minIndex = i
        for j in range(i+1, len(data)):
            if data[minIndex] > data[j]:
                minIndex = j
        data[i], data[minIndex] = data[minIndex], data[i]

random_list = [randint(1,25) for i in range(10)]
print(random_list)
selectionSort(random_list)
print(random_list)