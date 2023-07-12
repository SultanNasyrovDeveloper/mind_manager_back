from typing import Optional


get_first_or_none = lambda array: next(iter(array), None)
get_by_index_or_none = lambda array, index: array[index] if len(array) == index else None


class LearningQueueManager:

    def __init__(self, learning_session) -> None:
        self.session = learning_session
        self.queue = self.session.queue
        self.additional_queue = self.session.additional_queue

    def __contains__(self, item):
        return item in self.queue

    def current(self) -> int:
        current = get_first_or_none(self.queue)
        if not current:
            current = get_first_or_none(self.additional_queue)
        return current

    def next(self) -> Optional[int]:
        next_node = None
        match len(self.queue):
            case 0:
                next_node = get_by_index_or_none(self.additional_queue, 1)
            case 1:
                next_node = get_first_or_none(self.additional_queue)
            case _:
                next_node = get_first_or_none(self.queue)
        return next_node

    def add(self, node_id: int) -> None:
        self.queue.append(node_id)

    def remove(self, node_id: int) -> None:
        print(self.queue)
        self.queue.remove(node_id)

    def add_additional_node(self, node_id: int) -> None:
        self.additional_queue.append(node_id)

    def remove_additional_node(self, node_id: int) -> None:
        self.additional_queue.remove(node_id)

