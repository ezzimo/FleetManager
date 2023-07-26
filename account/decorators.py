from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .models import User
from .views import dashboard

"""
def administration_only(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.user_type == User.UserTypes.ADMINISTRATION:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
"""


class AdministrationOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.user_type == User.UserTypes.ADMINISTRATION:
            return redirect("account:dashboard")  # replace 'home' with the name of your home view
        return super().dispatch(request, *args, **kwargs)