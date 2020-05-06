from random import randint

DEFAULT_BUCKET_SIZE = 5

def bucket_sort(random_list, bucket_size=DEFAULT_BUCKET_SIZE):
    if len(random_list) == 0:
        return []
    
    min_value, max_value = (min(random_list), max(random_list))
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]

    for i in range(len(random_list)):
        buckets[int((random_list[i] - min_value) // bucket_size)].append(random_list[i])

    return sorted([buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))])

if __name__ == '__main__':
    random_list = [randint(1, 100) for i in range(25)]
    print(random_list)
    
    print(bucket_sort(random_list))