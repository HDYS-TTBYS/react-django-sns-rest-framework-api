from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from api_user import serializers
from core.models import Profiel, FriendRequest
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from core import cousompermissions


class CreateUserView(generics.CreateAPIView):
    """
    ユーザー作成
    """
    serializer_class = serializers.UserSerializer


class FriendRequestViewSet(viewsets.ModelViewSet):
    """
    フレンドリクエストのCRUD
    """
    queryset = FriendRequest.objects.all()
    serializer_class = serializers.FriendRequestSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        GET
        """
        return self.queryset.filter(Q(askTo=self.request.user) | Q(askFrom=self.request.user))

    def perform_create(self, serialiser):
        """
        POST
        """
        try:
            serialiser.save(askFrom=self.request.user)
        except:
            raise ValidationError("User can have only unique request")

    def destroy(self, requrst, *args, **kwargs):
        """
        DELETE
        """
        response = {"message": "Delete is not allowd!"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        PATCH
        """
        response = {"message": "Patch is not allowd!"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    プロフィールのCRUD
    """
    queryset = Profiel.objects.all()
    serializer_class = serializers.ProfielSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,
                          cousompermissions.ProfilePermissions,)

    def perform_create(self, serializer):
        """
        POST
        """
        serializer.save(userPro=self.request.user)


class MyProfileListView(generics.ListAPIView):
    """
    プロフィールの取得
    """
    queryset = Profiel.objects.all()
    serializer_class = serializers.ProfielSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        GET
        """
        return self.queryset.filter(userPro=self.request.user)
