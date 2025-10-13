from sympy import *


"""
Модуль для вычисления производных с использованием библиотеки SymPy.
"""
def derivative(expression: str, variable: str) -> str:
    """
    Calculate the derivative of a mathematical expression with respect to a given variable.
    
    Parameters:
        expression: mathematical expression as a string
        variable: variable of differentiation
    
    Returns:
        String representation of the derivative or error message
    """
    try:
     result = diff(expression, variable)
     return result
    except Exception:
       print("Некорректный синтаксисис")
       
if __name__=="__main__":
   test_cases = [
    ("x**2", "x"),
    ("sin(x)", "x"),
    ("x^2", "x"), ("x**", "x"), ("log(x)", "x"),
    ("x*y + y**2", "y"), ("x + ", "x")
]

for expr, var in test_cases:
    result = derivative(expr, var)
    if result is not None:
     print(f"Производная {expr} по {var}: {result}")