from django.db import models

# Create your models here.


class Book(models.Model):
    GENRE_CHOICES = (
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-fiction'),
        ('mystery', 'Mystery'),
        ('fantasy', 'Fantasy'),
        ('science_fiction', 'Science Fiction'),
        ('thriller', 'Thriller'),
        ('historical', 'Historical'),
        ('biography', 'Biography'),
        ('children', 'Children'),
        ('young_adult', 'Young Adult'),
    )
    code = models.CharField(max_length=20, unique=True)
    ISBN = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    author = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    available_for_loan = models.BooleanField(default=True)
    available_for_download = models.BooleanField(default=False)

    def calculate_location(genre, author, title):
    section = genre
    letter = author[0]
    number = calculate_number(author, title)
    return f"{section} - {letter}{number}"

    def __str__(self):
        return self.title


