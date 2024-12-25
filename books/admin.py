from django.contrib import admin
from .models import Author, Series, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'series', 'book_status', 'genre', 'book_type', 'favorite')
    list_filter = ('book_status', 'genre', 'book_type', 'favorite')
    search_fields = ('title',)
    ordering = ('title',)
