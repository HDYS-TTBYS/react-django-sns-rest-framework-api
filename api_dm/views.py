from rest_framework import authentication, permissions
from api_dm import serializers
from core.models import Message
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class MessageViewSet(viewsets.ModelViewSet):
    """
    メッセージのCRUD
    """
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        GET
        """
        return self.queryset.filter(sender=self.request.user)

    def perform_create(self, serialiser):
        """
        POST
        """
        serialiser.save(sender=self.request.user)

    def destroy(self, requrst, *args, **kwargs):
        """
        DELETE
        """
        response = {"message": "Delete is not allowd!"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        POST
        """
        response = {"message": "Update is not allowd!"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        PATCH
        """
        response = {"message": "Patch is not allowd!"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class InboxListView(viewsets.ReadOnlyModelViewSet):
    """
    受取人が自分のメッセージ一蘭を取得
    """
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(reciver=self.request.user)
