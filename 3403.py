from math import prod


a = float(input())
b = float(input())
c = float(input())
d = float(input())
l = [a, b, c, d]
s = sum(l)
n = len(l)
print(f"Sum : {s:.6f}")
print(f"Average : {s/n:.6f}")
print(f"Product : {prod(l):.6f}")
print(f"MAX : {max(l):.6f}")
print(f"MIN : {min(l):.6f}")
