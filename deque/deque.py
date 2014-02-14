__author__ = "jay"

class Deque():
    """
    A Deque ADT implementation using list with last index as FRONT 
    and 0 index as REAR
    """
    def __init__(self, *args):
        self.items = list(args)

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop()

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[-1]

    def rear(self):
        return self.items[0]

class DequeR():
    """
    A Deque ADT implementation using list with 0 index as FRONT 
    and last index as REAR
    """
    def __init__(self, *args):
        self.items = list(args)

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def add_rear(self, item): 
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]
