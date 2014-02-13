__author__ = "jay"

class Queue():
    """
    A Queue ADT implementation with FRONT as last index and REAR as 0 index
    """
    def __init__(self):
       self.items = []

    def enqueue(self, item):
       self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
       return self.items == [] 

    def size(self):
        return len(self.items)

#class Queue():
    """
    A Queue ADT implementation with FRONT as 0 index and REAR as last index
    """
#   def __init__(self):
#       self.items = []
#
#   def enqueue(self, item):
#       self.items.append(item)
#
#   def dequeue(self):
#       self.items.remove(0)
#
#   def isEmpty(self):
#       return self.items == []
#
#   def size(self):
#       return len(self.items)

