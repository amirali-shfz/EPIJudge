from test_framework import generic_test


def evaluate(expression: str) -> int:
    expr_array = expression.split(',')
    ops = {'+': (lambda x, y: x + y), '*': (lambda x, y: x * y),
           '/': (lambda y, x: int(x / y)), '-': (lambda y, x: x - y)}
    stack = []

    for e in expr_array:
        if e in ops:
            stack.append(ops[e](stack.pop(), stack.pop()))
        else:
            stack.append(int(e))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
