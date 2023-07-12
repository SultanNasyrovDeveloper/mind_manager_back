from mind_palace.core.enums import DjangoChoicesEnum


class MoveToPositionChoices(DjangoChoicesEnum):

    first_child = 'first-child'
    last_child = 'last-child'
    left = 'left'
    right = 'right'
