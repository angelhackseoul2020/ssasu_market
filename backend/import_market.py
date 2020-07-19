import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "angelhack.settings")
django.setup()

from market.models import Market

CSV_PATH = './datainput/market_info_02.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        Market.objects.create(
            name = row['name'],
            road_address = row['road_address'],
            address = row['address'],
            latitude = row['latitude'] if row['latitude'] else 0,
            longitude =  row['longitude'] if row['longitude'] else 0,
            phone = row['phone'],
            store_num = row['store_num'],
            cluster_key = row['cluster_key']
        )
    print("done")
        