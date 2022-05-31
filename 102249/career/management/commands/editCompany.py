from django.core.management.base import BaseCommand, CommandError, CommandParser
from career.models import Company

import re

email_regex = re.compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)

phone_regex = re.compile(r"^(0|\+98|0098)9[0-9]{9}$")


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("company", type=str)
        parser.add_argument("--name", type=str)
        parser.add_argument("--email", type=str)
        parser.add_argument("--phone", type=str)
        parser.add_argument("--description", type=str)

    def handle(self, *args, **options):
        company = options["company"]
        c = Company.objects.filter(name=company)
        if not c.exists():
            raise CommandError("Company matching query does not exist.")
        name = options["name"]
        if name == "":
            raise CommandError("Name cannot be blank.")
        elif name and len(name) > 50:
            raise CommandError(
                f"Error: Ensure this value has at most 50 characters (it has {len(name)})."
            )
        elif Company.objects.filter(name=name).exists():
            if name != company:
                raise CommandError("Error: That name is already taken.")
        email = options["email"]
        if email == "":
            raise CommandError("Email cannot be blank.")
        elif email and not re.fullmatch(email_regex, email):
            raise CommandError("Error: Enter a valid email address.")
        phone = options["phone"]
        if phone == "":
            raise CommandError("Phone cannot be blank.")
        elif phone and not re.fullmatch(phone_regex, phone):
            raise CommandError("Error: Phone number format is not valid.")
        description = options["description"]
        data = {}
        if name and name != "":
            data["name"] = name
        if email and email != "":
            data["email"] = email
        if phone and phone != "":
            data["phone"] = phone
        if description and description != "":
            data["description"] = description
        self.stderr.write(f"{name},{email},{phone},{description}")
        c.update(**data)
