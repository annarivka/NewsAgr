from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} ({self.code})'


class CountryFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='storage/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    country = models.ManyToManyField(Country)


