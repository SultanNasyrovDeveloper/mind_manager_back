from operator import attrgetter


from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsObjectOwner(BasePermission):

    owner_field_name: str = 'owner_id'

    def has_object_permission(self, request, view, obj):
        try:
            owner_id = attrgetter(self.owner_field_name)(obj)
        except AttributeError:
            owner_id = None
        is_object_owner = owner_id and owner_id == request.user.id
        return is_object_owner


class IsObjectOwnerOrRead(BasePermission):

    owner_field_name: str = 'owner_id'

    def has_object_permission(self, request, view, obj):
        try:
            owner_id = attrgetter(self.owner_field_name)(obj)
        except AttributeError:
            owner_id = None
        is_object_owner = owner_id and owner_id == request.user.id
        return is_object_owner or request.method in SAFE_METHODS
