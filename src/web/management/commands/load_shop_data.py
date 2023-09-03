from csv import DictReader
from pathlib import Path

from django.core.management import BaseCommand
from web.models import Shop


class Command(BaseCommand):
    help = "Loads data from shops.csv"

    def handle(self, *args, **options):

        if Shop.objects.exists():
            print('shop data already loaded...exiting.')
            exit(0)

        print("Loading shop data")

        shop_path = Path('data') / Path('shops.csv')
        csv_reader = DictReader(shop_path.open())
        for row in csv_reader:
            shop = Shop(category=row['Category'], shipper=row['Shipper'], website=row['Website'])
            shop.save()
