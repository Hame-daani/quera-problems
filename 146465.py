def solve(n, k):
    return not n % k


n, k = map(int, input().split())
print("YES " if solve(n, k) else "NO")
