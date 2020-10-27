import math
from random import randint

def prime_check(number: int) -> bool:
    """
    Checks to see if a number is a prime.
    Returns true if a number has only two factors: 1 and itself.
    """
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i: int = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    random_list = [randint(1, 10000) for i in range(25)]
    print(random_list)
    for number in random_list:
        if prime_check(number):
            print(f'{number} is prime')
        else:
            print(f'{number} is not prime')