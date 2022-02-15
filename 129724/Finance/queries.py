from django.db.models import F, Sum, Count, Case, When, Q
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
    return EmployeeProjectRelation.objects.filter(employee__id=x).aggregate(
        total_hours=Sum(F('hours'))
    )


def query_5(x):
    return Employee.objects.annotate(
        total=Sum("salary__payslip__payment__amount")
    ).filter(total__gt=x)


def query_6():
    return Employee.objects.annotate(
        total_hours=Sum("employeeprojectrelation__hours")
    ).order_by("-total_hours", "account__username").first()


def query_7():
    # TODO
    return Department.objects.annotate(
        total=Sum("employee__salary__payslip__payment__amount")
    ).order_by("-total", "name").first()


def query_8():
    # TODO not working on site
    return Department.objects.filter(
        project__end_time__lte=F('project__estimated_end_time')
    ).annotate(projects=Count('project')).order_by('-projects', 'name').first()


def query_9(x):
    # TODO
    return Employee.objects.filter(
        attendance__in_time__gt=x
    ).annotate(
        late_days=Count('attendance')
    ).order_by('late_days', 'account__username').first()


def query_10():
    return Employee.objects.filter(
        employeeprojectrelation=None
    ).aggregate(total=Count('*'))
