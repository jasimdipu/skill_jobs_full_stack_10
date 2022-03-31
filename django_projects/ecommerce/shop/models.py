from pydoc import describe
from unicodedata import name
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return self.name

