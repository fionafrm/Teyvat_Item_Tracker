from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    category = models.TextField()
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)