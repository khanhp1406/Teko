from django.db import models
from django.conf import settings
import json
# Create your models here.
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

class UserClick(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, default = 'id_tiki', on_delete=models.CASCADE)
    timeClick = models.DateTimeField(auto_now=True)

class ContentSimilarityBook(models.Model):
    id_tiki = models.IntegerField()
    title_similarity = models.CharField(max_length=255)
    descript_similarity = models.CharField(max_length=255)
        
    def set_title_similarity(self, x):
        self.title_similarity = json.dumps(x)

    def get_title_similarity(self):
        return json.loads(self.title_similarity)
    
    def set_descript_similarity(self, x):
        self.descript_similarity = json.dumps(x)

    def get_descript_similarity(self):
        print(self.descript_similarity)
        return json.loads(self.descript_similarity[:-1])

class CollabFilteringRsBook(models.Model):
    id_tiki = models.IntegerField()
    rs1 = models.CharField(max_length=255)

    def set_rs1(self, x):
        self.rs1 = json.dumps(x)

    def get_rs1(self):
        return json.loads(self.rs1[:-1]) 