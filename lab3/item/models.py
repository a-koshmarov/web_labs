from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.TextField(unique=True)
    price = models.TextField()
