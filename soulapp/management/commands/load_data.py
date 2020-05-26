from load_data import Scraper
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'loads data from reddit'

    def handle(self, *args, **kwargs):
        scraper = Scraper()
        scraper.load_data()
        scraper.write_data()

        self.stdout.write("loading data...")
