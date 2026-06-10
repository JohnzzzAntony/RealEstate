from rest_framework import permissions

class RoleBasedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.role == 'SUPER_ADMIN':
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        # Specific role mapping
        role = request.user.role
        if role == 'PROPERTY_MANAGER':
            return view.basename in ['properties', 'units', 'subtenants']
        elif role == 'FINANCE_OFFICER':
            return view.basename in ['billing']
        elif role == 'LEASE_ADMIN':
            return view.basename in ['leases', 'subleases', 'subtenants']
        elif role == 'LEGAL_COMPLIANCE':
            return view.basename in ['leases', 'ejari', 'documents']

        return False

class RoleRequiredMixin:
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.role == 'SUPER_ADMIN' or request.user.role in self.allowed_roles:
            return super().dispatch(request, *args, **kwargs)
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
