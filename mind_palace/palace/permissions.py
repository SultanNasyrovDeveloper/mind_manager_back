from mind_palace.core.permissions import IsObjectOwnerOrRead


class IsMindPalaceOwner(IsObjectOwnerOrRead):

    owner_field_name = 'user_id'
