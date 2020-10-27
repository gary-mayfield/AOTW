def double_linear_search(arr, x):
    start_ind, end_ind = 0, len(arr) - 1
    while start_ind <= end_ind:
        if arr[start_ind] == x:
            return start_ind
        elif arr[end_ind] == x:
            return end_ind
        else:
            start_ind += 1
            end_ind -= 1
    # returns -1 if search_item is not found in array
    return -1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    x = 13
    result = double_linear_search(arr, x)
    if result == -1:
        print(f"Number {x} not found")
    else:
        print(f"Number {x} is at index {result}")