from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(max_length=50)
    address = models.CharField(max_length=200, blank=True)
    message = models.TextField(max_length=300)

    def __str__ (self):
        return self.name
    
class Blogs(models.Model):
    names = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comments = models.TextField(max_length=200)

    def __str__ (self):
        return self.names