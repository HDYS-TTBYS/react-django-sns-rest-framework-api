from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import Message, User, Profiel, FriendRequest
from django.db.models import Q


class FriendFilter(serializers.PrimaryKeyRelatedField):
    """
    docstring
    """

    def get_queryset(self):
        """
        docstring
        """
        request = self.context["request"]
        friends = FriendRequest.objects.filter(
            Q(askTo=request.user) & Q(approved=True))
        list_friend = []
        for friend in friends:
            list_friend.append(friend.askFrom.id)
        query_set = User.objects.filter(id__in=list_friend)
        return query_set


class MessageSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    reciver = FriendFilter()

    class Meta:
        """
        docstring
        """
        model = Message
        fields = ("id", "message", "sender", "reciver")
        extra_kwargs = {"sender": {"read_only": True}}
