from django.core.management.base import BaseCommand, CommandError, CommandParser
from career.models import Company


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("names", nargs="*", type=str)
        parser.add_argument("--all", action="store_true")

    def handle(self, *args, **options):
        names = options["names"]
        all = options["all"]
        if all:
            Company.objects.all().delete()
        else:
            for name in names:
                try:
                    Company.objects.get(name=name).delete()
                except:
                    self.stderr.write(f"{name} matching query does not exist.")
