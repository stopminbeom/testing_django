from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)


class OpenApi(models.Model):
    item_name = models.CharField(max_length=32)
    kind_name = models.CharField(max_length=32)
    rank = models.CharField(max_length=8)
    unit = models.CharField(max_length=8)
