
from rest_framework.permissions import IsAuthenticated,IsAdminUser , BasePermission

from . import models


class IsPresenter(BasePermission):
    """
    Allows access only to authenticated Presenter.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.job == "presenter")
