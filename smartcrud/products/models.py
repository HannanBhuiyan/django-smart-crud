from cProfile import label
from django.db import models
import os
import datetime

from account.models import Category, Subcategory

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (timenow, old_filename)
    return os.path.join('uploads/', filename)



class Product(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Pending', 'Pending')
    )
    product_title = models.CharField(max_length=255)
    product_desc = models.TextField(max_length=500)
    product_price = models.FloatField()
    product_varient = models.CharField(max_length=255)
    in_stock = models.IntegerField()
    product_slug = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to=filepath, null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)