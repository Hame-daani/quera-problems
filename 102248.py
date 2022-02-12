def compare(string1, string2):
    a = string1[0]
    b = string2[0]
    if a > b:
        string2 = string2[1:]

    elif b > a:
        string1 = string1[1:]
    else:
        string1 = string1[1:]
        string2 = string2[1:]
    if string1 == "" and string2 == "":
        return "Both strings are empty!"
    if string1 == "":
        return string2
    if string2 == "":
        return string1
    return compare(string1[::-1], string2[::-1])
