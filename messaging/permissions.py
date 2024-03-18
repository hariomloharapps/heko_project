from rest_framework import permissions

class AllowAll(permissions.BasePermission):
    """
    Custom permission to allow all actions.
    """
    def has_permission(self, request, view):
        """
        Allow all actions.
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Allow all actions on object level.
        """
        return True