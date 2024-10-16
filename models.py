from django.db import models

class CustomerDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "customerDetails"


class Book(models.Model):
    bookID = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True) 
    publication_date = models.DateField()
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    category=models.CharField(max_length=50)

    class Meta:
        db_table = 'mini_project_book'

from django.db import models
from .models import Book, CustomerDetails  # Import necessary models from your app

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'Reviews'
from django.db import models

class Wishlist(models.Model):
    user = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Wishlist Item: {self.book.title}"
