# Generated by Django 3.2.6 on 2022-02-14 06:52

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday_date',
            field=django_jalali.db.models.jDateField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='ceremony_datetime',
            field=django_jalali.db.models.jDateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(default='Iran', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='national_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
