from programm_to_calculate.addition import calculate_addition
from programm_to_calculate.division import calculate_division
from programm_to_calculate.multiplication import calculate_multiplication
from programm_to_calculate.substract import calculate_substraction

def calculate (a: float, b: float, operator: str) -> float:
    if operator not in ("+","-","*","/"):
        print ("error de mongole operator where is it ???")
        return None
    elif operator == "+":
        return calculate_addition(a,b)

    elif operator == "-":
        return calculate_substraction(a,b)

    elif operator == "*":
        return calculate_multiplication(a,b)

    elif operator == "/":
        return calculate_division(a,b)

    return None
 