from stack import Stack

# Evaluating the paranthesis
# Starting with an empty stack, process the parenthesis from left to right.
# If a symbol is an opening parenthesis, push it on the stack,
# as a signal that a corresponding closing symbol needs to appear later.
# If, on the other hand, a symbol is a closing parenthesis, pop the stack.
# As long as it is possible to pop the stack to match every closing symbol,
# the parentheses remain balanced.
# If at any time there is no opening symbol on the stack,
# to match a closing symbol, the string is not balanced properly.
# At the end of the string, when all symbols have been processed,
# the stack should be empty.
def evaluate_paranthesis(expression):
    """
    Evaluate the paranthesis in a given expression.
    
    Arguements:
        expression: a string which only contains paranthesis.
    Returns:
        Boolean: True if balanced, else False.
    Raises:
        None
    """
    stack = Stack()
    expression = expression.replace(" ", "")
    for i in expression:
        if i == "(":
            stack.push(i)
        elif i == ")":
            try:
                stack.pop()
            except IndexError:
                return False
        else:
            return "Invalid symbol!"
    if stack.isEmpty():
        return True
    else:
        return False

# Each opening symbol is simply pushed on the stack,
# to wait for the matching closing symbol to appear later in the sequence.
# When a closing symbol does appear, the only difference is that,
# we must ensure that it correctly matches the type of the opening symbol,
# on top of the stack.
# If the two symbols do not match, the string is not balanced.
# If the entire string is processed and nothing is left on the stack,
# the string is correctly balanced.
def evaluate_general_braces(expression):
    """
    Evaluate the braces in a given expression
    
    Arguements:
        expression: a string which only contains braces.
    Returns:
        Boolean: True if balanced, else False.
    Raises:
        None
    """
    stack = Stack()
    expression = expression.replace(" ", "")
    for i in expression:
        if i in "{[(":
            stack.push(i)
        elif i in ")]}":
            try:
                if is_matching(stack.peek(), i):
                    stack.pop()
                else:
                    return False
            except IndexError:
                return False
        else:
            return "Invalid symbol!"
    if stack.isEmpty():
        return True
    else:
        return False

def is_matching(opening_brace, closing_brace):
    """
    Evaluates if the opening and the closing braces matches.
    
    Arguments:
        opening_brace: a character
        closing_brace: a character
    Returns:
        Boolean: True if balanced, else False.
    Raises:
        None
    """
    openers = "{[("
    closers = "}])"
    return openers.index(opening_brace) == closers.index(closing_brace)

def main():
    string = "(()))"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = ")(())"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "((())"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "((()))"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "(()())"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "((()))"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "(()())"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "{{([][])}()}"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "[ ] [ ] [ ] ( ) { }"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "( [ ) ]"
    print "%s: %s" % (string, evaluate_general_braces(string))
    string = "( ( ( ) ] ) )"
    print "%s: %s" % (string, evaluate_general_braces(string))


if __name__ == "__main__":
    main()
