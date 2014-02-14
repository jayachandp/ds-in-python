__author__ = "jay"

class Queue():
    """
    A Queue ADT implementation with FRONT as last index and REAR as 0 index
    """
    def __init__(self, *args):
       self.items = list(args)

    def enqueue(self, item):
       self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
       return self.items == [] 

    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[-1]
    
    def rear(self):
        return self.items[0]
    

class QueueR():
    """
    A Queue ADT implementation with FRONT as 0 index and REAR as last index
    """
    def __init__(self, *args):
       self.items = list(args)
   
    def enqueue(self, item):
       self.items.append(item)
   
    def dequeue(self):
       return self.items.pop(0)
   
    def is_empty(self):
       return self.items == []
   
    def size(self):
       return len(self.items)
    
    def front(self):
        return self.items[0]
    
    def rear(self):
        return self.items[-1]
    

def main():
    queue = Queue(1, 2, 3, 4)
    print "The elements of queue are :%s" % (queue.items)
    queue.enqueue(5)
    print "Enqueuing an element."
    print "The elements of queue are :%s" % (queue.items)
    queue.dequeue()
    print "Dequeuing an element."
    print "The elements of queue are :%s" % (queue.items)
    queuer = QueueR(1, 2, 3, 4)
    print "The elements of queue are :%s" % (queuer.items)
    queuer.enqueue(5)
    print "Enqueuing an element."
    print "The elements of queue are :%s" % (queuer.items)
    queuer.dequeue()
    print "Dequeuing an element."
    print "The elements of queue are :%s" % (queuer.items)

if __name__ == '__main__':
    main()
