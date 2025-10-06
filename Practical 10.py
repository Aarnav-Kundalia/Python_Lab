import math
def f(x):
    return x - 5 - 5*math.exp(-x)

def bisection(f, lower_limit, upper_limit, tol, max_iter):
    f_left, f_right = f(lower_limit), f(upper_limit)
    if f_left == 0:
        return lower_limit, 0
    if f_right == 0:
        return upper_limit, 0
    if f_left * f_right > 0:
        raise ValueError("f(a) and f(b) should be of opposite sign")
    for i in range(1, max_iter+1):
        middle_value = (lower_limit + upper_limit)/2
        fm = f(middle_value)
        if abs(fm) < tol or (b - a)/2 < tol:
            return middle_value, i, tol
        if f_left * fm < 0:
            upper_limit, f_right =  middle_value, fm
        else:
            lower_limit, f_left = middle_value, fm
    return (lower_limit + upper_limit)/2, max_iter, tol

a,b,tol,max_iter = 0, 100, 1e-3, 100
answer, iteration_number, tolerence = bisection(f, a, b, tol, max_iter)
print("Answer= ", answer, "Number of Iterations taken= ", iteration_number, "at tolerence= ", tolerence)