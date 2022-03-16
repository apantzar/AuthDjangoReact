from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):

    is_uni = models.BooleanField()
    is_dep = models.BooleanField()

    def __str__(self):
        return self.username


class Secretariat(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        
        







