from random import randint

def pigeon_sort(array):
    if len(array) == 0:
        return array

    min = array[0]
    max = array[0]

    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]

    holes_range = max - min + 1
    holes = [0 for _ in range(holes_range)]
    holes_repeat = [0 for _ in range(holes_range)]

    for i in range(len(array)):
        index = array[i] - min
        if holes[index] != array[i]:
            holes[index] = array[i]
            holes_repeat[index] += 1
        else:
            holes_repeat[index] += 1

    index = 0
    for i in range(holes_range):
        while holes_repeat[i] > 0:
            array[index] = holes[i]
            index += 1
            holes_repeat[i] -= 1

    return array

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(25)]
    print(random_list)
    arr = pigeon_sort(random_list)
    print(arr)