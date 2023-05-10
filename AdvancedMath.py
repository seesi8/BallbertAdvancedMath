import random
import time
from math import sqrt

from Hal.Classes import Response
from Hal.Decorators import reg

from Skills.SimpleMath import SimpleMath


class AdvancedMath:
    @reg(name="Exponent")
    def exponent(base: "number", exp: "number"):
        base = int(a)
        exp = int(b)
        power = base
        for i in range(1, exp):
            power = SimpleMath.multiply(power, base)
        return Response(suceeded=True, data=power)

    @reg(name="Square Root")
    def square_root(base: "number"):
        base = int(base)
        return Response(suceeded=True, data=sqrt(base))
    
    @reg(name="Get Number")
    def get_num(self):
        num = self.get("my_number")
        return Response(suceeded=True, data=num)
    
    
