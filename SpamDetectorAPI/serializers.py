from rest_framework import serializers
from .models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['username', 'phone', 'password', 'email']


# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = ['contact_name', 'contact_phone']


# # class UserContactsSerializer(serializers.ModelSerializer):
# #     contacts = ContactSerializer(many=True)
    
# #     class Meta:
# #         model = User
# #         fields = ['username', 'contacts']