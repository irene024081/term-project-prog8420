from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User


class Command(BaseCommand):
    help: str = "Create Admin User"

    # def add_arguments(self, parser: CommandParser) -> None:
    #     parser.add_argument("client_id", type=str, nargs=None, help="Twitter client id")
    #     parser.add_argument(
    #         "client_secret", type=str, nargs=None, help="Twitter client secret"
    #     )

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("username", type=str, nargs=None, help="Admin username")
        parser.add_argument("email", type=str, nargs=None, help="Admin email")
        parser.add_argument("password", type=str, nargs=None, help="Admin password")

    def handle(self, *args, **options):
        if not User.objects.filter(is_staff=True).exists():
            User.objects.create_superuser(
                username=options["username"],
                email=options["email"],
                password=options["password"],
                is_staff=True,
            )
            self.stdout.write(self.style.SUCCESS("Admin user created successfully"))
        else:
            self.stdout.write(self.style.WARNING("Admin user already exists"))