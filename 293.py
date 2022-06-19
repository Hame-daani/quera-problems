from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    root = int(sqrt(x))
    for i in range(3, root + 1, 2):
        if x % i == 0:
            return False
    return True


a = int(input())
b = int(input())
for i in range(a, b + 1):
    if is_prime(i):
        print(i)
