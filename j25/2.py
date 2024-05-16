# A simple generator for Fibonacci Numbers
def fib(limit):

    # Initialize first two Fibonacci Numbers
    a, b = 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


for i in fib(5):
    print(i, end = " ")
