from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    - Users can **view and edit only their own profile**.
    - Admins can **view, edit, and delete all profiles**.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Users can only see their own profile unless they are admin."""
        if request.user.is_staff:  # Admins can do anything
            return True

        return obj.user == request.user  # Users can only access their profile
