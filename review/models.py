from django.db import models

# Create your models here.
class Review(models.Model):
    book_title = models.CharField(max_length=200)
    rating = models.IntegerField()
    detail = models.TextField()

    def __str__(self):
        return self.book_title