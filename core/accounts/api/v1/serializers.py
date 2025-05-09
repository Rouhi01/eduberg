from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'password1']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({
                'detail':'passwords does not match'
            })
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({
                'password': list(e.messages)
            })
        return super().validate(attrs)
        
    def create(self, validated_data):
        validated_data.pop('password1')
        return User.objects.create_user(**validated_data)
    

class ChangePassSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password_confirm'):
            raise serializers.ValidationError({
                'detail':'Passwords do not match.'
            })
        try:
            validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({
                'new password': list(e.messages)
            })
        
        return attrs