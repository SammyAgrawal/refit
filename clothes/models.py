from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Clothing(models.Model):
    name = models.CharField(max_length=50,default="")
    #image = models.ImageField(upload_to='clothes/', blank=True, null=True)
    brand = models.TextField(max_length=100, default="")
    def __str__(self):
        return(self.name)


class Pictures(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    #src = models.ImageField(upload_to="pictures/")
    size = models.CharField(max_length=7, default="M")
    #user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, default="Anonymous")
    def __str__(self):
        return (str(self.user)+" " + str(self.clothing))


def thing