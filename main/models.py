from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.fam


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Image(models.Model):
    title1 = models.CharField(max_length=100, null=True, blank=True)
    data1 = models.ImageField(upload_to='images/', null=True, blank=True)
    title2 = models.CharField(max_length=100, null=True, blank=True)
    data2 = models.ImageField(upload_to='images/', null=True, blank=True)
    title3 = models.CharField(max_length=100, null=True, blank=True)
    data3 = models.ImageField(upload_to='images/', null=True, blank=True)


class Level(models.Model):
    winter = models.CharField(max_length=50, null=True, blank=True)
    summer = models.CharField(max_length=50, null=True, blank=True)
    autumn = models.CharField(max_length=50, null=True, blank=True)
    spring = models.CharField(max_length=50, null=True, blank=True)


class Status(models.Model):
    status_name = models.CharField(max_length=50, default='new')


class Pass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100, null=True, blank=True)
    connect = models.CharField(max_length=10, null=True, blank=True)
    add_time = models.DateTimeField(default=timezone.now)
    coords = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    levels = models.ForeignKey(Level, on_delete=models.CASCADE)
    statuses = models.ForeignKey(Status, on_delete=models.CASCADE)
