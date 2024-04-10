from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    on_stock=models.BooleanField(default=True)
    category=models.ManyToManyField(Category)
    author= models.ManyToManyField(Author)



class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

