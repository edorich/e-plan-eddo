from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def validate(self, data):
        password = data.get('password')

        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            serializers_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password': serializers_errors['non_field_errors']}
            )

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
