"""

In the Fibonacci sequence, each number is the sum of the two preceding ones.
Starting from 0 and 1, the sequence looks like this:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

"""


def fib(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


print(fib(5))