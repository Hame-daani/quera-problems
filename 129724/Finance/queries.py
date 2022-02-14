from django.db.models import F, Sum, Count, Case, When
from .models import *


def query_0():
    q = Employee.objects.all()
    return q


def query_1():
    return Payslip.objects.filter(payment=None).aggregate(
        total_dept=Sum(F("base") + F("tax")+F('insurance')+F('overtime'))
    )


def query_2(x):
    return Payslip.objects.filter(salary__overtime__gte=x).aggregate(
        total_overtime=Sum(F('overtime'))
    )


def query_3():
    return Payment.objects.all().aggregate(
        total=Sum(F('amount'))
    )


def query_4(x):
    # TODO
    pass


def query_5(x):
    # TODO
    pass


def query_6():
    # TODO
    pass


def query_7():
    # TODO
    pass


def query_8():
    # TODO
    pass


def query_9(x):
    # TODO
    pass


def query_10():
    # TODO
    pass
