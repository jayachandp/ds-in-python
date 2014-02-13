__author__ = "jay"

from stack import Stack

def reverse_string(string):
    """
    Reverses the string.
    
    Arguments:
        string: any string.
    Returns:
        A string which is reversed.
    Raises:
        None
    """
    stack = Stack()
    reversed_string = []
    for i in string:
        stack.push(i)
    while not stack.isEmpty():
        reversed_string.append(stack.pop())
    return "".join(reversed_string)

def main():
    string = "apple"
    print "Reverse of '%s' is '%s'" % (string, reverse_string(string))

if __name__ == '__main__':
    main()
