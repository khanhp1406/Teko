from django.db import models

# Create your models here.
class Book(models.Model):
    id_tiki = models.IntegerField()
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    short_description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    thumnail = models.CharField(max_length=500)
    
    class Meta:
        managed = False
        db_table = 'book'

class Bookdetail(models.Model):
    id_tiki = models.IntegerField()
    rating_average = models.FloatField()
    review_count = models.IntegerField()
    order_count = models.IntegerField()
    book_cover = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bookdetail'

