n = int(input())
zones = set()

for _ in range(n):
    s, e = map(int, input().split())
    zones.update(range(s, e + 1))

a = int(input())
b = int(input())

if set(range(a, b + 1)).issubset(zones):
    print("true")
else:
    print("false")
