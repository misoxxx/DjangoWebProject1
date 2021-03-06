"""
Definition of models.
"""

from django.db import models
import json

# Create your models here.

class ShopItem(models.Model):
    item_file = models.CharField(max_length=100)
    item_id = models.CharField(max_length = 100)
    product = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.URLField()
    imgurl = models.URLField()
    price_vat = models.CharField(max_length = 25)    

    def __unicode__(self):
        return self.product
 