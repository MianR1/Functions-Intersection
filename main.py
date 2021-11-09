def newton2(f, g, fprime, eps, guess=1, occur=0):

    if abs(f(guess) - g(guess)) > eps and occur < 994:
        nextGuess = guess - ((f(guess) - g(guess)) / fprime(guess))
        occur += 1
        return newton2(f, g, fprime, eps, nextGuess, occur)
    else:
        return guess


def intersect(f, g, a, b, eps):
    newFuncDer = lambda x: ((f(x + 0.0001) - f(x)) / 0.0001) - ((g(x + 0.0001) - g(x)) / 0.0001)
    return newton2(f, g, newFuncDer,eps,b)

# Example:
# f1 = lambda x: 2*x + 3
# g1 = lambda x: 3*x - 4
# x = intersect(f1, g1, -10, 10, 0.001)