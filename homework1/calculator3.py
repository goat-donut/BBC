def operation(num1: float, num2: float, znak: str) -> float:
    if znak == "+":
        return float(num1 + num2)
    elif znak == "-":
        return float(num1 - num2)
    elif znak == "*":
        return float(num1 * num2)
    elif znak == "/":
        return float(num1 / num2)
print(operation(66.5, 77.3, "*"))