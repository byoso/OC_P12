from rest_framework.permissions import BasePermission


class EmployeeMixin():
    """Contains methods that are used in :
    - ClientPermission
    - ContractPermission
    - EventPermission"""

    def user_groups(self, request):
        groups = [group.name for group in request.user.groups.all()]
        user = request.user  # debug
        print("=== user: ", user)  # debug
        print("=== user groups: ", groups)  # debug
        return groups

    def get_assignee(self, obj):
        try:
            assignee = obj.assignment.employee
        except AttributeError:
            assignee = None
        print("=== object's assignee: ", assignee)  # debug
        return assignee


class ClientPermission(EmployeeMixin, BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        if view.action == 'retrieve':
            return True
        if 'sale' in self.user_groups(request):
            if view.action in ['create', 'update', 'partial_update']:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        assignee = self.get_assignee(obj)
        if 'sale' in self.user_groups(request):
            if view.action in ['retrieve', 'update', 'partial_update'] and \
                    request.user == assignee:
                return True

        return False


class ContractPermission(EmployeeMixin, BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        if view.action == 'retrieve':
            return True
        if 'sale' in self.user_groups(request):
            if view.action in ['create', 'update', 'partial_update']:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        assignee = self.get_assignee(obj)
        if 'sale' in self.user_groups(request):
            if view.action in ['retrieve']:
                return True
            if view.action in ['update', 'partial_update'] and \
                    request.user == assignee:
                return True
        return False


class EventPermission(EmployeeMixin, BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        if view.action == 'retrieve':
            return True
        if 'support' in self.user_groups(request):
            if view.action in ['create', 'update', 'partial_update']:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        assignee = self.get_assignee(obj)
        if 'support' in self.user_groups(request):
            if view.action in ['retrieve']:
                return True
            if view.action in ['update', 'partial_update'] and \
                    request.user == assignee:
                return True
        return False
