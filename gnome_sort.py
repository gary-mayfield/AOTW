from random import randint

def gnome_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    i = 1

    while i < len(unsorted):
        if unsorted[i - 1] <= unsorted[i]:
            i += 1
        else:
            unsorted[i - 1], unsorted[i] = unsorted[i], unsorted[i - 1]
            i -= 1
            if i == 0:
                i = 1

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(25)]
    print(random_list)
    gnome_sort(random_list)
    print(random_list)