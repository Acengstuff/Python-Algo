"""
https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
"""
from math import factorial, pi


def maclaurin_sin(theta: float, accuracy: int = 30) -> float:
    """
    Finds the maclaurin approximation of sin

    :param theta: the angle to which sin is found
    :param accuracy: the degree of accuracy wanted minimum ~ 1.5 theta
    :return: the value of sine in radians


    >>> from math import isclose, sin
    >>> all(isclose(maclaurin_sin(x, 50), sin(x)) for x in range(-25, 25))
    True
    >>> maclaurin_sin(10)
    -0.544021110889369
    >>> maclaurin_sin(-10)
    0.5440211108893703
    >>> maclaurin_sin(10, 15)
    -0.5440211108893689
    >>> maclaurin_sin(-10, 15)
    0.5440211108893703
    >>> maclaurin_sin("10")
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires either an int or float for theta
    >>> maclaurin_sin(10, -30)
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires a positive int for accuracy
    >>> maclaurin_sin(10, 30.5)
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires a positive int for accuracy
    >>> maclaurin_sin(10, "30")
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires a positive int for accuracy
    """

    if not isinstance(theta, (int, float)):
        raise ValueError("maclaurin_sin() requires either an int or float for theta")

    if not isinstance(accuracy, int) or accuracy <= 0:
        raise ValueError("maclaurin_sin() requires a positive int for accuracy")

    theta = float(theta)
    div = theta // (2 * pi)
    theta -= 2 * div * pi
    return sum(
        (((-1) ** r) * ((theta ** (2 * r + 1)) / factorial(2 * r + 1)))
        for r in range(accuracy)
    )


if __name__ == "__main__":
    print(maclaurin_sin(10))
    print(maclaurin_sin(-10))
    print(maclaurin_sin(10, 15))
    print(maclaurin_sin(-10, 15))