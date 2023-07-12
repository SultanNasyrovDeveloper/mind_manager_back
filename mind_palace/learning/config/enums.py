from mind_palace.core.enums import DjangoChoicesEnum


class LearningCardField(DjangoChoicesEnum):

    name = 'name'
    description = 'title'
    body = 'body'
    media = 'media'