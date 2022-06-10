from rest_framework.permissions import BasePermission


class EmployeeMixin():
    """Contains methods that are used in :
    - ClientPermission
    - ContractPermission
    - EventPermission"""

    def user_groups(self, request):
        groups = [group.name for group in request.user.groups.all()]
        return groups

    def get_assignee(self, obj, filter_kwarg):
        self.employees = obj.assignment.filter(
            **filter_kwarg).filter(date_revoked=None)

        if len(self.employees) > 0:
            assignee = self.employees[len(self.employees)-1].employee
        else:
            assignee = None
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
        assignee = self.get_assignee(obj, {'client_id': obj.id})
        if assignee is None:
            return False
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
        assignee = self.get_assignee(obj, {'contract_id': obj.id})
        if assignee is None:
            return False
        if 'sale' in self.user_groups(request):
            if view.action in ['retrieve', 'update', 'partial_update'] and \
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
        assignee = self.get_assignee(obj, {'event_id': obj.id})
        if assignee is None:
            return False
        if 'support' in self.user_groups(request):
            if view.action in ['retrieve', 'update', 'partial_update'] and \
                    request.user == assignee:
                return True
        return False
