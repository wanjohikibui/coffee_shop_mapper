from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.


class CoffeeTypes(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    types_of_coffee = models.ManyToManyField(CoffeeTypes)
    street_name = models.CharField(max_length=50)
    location = gis_models.PointField(srid=4326)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    geom = gis_models.LineStringField(srid=4326)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=4, unique=True)
    geom = gis_models.PolygonField(srid=4326)

    def __str__(self):
        return self.name
