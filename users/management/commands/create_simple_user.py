from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@example.com',
            first_name='Simple',
            last_name='User'
        )
        user.set_password('0987')
        user.save()
