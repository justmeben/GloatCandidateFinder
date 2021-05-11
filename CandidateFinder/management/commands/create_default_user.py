from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from CandidateFinder.services.sample_data_service import generate_sample_data, clean_all_data


class Command(BaseCommand):
    help = 'Creates default user (resets password if exists)'

    def handle(self, *args, **options):
        u, _ = User.objects.get_or_create(username='ben', email='ben@ben.com', is_staff=True, is_superuser=True)
        u.set_password('123')
        u.save()
