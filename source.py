from hashlib import sha256


class Site:
    def __init__(self, url_address):
        self.url = url_address
        self.register_users = []
        self.active_users = []

    def show_users(self):
        pass

    def register(self, user):
        if user in self.register_users:
            raise Exception("user already registered")
        else:
            self.register_users.append(user)
            return "register successful"

    def login(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        email = kwargs.get('email')
        user = None
        if username and password and email:
            for u in self.register_users:
                if u.username == username and u.email == email and u.verify_password(password):
                    user = u
                    break
        elif username and password:
            for u in self.register_users:
                if u.username == username and u.verify_password(password):
                    user = u
                    break
        elif email and password:
            for u in self.register_users:
                if u.email == email and u.verify_password(password):
                    user = u
                    break
        if user:
            if user in self.active_users:
                return "user already logged in"
            self.active_users.append(user)
            return "login successful"
        return "invalid login"

    def logout(self, user):
        if user in self.active_users:
            self.active_users.remove(user)
            return "logout successful"
        return "user is not logged in"

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url


class Account:
    def __init__(self, username, password, user_id, phone, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.user_id = self.id_validation(user_id)
        self.phone = self.phone_validation(phone)
        self.email = self.email_validation(email)

    def set_new_password(self, password):
        self.password = self.password_validation(password)

    def username_validation(self, username):
        valid_lower = "abcdefghijklmnopqrstuvwxyz"
        valid_upper = valid_lower.upper()
        valids = valid_lower + valid_upper
        if username.count('_') != 1:
            raise Exception("invalid username")
        first, last = username.split('_')
        if not (first and last):
            raise Exception("invalid username")
        for c in first:
            if c not in valids:
                raise Exception("invalid username")
        for c in last:
            if c not in valids:
                raise Exception("invalid username")
        return username

    def password_validation(self, password):
        if len(password) < 8:
            raise Exception("invalid password")
        upper_flag = False
        lower_flag = False
        digit_flag = False
        for c in password:
            if upper_flag and lower_flag and digit_flag:
                break
            if c.islower():
                lower_flag = True
            if c.isupper():
                upper_flag = True
            if c.isdigit():
                digit_flag = True
        if not (upper_flag and lower_flag and digit_flag):
            raise Exception("invalid password")
        return sha256(password.encode('utf-8')).hexdigest()

    def id_validation(self, id):
        if not isinstance(id, str):
            id = str(id)
        if (not id.isdigit()) or len(id) != 10:
            raise Exception("invalid code melli")
        sum = 0
        for i in range(9):
            sum += int(id[i])*(10-i)
        rem = sum % 11
        if rem < 2:
            control = rem
        else:
            control = 11 - rem
        if int(id[9]) != control:
            raise Exception("invalid code melli")
        return id

    def phone_validation(self, phone):
        if not isinstance(phone, str):
            id = str(phone)
        if phone.startswith("+989"):
            phone = phone.replace('+989', '09')
        if not phone.startswith("09") or len(phone) != 11:
            raise Exception("invalid phone number")
        return phone

    def email_validation(self, email):
        i = email.find('@')
        first_part = email[:i]
        rem = email[i+1:]
        i = rem.rfind('.')
        second_part = rem[:i]
        third_part = rem[i+1:]
        valid_chars = "._-0123456789"
        valid_lower = "abcdefghijklmnopqrstuvwxyz"
        valid_upper = valid_lower.upper()
        valids = valid_lower + valid_upper
        for c in first_part:
            if (c not in valids) and (c not in valid_chars):
                raise Exception("invalid email")
        for c in second_part:
            if (c not in valids) and (c not in valid_chars):
                raise Exception("invalid email")
        for c in third_part:
            if c not in valids:
                raise Exception("invalid email")
        if len(third_part) > 5 or len(third_part) < 2:
            raise Exception("invalid email")
        return email

    def verify_password(self, password):
        password = sha256(password.encode('utf-8')).hexdigest()
        if password == self.password:
            return True
        return False

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


def show_welcome(func):
    def inner(user):
        name = user.username.replace('_', ' ').title()
        if len(name) > 15:
            name = name[:15]+"..."
        return func(name)
    return inner


def verify_change_password(func):
    def inner(user, oldpass, newpass):
        user_pass = user.password
        old_pass = sha256(oldpass.encode('utf-8')).hexdigest()
        if user_pass == old_pass:
            user.set_new_password(newpass)
            return func(user, oldpass, newpass)
    return inner


@show_welcome
def welcome(user):
    return ("welcome to our site %s" % user)


@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")
