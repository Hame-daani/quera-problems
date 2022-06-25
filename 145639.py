def solve(s, f, l, x):
    if x >= f:
        return "exam finished!"
    if x < s:
        return "exam did not started!"
    return min(l, f - x)


s, f, l, x = map(int, input().split())
print(solve(s, f, l, x))
