#!/usr/bin/python
# What is a function?
#import sys
#import appendix1
try:
    from appendix1 import *
except ImportError:
    sys.stderr.write(
        "You need appendix.py in the same directory as this file.\n")
    exit(1)

## ======================================================
## I. FUNCTIONS
## ======================================================

## ------------------------------------------------------
## 1. WHAT IS A FUNCTION?
## ------------------------------------------------------

##  ------------------------------------------------

## EXAMPLE 1
def f20(x):
    return 2*x

def g20(x):
    return x*x + 6*x - 7

def fahrenheit_to_celsius(t):
    return int((t - 32) * (5.0 / 9))

## ------------------------------------------------
def f21(x):
    return x+3

## ------------------------------------------------

## EXAMPLE 2

## Note: There's already a built-in Python function called
## abs(), so I'm naming this one absolute_value() --TJ
def absolute_value(x):
    if x > 0:
        return x
    return -x

## EXAMPLE 3
def area(length, width, height):
    return 2*(length*width+length*height+width*height)

##  ------------------------------------------------

## EXAMPLE 4
def digit(n):
    if n < 10:
        return n
    return digit(n - 10)

## This example is very inefficient for large numbers.
## Why is the following function a big improvement?
def units(n):
    if n < 10:
        return n
    return units(n % 10)

##------------------------------------------------
def count_numbers(n):
    if n == 1:
        return 1
    return n * count_numbers(n - 1)

## ------------------------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


## ------------------------------------------------
def power3(e):
    if e == 1:
        return 3
    return 3 * power3(e-1)

##  ------------------------------------------------
def power30a(n, e):
    if e == 1:
        return n
    return n * power30a(n, e-1)


def power30b(n, e):
    if e == 0:
        return 1
    return n * power30b(n, e-1)

##  ------------------------------------------------
## You need to implement rep_mult yourself!
def rep_mult(n,d,l):
    pass

def factorial32(n):
    return rep_mult(n,1,n)

def power32(n,e):
    return rep_mult(n,0,e)


## p. 34 ------------------------------------------------
## You need to implement fahrenheit_to_newgrade yourself!
def fahrenheit_to_newgrade34a(c):
    return (13.0 / 5) * c + 100

## You need to implement the hard version of celcius_to_newgrade yourself!
def celcius_to_newgrade34(t):
    pass

## Here's the easy version (once fahrenheit_to_newgrade and
## celsius_to_fahrenheit are done)
def celcius_to_newgrade34b(c):
    return fahrenheit_to_newgrade34(celsius_to_fahrenheit34(c))

def f34(x):
    return x * x + 3 * x - 2

def h34(x):
    return 4 * x * x + 10 * x + 2

## p. 35 ------------------------------------------------
def h35a(x):
    return f34(2 * x + 1)

def g35(x):
    return 2 * x + 1

def h35b(x):
    return f34(g35(x))

## Notice that in Python, you don't have to use the APPLY trick that
## is used in Logo. You can just pass the function name directly.
def composite(f, g, x):
    return f(g(x))

def celcius_to_newgrade(c):
    return composite(fahrenheit_to_newgrade, celsius_to_fahrenheit, c)

def h35c(x):
    return composite(f34,g35,x)

## p. 36 ------------------------------------------------
def scale(x):
    return (5.0 / 9) * x

def shift(x):
    return x - 32

def fahrenheit_to_celcius36(t):
    return composite(scale, shift, t)

##def simple(x):
##    return composite(fahrenheit_to_celsius, celsius_to_fahrenheit, t)

## p. 37 ------------------------------------------------
## There's an error in the text here. The first Logo program on the
## page should be:
##
## TO SUM :A :B
##   OP :A + :B
## END
##
def sum37(a,b):
    return a + b

def product37(a,b):
    return a * b

def bin37(x,y):
    return float(x) / y

def tabSuite():
    print("TABLES\n")
    tab(f20, 1, 5)
    tab(g20, 2, 23)
    tab(fahrenheit_to_celsius, 32, 212)
    
def testSuite():
    test(f20(2), 4)
    test(f20(0), 0)
    test(f20(-1), -2)
    test(count_numbers(5),120)
    test(factorial(0),1)
    test(factorial(3),6)
    test(power3(4),81)
    test(power30b(2,10),pow(2,10))
    test(power30b(10,0),1)
    test(h34(1),16)
    test(h35a(2),h34(2))
    test(h35b(3),h34(3))
    test(h35c(4),h34(4))
    
if __name__ == '__main__':
    tabSuite()
    testSuite()
