from random import randint

def heaps(arr: list) -> list:
    if len(arr) <=1:
        return [tuple(arr)]

    result = []

    def generate(k: int, arr: list):
        if k == 1:
            result.append(tuple(arr[:]))
            return

        generate(k - 1, arr)

        for i in range(k - 1):
            if k % 2 == 0:
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
            else:
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            generate(k - 1, arr)

    generate(len(arr), arr)
    return result

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(3)]
    print(random_list)
    
    print(heaps(random_list))