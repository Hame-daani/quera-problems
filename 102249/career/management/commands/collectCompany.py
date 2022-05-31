from django.core.management.base import BaseCommand, CommandError, CommandParser
from career.models import Company
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        # TODO: test failed
        with open("company.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=" ")
            for c in Company.objects.all():
                writer.writerow([c.name, c.email, c.phone])
