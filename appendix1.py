#!/usr/bin/python
# Copyright TJ Leone, 2012
# Released under MIT license
# http://www.opensource.org/licenses/mit-license.php
# Python version of programs in Albert Cuoco's *Investigations in Algebra*
# Appendix. Tools.

import copy
import sys
import math
import fractions
import scipy
import scipy.linalg
if sys.version_info<(2,6,0):
    try:
        import Numeric as mathx
    except ImportError:
      sys.stderr.write("You need to install Numeric\n")
      exit(1)
else:
    try:
        import numpy as mathx
    except ImportError:
      sys.stderr.write("You need to install numpy\n")
      exit(1)

## ------------------------------------------------------
## APPENDIX
## ------------------------------------------------------

## =============================================================================
# The test() function below is from:
#   Google's Python Class
#   http://code.google.com/edu/languages/google-python-class/
# ------------------------------------------------------------------------------
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if match(got, expected):
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def cascade(n, f, *args):
    result = args[0]
    for i in range(n):
        result = f(result)
##    if len(args) > 1:
##        handle other pairs of func, arg
    return result

def match(a, b, tolerance=0.0001):
    if type(None) in [type(a), type(b)]:
        return a == b
    if float in [type(a), type(b)]:
        return abs(a-b) < tolerance
    return a == b

def alt_tab(function, start, end):
    flist = str(function).split()
    print("function " + flist[1] + " from " + str(start) + " to " + str(end))
    return [function(x) for x in range(start,end)]

def is_number(s):
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        return False

def b(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - (k - (i+1)))
        c = c // (i+1)
    return c

"""
In the table below, n refers to the natural numbers, S(n) is the sum of n terms,
d1 is the first difference, being the differences between two successive
sums. d2 is the second difference, being the differences between successive
d2 values, etc.

The table can be used to find the formula for a series.

First we generate some values for analysis, using integral values beginning at 1.
Then we compute the differences between these values (the first differences) and
successively compute the differences between the differences until we reach a
repeating constant value (successive differences will be zero). 

The difference (first, second, etc) at which we reach this constant value is the
degree of the polynomial generating the values. For instance, in the table below,
we have some values for various n's. The differences have been computed in the table.

We begin with the following function:

def g119_recursive(x):
    if x == 1:
        return 2
    return x*(x+1) + g119_recursive(x-1)

Here is its differences table:

>>> differences(g119_recursive,1,10,4)
function g119_recursive from 1 to 10
n	1	2	3	4	5	6	7	8	9	10	
S(n)	2	8	20	40	70	112	168	240	330	440	
d1	0	6	12	20	30	42	56	72	90	110	
d2	0	0	6	8	10	12	14	16	18	20	
d3	0	0	0	2	2	2	2	2	2	2	
d4	0	0	0	0	0	0	0	0	0	0

The degree of the table above is 3, so the formula is of the form:

an**3 + bn**2 + cn + d = S(n)

Substituting in n=1, n=2, n=3, and n=4, we get the following:

(n=1)   a + b + c + d = 2
(n=2)   8a + 4b + 2c + d = 8
(n=3)   27a + 9b + 3c + d = 20
(n=4)   64a + 16b + 4c + d = 40

To solve this system, use scipy.linalg:

>>> A = scipy.mat('[1 1 1 1; 8 4 2 1; 27 9 3 1; 64 16 4 1]')
>>> b = scipy.mat('[2;8;20;40]')
>>> scipy.linalg.solve(A,b)
array([[  3.33333333e-01],
       [  1.00000000e+00],
       [  6.66666667e-01],
       [  6.66133815e-16]])

The desired coefficients are a = 1/3, b = 1, c = 2/3, d = 0

The desired closed version of the function is:

def g119_closed(x):
    return (x**3 + 3*x**2 + 2*x) / 3

Finally, notice that the degree of the table is 3 with a constant difference of 2,
a = 1/3, and 3! * (1/3) = 2

Reference:
    http://www.trans4mind.com/personal_development/mathematics/series/polynomialEquationDifferences.htm
"""
def differences(function, start, end, deltas):
    dmatrix = []
    dmatrix.append(range(start,end+1))
    m = map(function, range(start,end+1))
    dmatrix.append(m)
    for d in range(deltas):
        dlist = []
        for i in range(d+1):
            dlist.append(0)
        for i in range(d, len(m)-1):
            dlist.append(m[i+1]-m[i])
        m=dlist
        dmatrix.append(dlist)
    flist = str(function).split()
    print( "function " + flist[1] + " from " + str(start) + " to " + str(end))
    pretty_matrix = []
    pretty_matrix.append(['n'] + dmatrix[0])
    pretty_matrix.append(['S(n)'] + dmatrix[1])
    i = 0
    for dlist in dmatrix[2:]:
        i += 1
        pretty_matrix.append(['d' + str(i)] + dmatrix[i+1])
    print_matrix(pretty_matrix)

