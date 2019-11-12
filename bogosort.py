from random import randint, shuffle

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True



def bogosort(arr):
    counter = 0
    while not is_sorted(arr):
        print(counter)
        shuffle(arr)
        counter += 1

random_list = [randint(1, 25) for i in range(10)]
print(random_list)
bogosort(random_list)
print(random_list)