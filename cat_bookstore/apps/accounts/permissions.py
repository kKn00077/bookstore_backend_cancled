from rest_framework import permissions
from apps.profiles.models import OwnerUserProfile

class IsOwnerAuthenticated(permissions.BasePermission):
    message = "Account isn't owner"

    def has_permission(self, request, view):
        account=request.user

        if not account.is_authenticated:
            return False

        try:
            account.owner_profile
            return True
        except OwnerUserProfile.DoesNotExist:
            # account.profile
            return False