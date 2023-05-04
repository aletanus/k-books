from rest_framework import permissions


class IsAllowedForCollaboratorsOrStudentsOnlyOfHisOwn(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.is_superuser:
            return True
        elif request.user.is_authenticated and obj.student and obj == request.user:
            return True
        return False
