from django.core.management.base import BaseCommand, CommandError
from CandidateFinder.services.sample_data_service import generate_sample_data, clean_all_data


class Command(BaseCommand):
    help = 'Resets DB then initializes the DB with sample data'

    def handle(self, *args, **options):
        clean_all_data()
        generate_sample_data()
