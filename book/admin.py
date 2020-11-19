from django.contrib import admin
from .models import Book, Bookdetail
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['id_tiki', 'name', 'category','short_description','discount', 'price', 'thumnail']
    
class BookDetailAdmin(admin.ModelAdmin):
    list_display = ['id_tiki', 'rating_average', 'review_count', 'order_count', 'book_cover', 'publisher', 'author']


admin.site.register(Book, BookAdmin)  
admin.site.register(Bookdetail, BookDetailAdmin)