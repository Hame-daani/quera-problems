available_days = [
    "shanbe",
    "1shanbe",
    "2shanbe",
    "3shanbe",
    "4shanbe",
    "5shanbe",
    "jome",
]
for i in range(3):
    _ = input()
    p_days = input()
    for day in p_days.split():
        try:
            available_days.remove(day)
        except ValueError:
            pass
print(len(available_days))
