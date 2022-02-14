from django.db import models
import jdatetime
from django_jalali.db import models as jmodels

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class CustomUser(models.Model):
    username = models.CharField(max_length=256, null=True)
    full_name = models.CharField(max_length=256, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True)
    national_code = models.CharField(max_length=10, null=True)
    birthday_date = jmodels.jDateField(null=True)
    ceremony_datetime = jmodels.jDateTimeField(null=True)
    country = models.CharField(default='Iran', max_length=10)

    def get_first_and_last_name(self):
        first_name, last_name = self.full_name.split(' ')
        return {'first_name': first_name, 'last_name': last_name}

    def get_age(self):
        now = jdatetime.date.today()
        age = now - self.birthday_date
        return int(age.days/365)

    def is_birthday(self):
        now = jdatetime.date.today()
        bd = self.birthday_date
        return now.month == bd.month and now.day == bd.day
