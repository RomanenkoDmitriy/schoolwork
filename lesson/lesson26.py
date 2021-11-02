class Dequeue:

    def __init__(self):
        self._items = []

    def add_to_tail(self, element):
        self._items.append(element)

    def add_to_head(self, element):
        self._items.insert(0, element)

    def pop_from_tail(self):
        return self._items.pop()

    def pop_from_head(self):
        return self._items.pop(0)

    @property
    def empty(self):
        return not bool(self._items)

