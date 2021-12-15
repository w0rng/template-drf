from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from apps.user.models import User


class UserCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class AuthUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'created')


class UserChangePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def validate_password1(self, password):
        validate_password(password)
        return password

    def validate_password2(self, password):
        validate_password(password)
        return password

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise ValidationError(detail='Пароли не совпадают')
        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password1'])
        instance.save()
        return self.instance


class UserWriteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password2 = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'password2')

    def validate_password(self, password):
        validate_password(password)
        return password

    def validate_password2(self, password):
        validate_password(password)
        return password

    def validate(self, attrs):
        if 'password2' in attrs and 'password' in attrs:
            if attrs['password'] != attrs['password2']:
                raise ValidationError(detail='Пароли не совпадают')
        return super().validate(attrs)

    def create(self, validated_data):
        password2 = validated_data.pop('password2')

        user = User.objects.create(**validated_data)
        user.set_password(password2)
        user.save()

        return user

    def update(self, instance, validated_data):
        if 'password2' in validated_data and 'password' in validated_data:
            validated_data.pop('password2')
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()

        return super().update(instance, validated_data)
