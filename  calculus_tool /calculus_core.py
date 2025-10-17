from sympy import symbols, diff, sympify, SympifyError, exp


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
        # Парсинг математического выражения
        expr = sympify(expression)
        
        # Создание символа для переменной дифференцирования
        var = symbols(variable)
        
        # Вычисление производной
        result = diff(expr, var)
        
        return str(result)
        
    except SympifyError:
        return "Ошибка: неверный синтаксис математического выражения"
    except Exception as e:
        return f"Ошибка при вычислении производной: {str(e)}"


if name == "__main__":
    # Вычисляем производную функции e^(x^2)
    x = symbols('x')
    function = exp(x**2)
    
    print("Исходная функция: e^(x^2)")
    print("Вычисление производной...")
    
    # Вычисляем производную
    result = diff(function, x)
    print(f"Производная функции e^(x^2) = {result}")
    
    # Альтернативно через нашу функцию
    result2 = derivative("exp(x**2)", "x")
    print(f"Результат через функцию derivative: {result2}")