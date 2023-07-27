from django.shortcuts import redirect

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
        if not request.user.is_authenticated or request.user.user_type != 'ad':
            return redirect("account:dashboard")  
        return super().dispatch(request, *args, **kwargs)