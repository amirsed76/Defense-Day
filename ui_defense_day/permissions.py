
from rest_framework.permissions import IsAuthenticated,IsAdminUser , BasePermission

from . import models
import datetime


class IsPresenter(BasePermission):
    """
    Allows access only to authenticated Presenter.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.job == "presenter")

class IsLogin(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user)

class IsProfessor(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.job == "professor")

class CanScore(BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(datetime.date.today() <= models.Event.objects.all()[0].end_date)
        except:
            return True

