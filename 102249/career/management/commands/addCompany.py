from django.core.management.base import BaseCommand, CommandParser
from career.models import Company
import re

email_regex = re.compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)

phone_regex = re.compile(r"^(0|\+98|0098)9[0-9]{9}$")


class Command(BaseCommand):
    def handle(self, *args, **options):
        ok = False
        while not ok:
            name = input("Name: ")
            if not name:
                self.stderr.write("Error: This field cannot be blank.")
            elif len(name) > 50:
                self.stderr.write(
                    f"Error: Ensure this value has at most 50 characters (it has {len(name)})."
                )
            else:
                ok = True
        # TODO: uniquness failed
        if Company.objects.filter(name=name).exists():
            self.stderr.write("Error: That name is already taken.")

        ok = False
        while not ok:
            email = input("Email: ")
            if not email:
                self.stderr.write("Error: This field cannot be blank.")
            elif not re.fullmatch(email_regex, email):
                self.stderr.write("Error: Enter a valid email address.")
            else:
                ok = True

        ok = False
        while not ok:
            phone = input("Phone: ")
            if not phone:
                self.stderr.write("Error: This field cannot be blank.")
            elif not re.fullmatch(phone_regex, phone):
                self.stderr.write("Error: Phone number format is not valid.")
            else:
                ok = True
        # TODO: blank desc failed
        description = input("Description: ")
        Company.objects.create(
            name=name, email=email, phone=phone, description=description
        )
