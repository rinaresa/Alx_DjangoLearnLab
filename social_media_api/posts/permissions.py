from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Allow safe methods for everyone. Only allow owners to edit/delete.
    """

    def has_permission(self, request, view):
        # allow list/create for authenticated users (modify as needed)
        if view.action in ["list", "retrieve", "create"]:
            return True if request.user and request.user.is_authenticated else (view.action == "list" or view.action == "retrieve")
        return True

    def has_object_permission(self, request, view, obj):
        # safe methods are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # obj expected to have attribute `author`
        try:
            return obj.author == request.user
        except AttributeError:
            return False
