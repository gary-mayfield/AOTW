from random import randint

def pancake_sort(arr):
    cur = len(arr)
    while cur > 1:
        max_index = arr.index(max(arr[0:cur]))
        arr = arr[max_index::-1] + arr[max_index + 1: len(arr)]
        arr = arr[cur-1::-1] + arr[cur:len(arr)]
        cur -= 1
    return arr

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(25)]
    print(random_list)
    arr = pancake_sort(random_list)
    print(arr)