import csv

data = {
    "esm": [],
    "famil": [],
    "keshvar": [],
    "rang": [],
    "ashia": [],
    "ghaza": [],
}
ps = {}


def ready_up():
    with open("esm_famil_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data["esm"].append(row["esm"].replace(" ", ""))
            data["famil"].append(row["famil"].replace(" ", ""))
            data["keshvar"].append(row["keshvar"].replace(" ", ""))
            data["rang"].append(row["rang"].replace(" ", ""))
            data["ashia"].append(row["ashia"].replace(" ", ""))
            data["ghaza"].append(row["ghaza"].replace(" ", ""))


def add_participant(participant, answers):
    ps[participant] = answers


def calculate_all():
    answers = {
        "esm": [],
        "famil": [],
        "keshvar": [],
        "rang": [],
        "ashia": [],
        "ghaza": [],
    }
    n = len(ps)
    scores = {p: 0 for p in ps}

    for p, ans in ps.items():
        for field, a in ans.items():
            a = a.replace(" ", "")
            if len(a) > 0:
                answers[field].append(a)

    for p, ans in ps.items():
        for field, a in ans.items():
            a = a.replace(" ", "")
            if len(a) == 0 or a not in data[field]:
                scores[p] += 0
            elif len(answers[field]) == n:
                # everybodey answered
                if answers[field].count(a) > 1:
                    # repeated answer
                    scores[p] += 5
                else:
                    # unique answer
                    scores[p] += 10
            else:
                # someone didnt answered
                if answers[field].count(a) > 1:
                    # repeated answer
                    scores[p] += 10
                else:
                    # unique answer
                    scores[p] += 15
    return scores
