func = lambda x: x**2 -x -1
derivative = lambda x: 2*x -1
#initial_guess = 1.5
epsilon = 1.0e-3
N = 10


def root_newton_method(func,derivative,intial_guess,epsilon,N):
    x_n = intial_guess
    print(x_n)
    for n in range(0,N):
        print(x_n)
        fxn = func(x_n)
        print(fxn)
        if abs(fxn) < epsilon:
            print("Found soln after",n,"iteration",x_n)
            return x_n
        Dfxn = derivative(x_n)
        if Dfxn == 0:
            print("Zero Derivative. No Solution Found")
            return None
        x_n = x_n- fxn/Dfxn
    print("Exceeded maximum iterations. No solution found.")
    return None

root_newton_method(func,derivative,1.1,epsilon,N)
