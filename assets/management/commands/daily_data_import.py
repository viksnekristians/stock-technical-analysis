from django.core.management.base import BaseCommand
from assets.Services.API.Alphavantage.alphavantage_api_client import AlphavantageApiClient
from assets.models import DailyAssetInfo
from datetime import datetime

class Command(BaseCommand):
    help = 'Run periodic task'

    def handle(self, *args, **kwargs):
        client = AlphavantageApiClient()
        data = client.getDailyInfo('IBM')
        for day, values in data['Time Series (Daily)'].items():
            date=datetime.strptime(day, "%Y-%m-%d").date()

            try:
                a = DailyAssetInfo.objects.get(
                    asset_id=5,
                    date=date
                )

                if a:
                    print(f"continuing={day}")
                    continue  # Skip the current iteration if the object exists
            except DailyAssetInfo.DoesNotExist:
                daily = DailyAssetInfo(
                    asset_id = 5,
                    open = float(values['1. open']),
                    high = float(values['1. open']),
                    low = float(values['1. open']),
                    volume = int(values['5. volume']),
                    date =  datetime.strptime(day, "%Y-%m-%d").date()
                )

                daily.save()
                print('saving ')
            except DailyAssetInfo.MultipleObjectsReturned:
                # Handle the case where multiple objects are found
                print(f"Multiple records found for asset_id=1 and date={day}")
