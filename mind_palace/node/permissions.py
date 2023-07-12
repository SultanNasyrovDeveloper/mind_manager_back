from mind_palace.core.permissions import IsObjectOwnerOrRead


class IsNodeBodyOwner(IsObjectOwnerOrRead):

    owner_field_name = 'node.owner_id'
