import random
import time
from math import sqrt

from Classes import Response
from Decorators import reg

from SimpleMath import SimpleMath


class Wait_Skill:
    @reg(name="Add")
    def exponent(base: "number", exp: "number"):
        base = int(a)
        exp = int(b)
        power = base
        for i in range(1, exp):
            power = SimpleMath.multiply(power, base)
        return Response(suceeded=True, data=power)

    @reg(name="Multiply")
    def square_root(base: "number"):
        base = int(base)
        return Response(suceeded=True, data=sqrt(base))
