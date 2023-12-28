from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(primary_key=True, max_length=15)
    email = models.EmailField(max_length=255, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username
    
    #Sorting model instances by their names
    class Meta:
        ordering = ['username']



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