def print_matrix(m):
    for i in range(len(m)):
        row = ""
        for j in m[i]:
            row += str(j) + "\t"
        print(row)
    print()

    
## p. 597 -----------------------------------------------

## ......................................................
## List Processing
## ......................................................

def emptyp(l):
    return len(l) == 0

def first(l):
    return l[0]

def second(l):
    return l[1]

def last(l):
    return l[-1]

def bf(l):
    return l[1:]

def but_first(l):
    return bf(1)
        
def bl(l):
    return l[:-1]

def but_last(l):
    return bl(l)

def item(n,l):
    return l[n]

def list_all(*args):
    return list(args)

def se(*args):
    return do_se(list(args))

def do_se(l):
    """Flattens the list or tuple l. Helper function for se().

    Args:
        l: A function name.
    Returns:
        Flattened list.
    Note:
        There are a number of sequence types besides lists and tuples. These
        include str, unicode, bytearray, buffer, and xrange. An xrange is
        always flat to begin with, so we don't have to check for it. The
        other sequence types won't be used in this course, so I'm not
        giving them any special treatment. --TJ
    """
    s = []
    for item in l:
        if type(item) in [type([]), type(())]:
            s += item
        else:
            s.append(item)
    return s

def sentence(l):
    return se(l)

def fput(i,l):
    return [i] + l

def lput(i,l):
    return l + [i]

def appl(f, applist):
    return f(*applist)


## p. 603 -----------------------------------------------

def setitem(m, ob, l):
    assert m < len(l)
    if type(ob) in [type([]), type(())]:
        return l[:m] + ob + l[m+1:]
    a=copy.deepcopy(l)
    a[m] = ob
    return a

## ......................................................
## Apply and Tabulations
## ......................................................
"""In Python, you don't have to use the APPLY trick that is used
   in Logo. You can just pass the function name directly.
"""

## p. 604 -----------------------------------------------

def tab604(function, start, end):
    flist = str(function).split()
    print( "function " + flist[1] + " from " + str(start) + " to " + str(end))
    for i in range(start,end+1):
        print( str(i) + ". . ." + str(function(i)))
    print()

def tab(function, start, end, *args, **keywords):
    if 'step' in keywords.keys():
        step = keywords['step']
    else:
        step=1
    flist = str(function).split()
    print("function " + flist[1] + " from " + str(start) + " to " + str(end))
    arglist = list(args)
    for i in range(start,end+1,step):
        print( str(i) + ". . ." + str(function(*(arglist + [i]))))
    print()

##############def tab(function, start, end, *args, **keywords):
    """Creates a function table.

    Args:
        function: A function name.
        start:    Starting input.
        end:      Last input.
        step:     Step size. If step is positive, the last element is the
                  largest start + i * step less than stop; if step is negative,
                  the last element is the smallest start + i * step greater
                  than stop. step must not be zero (or else ValueError is
                  raised).
        *args:    Other arguments for the function (if more than one is needed).
    Returns:
        None. Prints out table of inputs for a given function. Examples:
        
            >>> tab(f21,1,5)
            function f21 from 1 to 5
            1. . .4
            2. . .5
            3. . .6
            4. . .7
            5. . .8
            
            >>> tab(geo_series158, 1, 20, 2, 3)
            function geo_series158 from 1 to 20
            1. . .2
            2. . .8
            3. . .26
            4. . .80
            5. . .242
            6. . .728
            7. . .2186
            8. . .6560
            9. . .19682
            10. . .59048
            11. . .177146
            12. . .531440
            13. . .1594322
            14. . .4782968
            15. . .14348906
            16. . .43046720
            17. . .129140162
            18. . .387420488
            19. . .1162261466
            20. . .3486784400

    See below for a definition of f21()
    See chapter_06.py for a definition of geo_series158()
    See Appendix (page 605) for extended Logo version of tab()
    """
   ###### if 'step' in keywords.keys():
        ######step = keywords['step']
    ######else:
       ############ step=1
    ######flist = str(function).split()
   ###### print("function " + flist[1] + " from " + str(start) + " to " + str(enda))
   ###### arglist = list(args)
   ###### for i in range(start,end+1,step):
       ###### print( str(i) + ". . ." + str(function(*(arglist + [i]))))
    ######print()

def tabv(function, start, end, *args, **keywords):
    if 'step' in keywords.keys():
        step = keywords['step']
    else:
        step=1
    flist = str(function).split()
    print( "function " + flist[1] + " from " + str(start) + " to " + str(enda))
    arglist = list(args)
    for i in range(start,end+1,step):
        if function(*(arglist + [i])):
            print( str(i) + ". . ." + str(function(*(arglist + [i]))))
    print()

def tabc(f1,f2, start, end, *args, **keywords):
    if 'step' in keywords.keys():
        step = keywords['step']
    else:
        step=1
    f1list = str(f1).split()
    f2list = str(f2).split()
    print( "composite of functions " + f1list[1] + " and " + f2list[1] + " from " + str(start) + " to " + str(enda))
