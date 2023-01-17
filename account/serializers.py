from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'last_name', 'first_name', 'username', 'avatar')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Passwords did\'t match!')
        if not attrs['password'].isalnum():
            raise serializers.ValidationError('Password field must contain alpha and numeric symbols!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
