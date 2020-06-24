from random import randint

def cocktail_shaker_sort(unsorted: list) -> list:
    for i in range(len(unsorted) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                swapped = True

        for j in range(i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swapped = True

        if not swapped:
            return unsorted

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(25)]
    print(random_list)
    
    print(cocktail_shaker_sort(random_list))