n = int(input())
serials = [input() for _ in range(n)]

for serial in serials:
    l = list(serial)
    for i in range(len(l) - 2, -1, -1):
        # find smallest char from right
        if l[i] < l[i + 1]:
            # find next char bigger than l[i]
            m = None
            for j in range(i + 1, len(l)):
                if l[i] < l[j]:
                    if m:
                        if l[m] > l[j]:
                            m = j
                    else:
                        m = j
            if m:
                l[i], l[m] = l[m], l[i]
                print("".join(l[: i + 1] + sorted(l[i + 1 :])))
                break
    else:
        print("no answer")
