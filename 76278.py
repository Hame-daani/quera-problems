def calculator(n, m, li):
    a = 0
    b = m
    newlist = []
    while(a <= n):
        newlist.append(sum(li[a:b]))
        a, b = b, b+m
    s = 0
    z = 1
    for num in newlist:
        s += num*z
        z *= -1
    return s
