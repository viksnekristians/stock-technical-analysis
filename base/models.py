from django.db import models
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=2)

    class Meta:
        db_table = 'g_countries'
