
'''
This is a program to find root of equation f(x) = exp(x) * ln(x) - x * x = 0
using bisection method.





'''



def root_bisection(func,lower_estimate,higher_estimate,tolerance=1.0e-6):
    print(func(lower_estimate))
    print(func(higher_estimate))
    #if func(lower_estimate) * func(higher_estimate) > 0.0:
    #    print("No root lies between these values")
    #else:
    #    diff = abs(higher_estimate - lower_estimate)
    diff = abs(higher_estimate - lower_estimate)
    while diff > tolerance:
        x = (lower_estimate + higher_estimate)/2.0
       # print(func(x))
        check_val_1 = func(x)*func(lower_estimate)
        check_val_2 = func(x)*func(higher_estimate)
        if check_val_1 > 0:
           lower_estimate = x
        else:
            higher_estimate = x
        diff = abs(higher_estimate -lower_estimate)
    return x
