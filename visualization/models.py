from django.db import models
# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)