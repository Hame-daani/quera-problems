# a-b > a+b
c = 0
n = int(input())
l = list(map(int, input().split()))
negs = sum(1 for i in l if i < 0)
c = negs * (n - 1)
print(c)
