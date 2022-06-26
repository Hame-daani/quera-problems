# find min and max with length 'm' and sum 's'
def find(m, s, reverse=False):
    def helper(length, remaining, num, allowed):
        if length == 1:
            if remaining in allowed:
                return 10 * num + remaining
        elif 0 <= remaining <= 9 * length:
            # the biggest that we can produce in this level and further is "9*length"
            # and if in the previous level we chosed a 'v' bigger than remaining, then this level remaining is negative
            for v in allowed:
                if reverse:
                    rng = range(9, -1, -1)
                else:
                    rng = range(10)
                r = helper(length - 1, remaining - v, 10 * num + v, rng)
                if r:
                    return r

    if reverse:
        rng = range(9, 0, -1)
    else:
        rng = range(1, 10)
    return helper(m, s, 0, rng)


m, s = map(int, input().split())
mn = find(m, s) or -1
mx = find(m, s, reverse=True) or -1
print(mn, mx)
