# A simple generator for Fibonacci Numbers
def fib(limit):
    a, b = 0, 1
    # Initialized first two Fibonacci Numbers 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b 
# Create a generator object
x = fib(5)
# Iterating over the generator object using for
# in loop.
for i in fib(5): 
    print(i)
