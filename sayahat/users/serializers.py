from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True) 
    first_name = serializers.CharField(required=True)  
    last_name = serializers.CharField(required=True)  
    phone_number = serializers.CharField(required=True, max_length=15)  
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match!'})
        return data

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number')  
        validated_data.pop('password2')  

        user = User.objects.create_user(**validated_data)

        Profile.objects.create(user=user, phone_number=phone_number)

        return user



class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'email', 'bio', 'profile_picture', 'phone_number']