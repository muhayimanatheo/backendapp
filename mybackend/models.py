from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

    def _str_ (self):
        return self.name
