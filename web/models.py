from django.db import models

# Create your models here.

from django.db import models


class Shop(models.Model):
    # Excessively large length but you never know.
    # https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/
    category = models.CharField(max_length=200)
    shipper = models.CharField(max_length=200)
    website = models.URLField()
