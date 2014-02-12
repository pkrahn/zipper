def add1(x): return x+1
def double(x): return 2*x
def square(x): return x*x

import sys
my_functions=[add1, double, square]
for f in my_functions:
    print f(float(sys.argv[1]))
