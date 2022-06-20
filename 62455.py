import itertools

_ = input()

# ins = list(map(int, input().split()))
# s = sum(a // b for a, b in itertools.product(ins, ins))


# ins = list(map(int, input().split()))
# n = max(ins) + 1
# nums = [0 for i in range(n)]
# for i in ins:
#     nums[i] += 1
# s = 0
# for i in range(n - 1, 0, -1):
#     if nums[i] == 0:
#         continue
#     for j in range(i, 0, -1):
#         if nums[j] == 0:
#             continue
#         a = nums[i]
#         b = nums[j]
#         s += (a * b) * (i // j)


ins = map(int, input().split())
nums = {}
n = 0
for num in ins:
    try:
        nums[num] += 1
    except:
        nums[num] = 1
        n += 1
s = 0
nums = sorted(nums.items(), reverse=True)
for i in range(n):
    for j in range(i, n):
        a, r = nums[i]
        b, k = nums[j]
        s += (r * k) * (a // b)

# nums = nums.items()
# s = sum((a[1] * b[1]) * (a[0] // b[0]) for a, b in itertools.product(nums, nums))

print(s)
