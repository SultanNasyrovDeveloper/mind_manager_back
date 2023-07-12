from mind_palace.core.permissions import IsObjectOwnerOrRead


class IsSessionOwner(IsObjectOwnerOrRead):

    owner_field_name = 'user_id'
