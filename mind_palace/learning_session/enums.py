from mind_palace.core.enums import DjangoChoicesEnum


class QueueGenerationStrategyEnum(DjangoChoicesEnum):
    random = 1
    outdated_first = 2
    # last_repeated_first = 3
