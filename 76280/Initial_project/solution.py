import json
import csv


def shift(input):
    res = input[:]
    x = res.pop(0)
    res.append(x)
    return res


def process(json_files_paths_list):
    data = []
    inputs = []
    for path in json_files_paths_list:
        with open(path, "r") as f:
            data.append(json.load(f))
    for row in data:
        l = []
        for col, value in row.items():
            l.insert(int(col), int(value))
        inputs.append(l)
    for row in inputs:
        row.sort()
    res = []
    for i, row in enumerate(inputs):
        r = row
        for _ in range(i):
            r = shift(r)
        res.append(r)
    with open("ans.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(res)
