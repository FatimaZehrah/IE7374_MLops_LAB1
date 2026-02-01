def fun1(x, y):
    """Add two numbers."""
    return x + y


def fun2(x, y):
    """Subtract y from x."""
    return x - y


def fun3(x, y):
    """Multiply two numbers."""
    return x * y


def fun4(x, y):
    """
    Combine results of fun1, fun2, fun3 and return their sum:
    fun4(x,y) = fun1(x,y) + fun2(x,y) + fun3(x,y)
    """
    return fun1(x, y) + fun2(x, y) + fun3(x, y)

def fun5(x, y):
    """Divide x by y."""
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y
