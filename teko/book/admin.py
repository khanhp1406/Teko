from django.contrib import admin
from .models import Book, Author, Puplisher, Authored
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'publisher' ,'cost']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

class PuplisherAdmin(admin.ModelAdmin):
    list_display = ['name']
class AuthoredAdmin(admin.ModelAdmin):
    list_display = ['book', 'author']
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Puplisher, PuplisherAdmin)
admin.site.register(Authored, AuthoredAdmin)