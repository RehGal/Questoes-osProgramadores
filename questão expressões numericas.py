def evaluate_expression(expression):
    try:
        expression = expression.replace("^", "**")
        
        result = eval(expression)
        
        if isinstance(result, float) and result == float('inf'):
            return "ERR DIVBYZERO"
        
        return result
    except ZeroDivisionError:
        return "ERR DIVBYZERO"
    except Exception:
        return "ERR SYNTAX"

expressions = [
    "1 + 0 + 25 - 3",
    "1+1*5-1",
    "1 + 4 / 2 ^2 - 1",
    "1 + 3 * 6 / 2 + 0",
    "0 / 1 + 1 / 0",
    "1 * (5 + 10) / 3",
    "((5-1) * 2)^2",
    "(2 - 1) * 2^3",
    "4 / (54 - (9 * 6))",
    "54 * * 54 - 1",
    "((79 - 12) * (5 + (2 - 1))",
    "266 + 54 * 4 - ( 41 + 2 ) * 10 / 5 - 7 ^ 3 - 1 + 1 * 0 - (( 45 / 5 * 3 - 1) * 2)"
]

for expr in expressions:
    print(evaluate_expression(expr))