from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Users can only edit their profile, Admins can delete all."""
        if request.method in permissions.SAFE_METHODS:  
            return True 

        if request.method == "DELETE":
            return request.user.is_staff  # Only admin can delete

        return obj.user == request.user  # Users can only edit their own profile
