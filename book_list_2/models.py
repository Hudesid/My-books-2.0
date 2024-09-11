from django.db import models


class Book_list(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    page_numbers = models.PositiveIntegerField()
    book_languages = models.CharField(max_length=30)
    book_genre = models.CharField(max_length=50)


    def __str__(self):
        return self.title

