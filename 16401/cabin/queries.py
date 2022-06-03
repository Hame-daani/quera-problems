from .models import *
from django.db.models import Count, Sum, F


def query_0():
    q = Driver.objects.all()
    return q


def query_1():
    """
    :return: Something like {'income': value }
    """
    q = Payment.objects.aggregate(income=Sum("amount"))
    return q


def query_2(x):
    """
    :return: Something like {'payment_sum': value }
    """
    q = Payment.objects.filter(ride__request__rider__id=x).aggregate(
        payment_sum=Sum("amount")
    )
    return q


def query_3():
    """
    :return: Just a number
    """
    q = Driver.objects.filter(car__car_type="A").distinct().count()
    return q


def query_4():
    """ """
    q = RideRequest.objects.filter(ride__isnull=True)
    return q


def query_5(t):
    """ """
    q = Rider.objects.annotate(sum=Sum("riderequest__ride__payment__amount")).filter(
        sum__gte=t
    )
    return q


def query_6():
    """
    :return: Account object
    """
    q = (
        Account.objects.annotate(count=Count("drivers__car"))
        .order_by("-count", "last_name")
        .first()
    )
    return q


def query_7():
    """ """
    q = Rider.objects.filter(riderequest__ride__car__car_type="A").annotate(
        n=Count("riderequest__ride")
    )
    return q


def query_8(x):
    """ """
    q = Driver.objects.filter(car__model__gte=x).distinct().values("account__email")
    return q


def query_9():
    """ """
    q = Driver.objects.annotate(n=Count("car__ride"))
    return q


def query_10():
    """ """
    q = Driver.objects.values("account__first_name").annotate(n=Count("car__ride"))
    return q


def query_11(n, c):
    """ """
    q = Driver.objects.filter(car__model__gte=n, car__color=c).distinct()
    return q


def query_12(n, c):
    """ """
    q = Driver.objects.filter(car__model__gte=n).filter(car__color=c).distinct()
    return q


def query_13(n, m):
    """
    :return: Something like {'sum_duration': value }
    """
    q = (
        Ride.objects.filter(
            car__owner__account__first_name=n, request__rider__account__first_name=m
        )
        .annotate(d=F("dropoff_time") - F("pickup_time"))
        .aggregate(sum_duration=Sum("d"))
    )
    return q
