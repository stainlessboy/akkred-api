from functools import partial
from operator import is_not

from rest_framework.permissions import BasePermission, DjangoModelPermissions as BaseDjangoModelPermission

from main.models import User


class IsSaveMethod(BasePermission):
    save_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', ]

    def has_permission(self, request, view):
        return request.method in self.save_methods


class IsAuthenticated(IsSaveMethod):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and
                super(IsAuthenticated, self).has_permission(request, view))


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ['PUT', 'POST']:
#             user = getattr(request, 'user', None)
#             if user.user_type == User.ADMIN:
#                 return True
#             executor = getattr(user, 'executor', None)
#             client = getattr(user, 'client', None)
#             current_user = next(filter(partial(is_not, None), [executor, client, False]))
#             if not current_user:
#                 return False
#             return (
#                     getattr(obj, 'owner', None) == current_user or
#                     obj == current_user
#             )


class IsExecutor(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['PUT', 'POST']:
            return bool(request.user.executor)
        return True


class IsClient(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['PUT', 'POST']:
            return bool(request.user.client)
        return True


class IsClientOrExecutor(BasePermission):
    def has_permission(self, request, view):
        return any([request.user.client, request.user.executor])


class DjangoModelPermissions(BaseDjangoModelPermission):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
