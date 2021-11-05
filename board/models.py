from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=30)
