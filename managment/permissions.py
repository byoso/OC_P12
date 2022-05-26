from rest_framework.permissions import BasePermission


class EmployeeMixin():
    """Contains methods that are used in :
    - EmployeePermission"""

    def user_groups(self, request):
        groups = [group.name for group in request.user.groups.all()]
        user = request.user  # debug
        print("=== user: ", user)  # debug
        print("=== user groups: ", groups)  # debug
        return groups

    def get_assignee(self, obj):
        assignee = obj.assignment.employee
        print("=== object's assignee: ", assignee)  # debug
        return assignee


class EmployeePermission(EmployeeMixin, BasePermission):
    pass