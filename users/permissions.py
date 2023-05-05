from rest_framework import permissions


class IsAllowedForCollaboratorsOrStudentsOnlyOfHisOwn(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.is_superuser:
            return True
        elif request.user.is_authenticated and obj.student and obj == request.user:
            return True
        return False


class IsAccountCollaborator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsAccountStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.student


class IsStudentOrCollaboratorViewingStudents(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.student or request.user.is_superuser)
        )
