import datetime


class Factor:
    def __init__(self, date, value):
        self.date = date
        self.value = value


class FactorHandler:

    def __init__(self):
        self.factors = []

    def get_date(self, time_format, time):
        form = time_format.split('/')
        year_index = form.index('yyyy')
        month_index = form.index('mm')
        day_index = form.index('dd')
        time = time.split('/')
        year = int(time[year_index])
        month = int(time[month_index])
        day = int(time[day_index])
        return datetime.date(year, month, day)

    def add_factor(self, time_format, time, value):
        date = self.get_date(time_format, time)
        self.factors.append(Factor(date, value))

    def remove_all_factors(self, time_format, time):
        date = self.get_date(time_format, time)
        for factor in self.factors[:]:
            if factor.date == date:
                self.factors.remove(factor)

    def get_sum(self, time_format, start_time, finish_time):
        start_date = self.get_date(time_format, start_time)
        finish_date = self.get_date(time_format, finish_time)
        sum = 0
        for factor in self.factors:
            if start_date <= factor.date <= finish_date:
                sum += factor.value
        return sum
