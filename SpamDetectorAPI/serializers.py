from rest_framework import serializers
from .models import User, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone', 'password', 'email']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['user', 'contact_name', 'contact_phone']


# # class UserContactsSerializer(serializers.ModelSerializer):
# #     contacts = ContactSerializer(many=True)
    
# #     class Meta:
# #         model = User
# #         fields = ['username', 'contacts']