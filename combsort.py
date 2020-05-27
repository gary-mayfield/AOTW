from random import randint

def combsort(data: list) -> list:
    shrink_factor = 1.3
    gap = len(data)
    finished = False

    while not finished:
        gap = int(gap/shrink_factor)
        if gap <= 1:
            finished = True

        index = 0
        while index + gap < len(data):
            if data[index] > data[index + gap]:
                data[index], data[index + gap] = data[index + gap], data[index]
                finished = False
            index += 1

    return data

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(25)]
    print(random_list)
    
    print(combsort(random_list))