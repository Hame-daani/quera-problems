import os


def next_path(path_pattern):
    """
    Finds the next free path in an sequentially named list of files
    Runs in log(n) time where n is the number of existing files in sequence
    """
    i = 1

    # First do an exponential search
    while os.path.exists(f"{path_pattern} ({i})"):
        i = i * 2

    # Result lies somewhere in the interval (i/2..i]
    # We call this interval (a..b] and narrow it down until a + 1 = b
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2  # interval midpoint
        a, b = (c, b) if os.path.exists(f"{path_pattern} ({c})") else (a, c)

    return f"{path_pattern} ({b})"


n = int(input())
names = []
# repeats = {}

for _ in range(n):
    name = input()
    names.append(name)

# print()

current_directory = os.getcwd()

for name in names:
    path = os.path.join(current_directory, name)
    # try:
    #     os.mkdir(path)
    # except:
    #     path = next_path(name)
    #     try:
    #         os.mkdir(path)
    #     except:
    #         pass
    if not os.path.exists(path):
        os.mkdir(path)
    l = sorted(filter(os.path.isdir, os.listdir()))
    print(str(l)[1:-1])
