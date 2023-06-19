import random
import time
from math import sqrt

from Hal.Classes import Response
from Hal.Decorators import reg
from Hal.Skill import Skill

from Hal import initialize_assistant
assistant = initialize_assistant()


class AdvancedMath(Skill):
    def __init__(self):
        self.my_num = 0
    
    @reg(name="Exponent")
    def exponent(self, base, exp):
        """
        Calculate the exponentiation of base raised to the power of exp.
        
        Args:
            base (number): The base number.
            exp (number): The exponent number.
        
        Returns:
            Response: The response object with the calculated power.
        """
        base = int(base)
        exp = int(exp)
        power = base
        for i in range(1, exp):
            power = assistant.call_function("simplemath.multiply", (power, base)).data
        return Response(suceeded=True, data=power)

    @reg(name="Square Root")
    def square_root(self, base):
        """
        Calculate the square root of a given number.
        
        Args:
            base (number): The number to calculate the square root of.
        
        Returns:
            Response: The response object with the calculated square root.
        """
        base = int(base)
        return Response(suceeded=True, data=sqrt(base))
    
    @reg(name="Get My Number")
    def get_my_num(self):
        """
        Get the value of the 'my_num' attribute.
        
        Returns:
            Response: The response object with the current value of 'my_num'.
        """
        return Response(suceeded=True, data=self.my_num)
    
    @reg(name="Get Number")
    def get_num(self, thing):
        """
        Get the 'my_number' value and increment 'my_num' attribute.
        
        Args:
            thing: Placeholder argument.
        
        Returns:
            Response: The response object with the current value of 'my_number'.
        """
        num = self.get("my_number")
        if self.my_num:
            self.my_num += 1
        else:
            self.my_num = 222
        return Response(suceeded=True, data=num)
