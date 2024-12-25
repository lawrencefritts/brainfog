from django.db import models

BOOK_STATUS_CHOICES = [
    ("TR", "To Read"),
    ("TA", "To Acquire"),
    ("F", "Finished"),
    ("N4", "Not For Me"),
]

GENRE_CHOICES = [
    ("F", "Fiction"),
    ("SF", "Science Fiction"),
    ("FA", "Fantasy"),
    ("M", "Mystery"),
    ("H", "History"),
    ("O", "Other"),
]

BOOK_TYPE_CHOICES = [
    ("P", "Paper"),
    ("K", "Kindle"),
    ("A", "Audible"),
]

class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Series(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    series = models.ForeignKey(Series, null=True, blank=True, on_delete=models.DO_NOTHING)
    series_order = models.PositiveSmallIntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    book_status = models.CharField(max_length=2, choices=BOOK_STATUS_CHOICES)
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES)
    book_type = models.CharField(max_length=1, choices=BOOK_TYPE_CHOICES)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

