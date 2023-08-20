from mind_palace.core.enums import DjangoChoicesEnum


class NodeBodyTypeEnum(DjangoChoicesEnum):

    TEXT = 'text'
    CODE = 'code'
    CHESS = 'chess'
    TRANSLATION = 'translation'


class NodeMediaTypeEnum(DjangoChoicesEnum):

    not_set = 1
    youtube = 2
