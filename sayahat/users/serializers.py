from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)  
    last_name = serializers.CharField(required=True)  
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True, max_length=15, write_only=True)  
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}) 
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','email', 'phone_number', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match!'})
        return data

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number')  
        validated_data.pop('password2')  
        email = validated_data['email']
        username = email  
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User.objects.create_user(username=username, email=email,first_name = first_name,last_name= last_name, password=validated_data['password'])
        Profile.objects.create(user=user, phone_number=phone_number)
        return user



class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'email', 'bio', 'profile_picture', 'phone_number']
