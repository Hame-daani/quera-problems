from material import TrafficUsageDao


class TrafficUsageService:
    def __init__(self, traffic_usage_dao: TrafficUsageDao):
        self.traffic_usage_dao = traffic_usage_dao

    def social_media_lovers(self, year: int, month: int):
        data = {}
        for usage in self.traffic_usage_dao.load_all():
            y, m, d = usage.date.split("/")
            if not usage.internal and int(y) == year and int(m) == month:
                user = usage.user
                if user not in data:
                    data[user] = 0
                data[user] += usage.usage
        min_value = min(data.values(), default="EMPTY")
        max_value = max(data.values(), default="EMPTY")
        res = []
        for user, value in data.items():
            fraction = float(value - min_value) / (max_value - min_value)
            percentage = fraction * 100
            if percentage > 90:
                res.append(user)
        return res

    def download_lovers(self, year: int, month: int):
        data = {}
        for usage in self.traffic_usage_dao.load_all():
            y, m, d = usage.date.split("/")
            if int(y) == year and int(m) == month:
                user = usage.user
                if user not in data:
                    data[user] = {"d": 0, "n": 0}
                if usage.nightly:
                    data[user]["n"] += usage.usage
                else:
                    data[user]["d"] += usage.usage
        return [user for user, usage in data.items() if usage["n"] > usage["d"]]
