from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=60)
    category=models.CharField(max_length=100)
    price=models.FloatField()

    def __str__(self):
        return self.name
    


class Country(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name=models.CharField(max_length=100)
    population=models.IntegerField()
    country=models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name