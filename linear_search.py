def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None

if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    x = 13
    result = linear_search(arr, x)
    if result == None:
        print(f"Number {x} not found")
    else:
        print(f"Number {x} is at index {result}")