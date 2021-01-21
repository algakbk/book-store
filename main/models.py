from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)