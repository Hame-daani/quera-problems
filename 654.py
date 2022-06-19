n = int(input())

for a in range(1, n):
    p = (a**2) // (n - a)
    b = (n - a - p) // 2
    c = n - a - b
    if (a > 1 and b > 1 and c > 1) and (a**2 + b**2 == c**2) and (a + b + c == n):
        print(a, b, c)
        exit()

print("Impossible")
