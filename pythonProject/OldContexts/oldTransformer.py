from lark import Transformer, v_args
from lark import Tree
# Define the custom transformer
class MyTransformer(Transformer):
    def __init__(self):
        self.variables = {}

    def start(self, items):
        if isinstance(items, Tree):
            return self.transform(items.children)
        else:
            return items

    def statement(self, items):
        print("These are the statement items", items)
        return items[0]

    def semicolonstatements(self, items):
        print("These are the semicolonstatements items", items)
        return items

    def basicstatement(self, items):
        print("These are the basicstatement items", items)
        return items[0]

    def assignment(self, items):
        print("These are the assignment items", items)
        var_type = items[0]  # Extract the variable type
        var_name = items[1]  # Extract the variable name
        var_value = items[2]  # Extract the variable value
        print("Variable type:", var_type)
        print("Variable name:", var_name)
        print("Variable value:", var_value)

        if "int" in str(var_type):
            try:
                print("The variable is int:", var_value)
                var_value = float(var_value)
            except ValueError:
                raise ValueError(f"Variable '{var_name}' value should be a float.")
        elif "float" in str(var_type):
            try:
                print("The variable is int:", var_value)
                var_value = float(var_value)
            except ValueError:
                raise ValueError(f"Variable '{var_name}' value should be a float.")

        else:
            raise ValueError(f"Unknown variable type '{var_type}'.")

        self.variables[var_name] = var_value  # Store the variable assignment
        return ('assignment', var_type, var_name, var_value)

    def reassignment(self, items):
        assignable = items[0]
        if assignable not in self.variables:
            raise ValueError("Variable {} has not been assigned before.".format(assignable))
        value = self.variables[assignable]

        expression = items[1]
        print(f"the expression is '{expression}'.")
        print(f"the items are '{items}'.")

        # Only update the variable value if the expression is not an operation
        value = self.evaluate_expression(expression)

        self.variables[assignable] = value
        return ('reassignment', assignable, value)

    def evaluate_expression(self, operands):
        if isinstance(operands, float):  # Check if operands is a single float value
            return operands
        elif isinstance(operands[0], str) and operands[0] in self.variables:
            left_operand = self.variables[operands[0]]
        else:
            left_operand = operands[0]

        if isinstance(operands[1], str) and operands[1] in self.variables:
            right_operand = self.variables[operands[1]]
        else:
            right_operand = operands[1]

        return left_operand + right_operand

    def methoddecl(self, items):
        return ('methoddecl', items[1], items[2], items[3])

    def methodparams(self, items):
        return items[1:-1]

    def var_decl(self, items):
        print(f"VarDecl!!!!!!! items are '{items}'.")
        print("Var type", items[0].data)
        return ('vardecl', items[0], items[1])

    def paramdecl(self, items):
        return items

    def vartype(self, items):
        return items[0]

    def codeblock(self, items):
        return items[1:-1]

    def return_(self, items):
        return ('return', items[1:])

    def method(self, items):
        return items[0]

    def methodcall(self, items):
        return ('methodcall', items[0], items[1:-1])

    def blockexec(self, items):
        return ('blockexec', items[0])

    def expression(self, items):
        return items[0]

    def simpleexpression(self, items):
        return items[0]

    def assignable(self, items):
        return items[0]

    def add(self, tokens):
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])
        if isinstance(operand1, float) or isinstance(operand2, float):
            return float(operand1) + float(operand2)
        else:
            return operand1 + operand2

    def calculate_expression(self, expr):
        if isinstance(expr, Tree):
            if expr.data == 'simpleexpression':
                return self.calculate_expressiond(expr.children[0])
            elif expr.data == 'add' or 'sub' or 'mul' or 'div':
                operand1 = self.calculate_expression(tokens[0])
                operand2 = self.calculate_expression(tokens[1])
                if operand1 is None or operand2 is None:
                    return None
            return operand1 + operand2
        # Handle other operators similarly
        elif isinstance(expr, float):
            return expr
        elif isinstance(expr, str):
            if expr in self.variables:
                return self.variables[expr]
            else:
                return None
        return None

    def sub(self, tokens):
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])
        return operand1 - operand2

    def mul(self, tokens):
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])
        return operand1 * operand2

    def div(self, tokens):
        if tokens[1] == 0:
            raise ValueError("Division by zero")
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])
        return operand1 / operand2

    def NAME(self, token):
        return token.value

    def NUMBER(self, token):
        return float(token)