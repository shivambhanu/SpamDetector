from django.db import models


# Create your models here.
class AppUser(models.Model):
    username = models.CharField(max_length=127)
    phone = models.CharField(primary_key=True,max_length=15)
    password = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username


class Contact(models.Model):
    parent_user = models.ForeignKey(AppUser, related_name='contacts' ,on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.contact_name



# class PhoneBook(models.Model):
#     phone = models.CharField(max_length=255)
#     def __str__(self) -> str:
#         return self.phone