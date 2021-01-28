from rest_framework import permissions


class ProfilePermissions(permissions.BasePermission):
    """
    docstring
    """

    def has_object_permission(self, request, view, obj):
        """
        docstring
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.userPro.id == request.user.id
