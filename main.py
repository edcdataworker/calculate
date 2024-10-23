from programm_to_calculate.calculator import calculate

if __name__=="__main__":
    a = 2
    b = 0
    operators = ["+", "-", "*", "/"]
    for operator in operators :
        print(f"le calcul {a} {operator} {b} le résultat est {calculate(a,b,operator)}")