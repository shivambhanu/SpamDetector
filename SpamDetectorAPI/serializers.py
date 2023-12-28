from rest_framework import serializers
from .models import User, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_phone']


class UserContactsSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['username', 'contacts']