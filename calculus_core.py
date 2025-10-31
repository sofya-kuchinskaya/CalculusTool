from sympy import *


"""
Модуль для вычисления производных, в том числе n-го порядка, с использованием библиотеки SymPy.
"""
def derivative(expression: str, variable: str, order: int = 1) -> str:
    """
    Calculate the derivative of a mathematical expression with respect to a given variable.
    
    Parameters:
        expression: mathematical expression as a string
        variable: variable of differentiation
        order: order of derivative (default = 1)
    
    Returns:
        String representation of the derivative or error message
    """
    try:
     result = diff(expression, variable, order)
     return result
    except Exception:
       return "Некорректный синтаксис"
       
if __name__=="__main__":
   test_cases_1 = [
    ("x**2", "x"),
    ("sin(x)", "x"),
    ("x^2", "x"), ("x**", "x"), ("log(x)", "x"),
    ("x*y + y**2", "y"), ("x + ", "x")
]
   test_cases_2 = [("x**4", "x", 2),          
        ("sin(x)", "x", 2),         
        ("x**3", "x", 3),           
        ("exp(x)", "x", 4),        
        ("ln(x)", "x", 2), ("x", "x", 0),              
        ("5", "x", 2),             
        ("x", "x", 5), ("x**2", "y", 2),        
        ("", "x", 2),              
        ("x**", "x", 3), ("x**a", "x", 2), 
        ("sin(x", "x", 2) ]
   

   for expr, var in test_cases_1:
        result = derivative(expr, var)
        print(f"Производная {expr} по {var}: {result}")
   for expr, var, order in test_cases_2:
        result = derivative(expr, var, order)
        print(f"{order}-я производная {expr} по {var}: {result}")