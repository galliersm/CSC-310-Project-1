# A Python project for interpreting postfix notation.
import operator

from stack import Stack


# Class for interpreting postfix notation.
class Postfix:
    # Dictionary of operators and associated functions for evaluating.
    OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    def __init__(self):
        # Stack object to be used for postfix interpretation.
        self.stack = Stack()

    # Evaluates a postfix expression.
    def evaluate(self, expr):
        # Iterate through each char in the expression.
        for item in expr:
            # Ignore whitespace.
            if item == ' ':
                continue
            # If the char is a digit, push it to the stack.
            elif '0' <= item <= '9':
                self.stack.push(int(item))
            # Otherwise, it is an operator.
            else:
                # Pop off the last two numbers and save them.
                num2 = self.stack.pop()
                num1 = self.stack.pop()
                # Evaluate them using the given operator function from operators dictionary.
                res = self.OPERATORS[item](num1, num2)
                # Push result back onto stack.
                self.stack.push(res)
        # Pop and return the last item on the stack, the result of evaluating the expression.
        return self.stack.pop()


if __name__ == '__main__':
    # Create new Postfix instance.
    postfix = Postfix()
    # Print some information about the program.
    print('Welcome to the Postfix expression evaluator program by Michael Galliers')
    print('Please enter postfix expressions using only single digit numbers and')
    print('the following operators: (\'*\', \'/\', \'+\', and \'-\')')
    # Set to False when the user wants to exit.
    restart = True
    # User input loop.
    while restart:
        # Prompt the user for expression.
        expr = input('Enter expression: ')
        # Obtain result.
        res = postfix.evaluate(expr)
        # Print result.
        print('The result of your expression is: {0}'.format(res))
        # Ask if user wants to enter another expression.
        answer = input('Would you like to enter another expression? (y, n): ')
        # If they do not want to proceed, update restart var to False.
        if answer.lower() == 'n':
            restart = False
            print('Thank you for using the program.')
