"""

CPE 202
Project 2
Author:
    Tushar Sharma
"""

from StackArray import StackArray


def infix_to_postfix(infix_epr):
    """
    Converts infix to postfix operation by creating a stack to maintain order
    args:
        infix_epr(string): string turned into list and then evaluated into postfix list
    :return:
        post_fix(string): a list turned into a string to be evaluated in postfix notation
    """
    prec = {}
    prec['^'] = 4
    prec['~'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    post_fix = []
    token_list = infix_epr.split()
    opstack = StackArray()
    for token in token_list:
        if token.isdigit():
            post_fix.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            top_token = opstack.pop()
            while top_token is not "(":
                post_fix.append(top_token)
                top_token = opstack.pop()
        else:
            while (opstack.num_items > 0) and \
             (prec[opstack.peek()] > prec[token]):
                post_fix.append(opstack.pop())
            opstack.push(token)
    while opstack.num_items is not 0:
        post_fix.append(opstack.pop())
    return " ".join(post_fix)


def post_fix_eval(postfix_epr):
    """
    Evaluates a postfix expression and returns a value
    args:
        postfix_epr(string): a string in postfix notation
    returns:
        val(int): returns the value of the postfix
    """
    token_list = postfix_epr.split()
    operand_stack = StackArray()
    for token in token_list:
        if token is "+":
            val1 = operand_stack.pop()
            val2 = operand_stack.pop()
            new_val = float(val2) + float(val1)
            operand_stack.push(new_val)
        elif token is "-":
            val1 = operand_stack.pop()
            val2 = operand_stack.pop()
            new_val = float(val2) - float(val1)
            operand_stack.push(new_val)
        elif token is "*":
            val1 = operand_stack.pop()
            val2 = operand_stack.pop()
            new_val = float(val2) * float(val1)
            operand_stack.push(new_val)
        elif token is "/":
            val2 = operand_stack.pop()
            val1 = operand_stack.pop()
            if int(val2) == 0:
                raise ZeroDivisionError
            new_val = float(val1) / float(val2)
            operand_stack.push(new_val)
        elif token is "^":
            val1 = operand_stack.pop()
            val2 = operand_stack.pop()
            new_val = float(val2) ** float(val1)
            operand_stack.push(new_val)
        else:
            if token.isdigit():
                operand_stack.push(token)
            else:
                val1 = operand_stack.pop()
                new_val = float(val1)
                new_val = -(new_val)
                operand_stack.push(new_val)
    return operand_stack.pop()


def postfix_valid(postfix_epr):
    """
    Tests for an invalid postfix expression
    :param
        postfix_epr(string): a string in postfix notation
    :return:
        True: if postfix_epr is valid. Has the correct number and position of operations\
         and operators
        False: if postfix_epr is invalid.
    """
    token_list = postfix_epr.split()
    number_stack = StackArray()
    for token in token_list:
        if token.isdigit():
            number_stack.push(token)
        elif token == '^' or token == '+' or token == '/' or token == '*' or token == '-':
            if number_stack.num_items > 1:
                temp1 = number_stack.pop()
                temp2 = number_stack.pop()
                new_val = temp1 + temp2
                number_stack.push(new_val)
            else:
                return False
        else:
            if number_stack.num_items > 0:
                temp1 = number_stack.pop()
                new_val = -1 * temp1
                number_stack.push(new_val)
            else:
                return False
    if number_stack.num_items == 1:
        return True
    return False
