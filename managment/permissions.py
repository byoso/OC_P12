from rest_framework.permissions import BasePermission


class EmployeeMixin():
    """Contains methods that are used in :
    - EmployeePermission
    - AssigneEventPermission"""

    def user_groups(self, request):
        groups = [group.name for group in request.user.groups.all()]
        return groups


class EmployeePermission(EmployeeMixin, BasePermission):
    def has_permission(self, request, view):
        if 'managment' in self.user_groups(request):
            return True

    def has_object_permission(self, request, view, obj):
        if 'managment' in self.user_groups(request):
            return True
