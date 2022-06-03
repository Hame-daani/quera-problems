def check_registration_rules(**kwargs):
    blacklist = ["quera", "codecup"]
    min_uesrname_len = 4
    min_password_len = 6
    allowed = []
    for username, password in kwargs.items():
        if username in blacklist:
            continue
        if len(username) < min_uesrname_len:
            continue
        if len(password) < min_password_len:
            continue
        if password.isnumeric():
            continue
        allowed.append(username)
    return allowed
