from django.db import models
# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=32)
    type_id = models.PositiveIntegerField()
    country_id = models.PositiveIntegerField()
    market_id = models.PositiveIntegerField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'a_assets'

class AssetPrice(models.Model):
    asset_id = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    gmt = models.DateTimeField()

    class Meta:
        db_table = 'a_asset_prices'

class DailyAssetInfo(models.Model):
    asset_id = models.PositiveBigIntegerField()
    open = models.DecimalField(max_digits=12, decimal_places=2)
    high = models.DecimalField(max_digits=12, decimal_places=2)
    low = models.DecimalField(max_digits=12, decimal_places=2)
    close = models.DecimalField(max_digits=12, decimal_places=2)
    volume = models.PositiveIntegerField()
    date = models.DateField()
    
    class Meta:
        db_table = 'a_daily_asset_info'
        unique_together = ('asset_id', 'date')

class AssetType(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'a_asset_types'