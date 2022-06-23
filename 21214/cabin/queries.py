from cabin.models import *
from django.db.models import (
    Sum,
    F,
    Q,
    Count,
    FloatField,
    ExpressionWrapper,
    Case,
    When,
    IntegerField,
)


def query_0(x):
    q = Driver.objects.filter(rating__gt=x)
    return q


def query_1(x):
    q = Payment.objects.filter(ride__car__owner__id=x).aggregate(
        payment_sum=Sum("amount")
    )
    return q


def query_2(x):
    q = Ride.objects.filter(request__rider__id=x)
    return q


def query_3(t):
    q = (
        Ride.objects.annotate(duration=F("dropoff_time") - F("pickup_time"))
        .filter(duration__gt=t)
        .count()
    )

    return q


def query_4(x, y, r):
    q = Driver.objects.annotate(
        loc=ExpressionWrapper(
            ((F("x") - x) ** 2) + ((F("y") - y) ** 2), output_field=FloatField()
        )
    ).filter(active=True, loc__lt=r**2)
    return q


def query_5(n, c):
    q = (
        Driver.objects.annotate(ride_num=Count("car__ride"))
        .filter(Q(car__color=c) | Q(car__car_type="A"))
        .filter(ride_num__gte=n)
    )
    return q


def query_6(x, t):
    q = Rider.objects.annotate(
        ride_num=Count("riderequest__ride"),
        total_pay=Sum("riderequest__ride__payment__amount"),
    ).filter(ride_num__gte=x, total_pay__gt=t)
    return q


def query_7():
    q = Driver.objects.filter(
        account__first_name=F("car__ride__request__rider__account__first_name")
    )
    return q


def query_8():
    q = Driver.objects.annotate(
        n=Count(
            "car__ride",
            filter=Q(
                account__last_name=F("car__ride__request__rider__account__last_name")
            ),
        )
    )
    return q


def query_9(x, t):
    # TODO: not working
    s = Ride.objects.annotate(duration=F("dropoff_time") - F("pickup_time")).filter(
        duration__gt=t, car__model__gte=x
    )
    q = Driver.objects.annotate(n=Count("car__ride", filter=Q(car__ride__in=s))).values(
        "id", "n"
    )
    return q


def query_10():
    q = Car.objects.annotate(
        extra=Case(
            When(
                car_type="A",
                then=Count("ride"),
            ),
            When(
                car_type="B", then=Sum(F("ride__dropoff_time") - F("ride__pickup_time"))
            ),
            When(car_type="C", then=Sum("ride__payment__amount")),
            output_field=IntegerField(),
        )
    )
    return q
