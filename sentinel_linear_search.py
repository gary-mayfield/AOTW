def sentinel_linear_search(sequence, target):
    sequence.append(target)

    index = 0

    while sequence[index] != target:
        index += 1

    sequence.pop()

    if index == len(sequence):
        return None
        
    return index

if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    x = 12
    result = sentinel_linear_search(arr, x)
    if result == None:
        print(f"Number {x} not found")
    else:
        print(f"Number {x} is at index {result}")