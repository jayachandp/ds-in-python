__author__ = "jay"

from deque import Deque

def is_palindrome(string):
    """
    Checks whether the given string is a palindrome or not.
    Uses Deque to solve the problem

    Arguments:
        string: Any string

    Returns: 
        Boolean: True if palindrome, else False
    Raises:
        None
    """
    deque = Deque()
    [deque.add_front(i) for i in string]
    while deque.size() > 1:
        if deque.remove_front() != deque.remove_rear():
            return False
    return True

def main(string):
    print "%s is palindrome? %s" % (string, is_palindrome(string))

if __name__ == "__main__":
    string = raw_input("Enter a string: ")
    main(string)
