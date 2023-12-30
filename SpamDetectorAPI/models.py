from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20)


class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts' ,on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return (f"{self.user.username}: {self.contact_name}")



# class PhoneBook(models.Model):
#     phone = models.CharField(max_length=255)
#     def __str__(self) -> str:
#         return self.phone