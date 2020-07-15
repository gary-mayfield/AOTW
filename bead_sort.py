from random import randint

def bead_sort(sequence: list) -> list:
    if any(not isinstance(x,int) or x <0 for x in sequence):
        raise TypeError("Sequence must be a list of non negative integers")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(25)]
    print(random_list)
    arr = bead_sort(random_list)
    print(arr)