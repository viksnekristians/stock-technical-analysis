from django.core.management.base import BaseCommand
from assets.services.API.Alphavantage.alphavantage_api_client import AlphavantageApiClient
from assets.models import DailyAssetInfo, Asset
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        client = AlphavantageApiClient()

        all_assets = Asset.objects.all()

        for asset in all_assets:
            try:
                data = client.getDailyInfo(asset.symbol)
            except Exception as e:
                print(f"Error fetching data for {asset.symbol}: {e}")
                continue
                
            for day, values in data['Time Series (Daily)'].items():
                date=datetime.strptime(day, "%Y-%m-%d").date()

                try:
                    a = DailyAssetInfo.objects.get(
                        asset_id=asset.id,
                        date=date
                    )

                    if a:
                        print(f"record already exists for {asset.symbol} on {day}")
                        continue  # Skip the current iteration if the object exists
                except DailyAssetInfo.DoesNotExist:
                    daily = DailyAssetInfo(
                        asset_id = asset.id,
                        open = float(values['1. open']),
                        high = float(values['2. high']),
                        low = float(values['3. low']),
                        close = float(values['4. close']),
                        volume = int(values['5. volume']),
                        date =  datetime.strptime(day, "%Y-%m-%d").date()
                    )

                    daily.save()
                except DailyAssetInfo.MultipleObjectsReturned:
                    # Handle the case where multiple objects are found
                    print(f"Multiple records found for {asset.symbol} and date={day}")
