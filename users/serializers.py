from .models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})


class UserSerializerInfo(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length = 50)
    password = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'})

    def validate(self,data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Enter password and confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Confirm password error.")
        return data


    def validate_email(self,email):
        exist= User.objects.filter(email=email).first()
        if exist:
            raise serializers.ValidationError("User with such email has already registered.")
        return email

    def validate_username(self,username):
        exist= User.objects.filter(username=username).first()
        if exist:
            raise serializers.ValidationError("User with such username has already registered.")
        return username

    def create(self, validated_data):
        user = User.objects.create_user(email = validated_data['email'],username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
