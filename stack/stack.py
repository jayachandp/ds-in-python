__author__ = "jay"

# Stack implementation with last index as TOP
# Performance is good. O(1)
class Stack:
    """
    A Stack ADT implementation using list with last index as TOP
    """
    def __init__(self, *args):
        self.items = list(args)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# Stack implementation with first index as TOP
# Performance is poor. O(n). Reason being push() and pop() implementations.
#class Stack:
    """
    A Stack ADT implementation using list with first index as TOP
    """
#    def __init__(self, *args):
#        self.items = list(args)
#    
#
#    def push(self, item):
#        self.items.insert(0,item)
#    
#    def pop(self):
#        return self.items.pop(0)
#
#    def peek(self):
#        return self.items[0]
#
#    def is_empty(self):
#        return self.items == []
#
#    def size(self):
#        return len(self.items)
