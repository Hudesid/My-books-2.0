from django.contrib import admin
from .models import Book_list

@admin.register(Book_list)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'isbn', 'page_numbers', 'book_languages', 'book_genre')

#admin.site.register(Book_list)
