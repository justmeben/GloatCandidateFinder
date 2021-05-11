from django.core.management.base import BaseCommand, CommandError
from CandidateFinder.services.sample_data_service import generate_sample_data


class Command(BaseCommand):
    help = 'Initializes the DB with sample data'

    def handle(self, *args, **options):
        generate_sample_data()
