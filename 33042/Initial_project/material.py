class User:
    def __init__(self, username: str, name: str, age: int):
        """
        :param username: "Sara__99"
        :param name: "Sara"
        :param age: 20
        """
        self.username: str = username
        self.name: str = name
        self.age: int = age

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.username == other.username


class TrafficUsage:
    def __init__(self, user: User, internal: bool, nightly: bool, usage: int, date: str):
        """
        :param user: <User object>
        :param internal: True
        :param nightly: True
        :param usage: 10 MB
        :param date: yy/mm/dd
        """
        self.user: User = user
        self.internal: bool = internal
        self.nightly: bool = nightly
        self.usage: int = usage
        self.date = date


class TrafficUsageDao:
    """
    Traffic Data Usage Data Access Object
    """
    def load_all(self):
        """
        :return: List of <TrafficUsage object>s
        """
        return [
            TrafficUsage(),
            TrafficUsage(),
            TrafficUsage(),
            TrafficUsage(),
        ]
