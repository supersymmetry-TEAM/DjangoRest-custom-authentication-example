from rest_framework import serializers
from .models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( "avatar")


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "avatar",
            "first_name",
            "last_name",
            "username",
            "password",
            'email',
        )
        read_only_fields = ("id", "avatar")

    def validate_first_name(self, value):
        return value.upper()

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user