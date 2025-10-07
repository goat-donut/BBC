import math
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def classic(num1: float, num2: float, znak:str) -> float:
        if znak == "+":
            return num1 + num2
        elif znak == "-":
            return num1 - num2
        elif znak == "*":
            return num1 * num2
        elif znak == "/":
            return num1 / num2
    def inzh(num1: float, znak: str) -> float:
        if znak == "sin":
            return math.sin(num1)
        elif znak == "cos":
            return math.cos(num1)
        elif znak == "tan":
            return math.tan(num1)
        elif znak == "log":
            return math.log(num1)
        elif znak == "sqrt":
            return math.sqrt(num1)


