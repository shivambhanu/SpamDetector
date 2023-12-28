from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(primary_key=True, max_length=15)
    email = models.EmailField(max_length=255, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name



# class Contacts(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     contact_name = models.CharField(max_length=255)
#     contact_phone = models.CharField(max_length=15)
    
#     def __str__(self) -> str:
#         return (f"{self.user__name}: {self.contact_name}")



# class PhoneBook(models.Model):
#     phone = models.CharField(max_length=255)
#     def __str__(self) -> str:
#         return self.phone