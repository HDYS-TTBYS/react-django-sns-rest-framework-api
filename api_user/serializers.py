from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import Profiel, FriendRequest


class UserSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model = get_user_model()
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        docstring
        """
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ProfielSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        """
        docstring
        """
        model = Profiel
        fields = ("id", "nickName", "userPro", "created_on", "img")
        extra_kwargs = {"userPro": {"read_only": True}}


class FriendRequestSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model = FriendRequest
        fields = ("id", "askFrom", "askTo", "approved")
        extra_kwargs = {"askFrom": {"read_only": True}}
