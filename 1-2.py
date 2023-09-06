import re

def calculate(expression):
    try:
        expression = expression.replace('^', '**').replace('x', '*')

        while '(' in expression:
            expression = re.sub(r'\(([^()]+)\)', lambda x: str(eval(x.group(1))), expression)

        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {str(e)}"


expression = input("Enter a mathematical expression: ")


result = calculate(expression)
if isinstance(result, (int, float)):
    round_res = round(result, 2)
    print("Result:", round_res)
else:
    print(result)