##    print "function " + f1list[1] + " from " + str(start) + " to " + str(end)
    arglist = list(args)
    for i in range(start,end+1,step):
        print( str(i) + ". . ." + str(f1(f2(*(arglist + [i])))))
    print()

def rtab(function, start, end, *args, **keywords):
    """Creates a function table.

    Args:
        function: A function name.
        start:    Starting input.
        end:      Last input.
        step:     Step size. If step is positive, the last element is the
                  largest start + i * step less than stop; if step is negative,
                  the last element is the smallest start + i * step greater
                  than stop. step must not be zero (or else ValueError is
                  raised).
        *args:    Other arguments for the function (if more than one is needed).
                  Input is added to front of arglist instead of back as with tab.
    Returns:
        None. Prints out table of inputs for a given function.
"""
    if 'step' in keywords.keys():
        step = keywords['step']
    else:
        step=1
    flist = str(function).split()
    print( "function " + flist[1] + " from " + str(start) + " to " + str(enda))
    arglist = list(args)
    for i in range(start,end+1,step):
        print(str(i) + ". . ." + str(function(*([i] + arglist))))
    print()

def tab2(f1, f2, start, end, step=1, **keywords):
    f1_list = f2_list = []
    if 'f1args' in keywords.keys():
        f1_args = keywords['f1args']
    if 'f2args' in keywords.keys():
        f2_args = keywords['f2args']
    f1list = str(f1).split()
    f2list = str(f2).split()
    header = "functions " + str(f1list[1])
    header += "(" + str(f1_args) + ",)"
    header += " and " + str(f2list[1])
    header += "(" + str(f2_args) + ",)"
    header += " from " + str(start) + " to " + str(end)
    print(headear)
    for i in range(start,end+1,step):
        tabline = str(i) + ". . ." + str(f1(*(f1_args + [i])))
        tabline += ". . ." + str(f2(*(f2_args + [i])))
        print(tabline)
    print()


def tab3(f1, f2, f3, start, end, step=1, **keywords):
    f1_list = f2_list = f3_list = []
    if 'f1args' in keywords.keys():
        f1_args = keywords['f1args']
    if 'f2args' in keywords.keys():
        f2_args = keywords['f2args']
    if 'f3args' in keywords.keys():
        f3_args = keywords['f3args']
    f1list = str(f1).split()
    f2list = str(f2).split()
    f3list = str(f3).split()
    header = "functions " + str(f1list[1])
    header += "(" + str(f1_args) + ",)"
    header += " and " + str(f2list[1])
    header += "(" + str(f2_args) + ",)"
    header += " and " + str(f3list[1])
    header += "(" + str(f3_args) + ",)"
    header += " from " + str(start) + " to " + str(end)
    print(header)
    for i in range(start,end+1,step):
        tabline = str(i) + ". . ." + str(f1(*(f1_args + [i])))
        tabline += ". . ." + str(f2(*(f2_args + [i])))
        tabline += ". . ." + str(f3(*(f3_args + [i])))
        print( tabline)
    print()
    
    

## p. 607 -----------------------------------------------

## ......................................................
## Accumulations
## ......................................................

def simple_sigma(f,m,n):
    return sum(f(i) for i in range(m,n+1))

def sigma(f,*args):
    arglist = list(args)
    return do_sigma(f,arglist[:-2], arglist[-2], arglist[-1])

def do_sigma(f,extra,m,n):
    return sum(f(*(extra + [i])) for i in range(m,n+1))

def rsigma(f,*args):
    arglist = list(args)
    return do_rsigma(f,arglist[:-2], arglist[-2], arglist[-1])

def do_rsigma(f,extra,a,b):
    return sum(f(*([i] + extra)) for i in range(m,n+1))

def sigma_l(f, *args):
    arglist = list(args)
    return do_sigma_l(f,arglist[:-1], arglist[-1])

def do_sigma_l(f, extra, list_of_combs):
    if len(list_of_combs) == 0:
        return 0
    x = appl(f, se(extra, len(list_of_combs[0])))
    y = do_sigma_l(f, extra, list_of_combs[1:])
    return x + y

def unique_combos(combolist):
    l = []
    for item in combolist:
        if not permutation_found(item, l):
            l.append(item)
    return l

def permutation_found(i,l):
    for item in l:
        if isa_permutation(item,i):
            return True
    return False
    
def isa_permutation(a,b):
    if len(a) != len(b):
        return False
    for item in a:
        if not item in b:
            return False
    return True

def prod(f,*args):
    arglist = list(args)
    return do_prod(f,arglist[:-2], arglist[-2], arglist[-1])

def do_prod(f,extra,m,n):
    return mathx.prod(list(f(*(extra + [i])) for i in range(m,n+1)))

def one(x):
    return 1

def ident(x):
    return x

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def binomial(n,k):
    return factorial(n) / (factorial(k)*factorial(n-k))


