from rest_framework.permissions import BasePermission

class IsRole(BasePermission):
    """
    Permite acceso solo a usuarios con role incluido en allowed_roles.
    Uso: permission_classes = [IsRole] y pasar allowed_roles en la view (atributo)
    """

    def has_permission(self, request, view):
        allowed = getattr(view, 'allowed_roles', None)
        if allowed is None:
            return True  
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role in allowed
