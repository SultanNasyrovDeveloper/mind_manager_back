from mind_palace.core.enums import DjangoChoicesEnum


class NodeBodyTypeEnum(DjangoChoicesEnum):

    TEXT = 'text'
    CODE = 'code'
    CHESS = 'chess'
    TRANSLATION = 'translation'


class NodeMediaTypeEnum(DjangoChoicesEnum):

    NOT_SET = 'not_set'
    IMAGE = 'image'
    YOUTUBE = 'youtube'
