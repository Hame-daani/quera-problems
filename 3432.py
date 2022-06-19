# n: javad
# m: mostafa
_ = input()
n = set(input().split())
m = set(input().split())
n, m = n - m, m - n
if n and (not m):
    print("Mostafa")
elif m and (not n):
    print("Mohammad Javad")
elif (not n) and (not m):
    print("Both")
else:
    print("None")
