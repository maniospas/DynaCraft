#from mainObject import Object
from lark import Visitor
from lark import Tree
from Objects.mainObject import my_Object
from myLogger import print_debug
from myLogger import print_return
from myLogger import print_info
class Context(Visitor):
    def __init__(self, parent=None):
        self.parent = None
        self.types = {}  # {"x": "float"}
        self.values = {}
        self.variables = {}
        #self.varValues = {}
        self.found_item = None
        #if parent is None:
            #self.types["empty"] = "object"
            #self.values["empty"] = object()

            #self.types["__add__"] = "method"

            #def add(x, y):
                #xvalue = x.fields["value"]
                #yvalue = y.fields["value"]
                #return x + y

            #self.values["__add__"] = my_Object({"call": add}, types=["object", "method"])

    def set(self, name, value):
        if name not in self.types:
            if self.parent is None:
                raise Exception("no such variable: " + name)
            return self.parent.set(name, value)
        for i in range(len(self.types[name])):
            if self.types[name][i] != value.types[name][i]:
                raise Exception("invalid datatypes")
        self.values[name] = value

    def start(self, node):
        print("The start items are :", node)
        print("Visiting start node:", node.data)
        for child in node.children:
            self.visit(child)
        # if isinstance(items, Tree):
        #     return self.transform(items.children)
        # else:
        #     return items


    def statement(self, items):
        print("These are the statement items!!!!", items)
        print("Finally context values", self.values)
        return items

    def semicolonstatements(self, items):
        print("These are the semicolonstatements items", items)
        return items

    def basicstatement(self, items):
        print("These are the basicstatement items", items)
        return items

    def assignment(self, items):
        print("Assignment Items", items)
        var_type = items[0]  # Extract the variable type
        var_name = items[1]  # Extract the variable name
        var_value = items[2]  # Extract the variable value
        print_debug("Variable type:", var_type)
        print_debug("Variable name:", var_name)
        print_debug("Variable value:", var_value)

        #if type(var_value) == tuple and var_value[0] == 'methodcall' :
            #self.methodcall(items[2])
        if isinstance(var_value, str):
            try:
                saved_value = self.values[var_value].fields["value"]
                print("The saved value is :", saved_value )
            except ValueError:
                saved_value = None
        var_value = saved_value if isinstance(var_value, str) and saved_value is not None else (1 if isinstance(var_value, str) and saved_value is None else var_value)

        if not isinstance(items[2], float) and len(items[2]) == 3:
            var_value = items[2][1]
            print("Now the value is", var_value)


        if "int" in str(var_type):
            try:
                var_value = float(var_value)
                print_debug("The variable is int:", var_value)
                self.types[var_name] = ["object","int"]
                self.values[var_name] = my_Object({"body": items, "value": var_value}, types=["object", "int"])

                for item_key, item_value in self.types.items():
                    if item_key == var_name:
                        self.found_item = item_value
                        break

                print_return("Value form memory:", self.values[var_name].fields["value"])  # etsi prepei na einai
                return ('assignment', self.values[var_name].types, self.values[var_name].fields)
            except ValueError:
                raise ValueError(f"Variable '{var_name}' value should be a float.")
        elif "float" in str(var_type):
            try:
                self.types[var_name] = ["object","float"]
                self.values[var_name] = my_Object({"body": items,"value": float(var_value)}, types=["object", "float"])
                print_info("The variable is float:", var_value, self.values[var_name])

                for item in self.types.items():
                    if item[0] == var_name:  # Check if the first element of the tuple matches the key
                        self.found_item = item  # Assign the entire tuple to found_item
                        break
                #print_return("Value form memory:", self.values[var_name].fields["value"])# etsi prepei na einai
                return ('assignment', self.values[var_name].types, self.values[var_name].fields)
            except ValueError:
                raise ValueError(f"Variable '{var_name}' value should be a float.")

        else:
            raise ValueError(f"Unknown variable type '{var_type}'.")

        self.variables[var_name] = var_value  # Store the variable assignment
        return ('assignment', var_type, var_name, var_value)

    def reassignment(self, items):
        print("The reassignment items are:", items)
        print("The types items are:", self.types)
        assignable = items[0]
        assignable_value = items[1]
        for item in self.types.items():
            print_debug("The preitem now is :", item)
            if item[0] == assignable :
                print("The ITEM now is :", item)
                self.values[assignable] = my_Object({"value": float(assignable_value)}, types=["object", "float"])
                #self.varValues[assignable] = assignable_value
                return('reassignment', self.values[assignable].types, self.values[assignable].fields)
        raise ValueError("Variable {} has not been assigned before.".format(assignable))


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

    def var_decl(self, items):
        print_debug("The declaration items are:", items)
        print_debug("Var type", items[0].data)
        var_name = items[1]
        var_type = items[0].data
        self.types[var_name] = ["object", var_type]

        for item in self.types.items():
            if item[0] == var_name:  # Check if the first element of the tuple matches the key
                self.found_item = item  # Assign the entire tuple to found_item
                break
        self.variables[var_name] = 0  # Store the variable assignment
        print_info("The declared variable is :", self.found_item)
        return ('var_decl', self.found_item)

    def expression(self, items):
        print("???????The expression is", items)
        return items[0]

    def simpleexpression(self, items):
        print("???????The simple expression is", items)
        return items[0]

    def assignable(self, items):
        return items[0]

    def add(self, tokens):
        print("!?!?!?The tokens are", tokens)
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])
        print("!?!?!?The tokens are", tokens)
        print("op1", operand1)
        #operand1_value = operand1.fields["value"]
        operand1_value = operand1.value
        print("op2", operand2)
        operand2_value = operand2.fields["value"]
        print("op2", operand2_value)
        add_result = operand1_value + operand2_value
        self.values[add_result] = my_Object({"value": float(add_result)}, types=["object", "float"])
        return ('add', add_result, tokens)
        #if isinstance(operand1, float) or isinstance(operand2, float):
            #return float(operand1) + float(operand2)
        #else:
           #return operand1 + operand2 #also return object with sum and value

    def calculate_expression(self, expr): #to return only object
        print_debug("The expression is", expr)
        if isinstance(expr, Tree):
            print_debug("!!!!!!Never in here Yet!!!!!!!!!!!!!!!!!!!")
            if expr.data == 'simpleexpression':
                return self.calculate_expressiond(expr.children[0])
            elif expr.data == 'add' or 'sub' or 'mul' or 'div':
                operand1 = self.calculate_expression(tokens[0])
                operand2 = self.calculate_expression(tokens[1])
                if operand1 is None or operand2 is None:
                    return None
            result = operand1 + operand2
            print_debug("The result is ", result)
            return operand1 + operand2
        #Handle other operators similarly
        elif isinstance(expr, float):
            self.values[expr] = my_Object({"value": float(expr)}, types=["object", "float"])
            print_return("The return is:", self.values[expr])
            return self.values[expr]
        elif isinstance(expr, str):
            print("Expression is str")
            print("self values", self.values)
            if expr in self.values:
                print_debug("In here the variable is", expr)
                print_return("The return for variable is:", self.values[expr])
                return self.values[expr]
            else:
                return None
        elif len(expr) == 3:
            print("HAAAAAAAAA", expr[2])
            if expr[0] == 'add':
                self.values[str(expr[2])] = my_Object({"value": float(expr[1])}, types=["object", "float"])
                return self.values[str(expr[2])]

        return None

    def methodcall(self, items):
        print_debug("In method call", items)
        data = items
        params = items[1:]
        print(data)
        print("Method Call", self.values[items[0]])
        method = self.values[items[0]]
        method_body = method.fields
        print("Method is", method)

        print("Method body is", method_body)

        body_items = []

        # Iterate through the list of lists and extract assignments and returns
        for sublist in method_body['body']:
            for item in sublist:
                #if item[0] == 'assignment' or item[0] == 'returns':
                body_items.append(item)



        newContext = Context(self)

        param_index = 0;
        for param in method.fields['params'][0]:
            if "int" in str(param[0]):
                newContext.types[param[1]] = ["object", "int"]
                newContext.values[param[1]] = my_Object({"value": params[param_index]}, types=["object", "int"])
            elif "float" in str(param[0]):
                newContext.types[param[1]] = ["object", "float"]
                newContext.values[param[1]] = my_Object({"value": params[param_index]}, types=["object", "float"])
            param_index += 1
            print("The param is", param)

        print("Items are", body_items)
        for item in body_items:
            print("Item is", item)
            if item[0] == "assignment":
                print("body is", item[2]['body'])
                command = item[2]['body']
                print("command is", command[-1])
                if isinstance(command[-1], tuple):
                    print("_________________________________its add", command)
                    print("context val is", newContext.values)
                    temp = (command[0], command[1], newContext.process_item(command[-1]))
                    print("add body is", temp)
                    exprBody = temp[2]
                    newContext.assignment(temp)
                    print("finish extra assignment")
                    continue


            if item[0] == "returns":
                print("new cont itm", newContext.values["selfz"].fields['value'])
                print("new cont itm", newContext.values["selfx"].fields['value'])
                print("new cont itm", newContext.values["selfy"].fields['value'])
                print("Return itm", item)
                newContext.returns(self.values["return_Value"].fields['body'])
                print("reet is", newContext.values["return_Value"])
                ret_body = newContext.values["return_Value"].fields["body"]
                print("reet body is", ret_body)
                print("reet type is", newContext.values["return_Value"].types)
                temp = (newContext.values["return_Value"].types, "return_Value", newContext.process_item(ret_body))
                print("temp  is", newContext.values["return_Value"].types)
                newContext.values["return_Value"] = my_Object({"value": temp[2][0][1]}, types=newContext.values["return_Value"].types)
                print("new return value", newContext.values["return_Value"])
                break
                #if(self.values["return_Value"].fields[])
                #print("reet is", self.values["return_Value"].fields['body'])
                #newContext.returns(self.values["return_Value"].fields['body'])

            newContext.assignment(item[2]['body'])

        #print("All new Context Values:",newContext.values)
        #print("Return Value:", newContext.values["return_Value"].fields["value"])
        return (newContext.values["return_Value"].fields["value"])

    def process_item(self, item):
        print("NOW THE ITEM IS :", item)
        if isinstance(item, tuple) :
            print("NOW THE ITEM IS basic:", item)
            print("NOW THE ITEM IS :", item)
            token1 = item[2][0]
            token2 = item[2][1]
            print("NOW THE token IS :", token1)
            print("NOW THE token IS :", token2)
            print("NOW values  IS :", self.values)
            if isinstance(token2, int):
                print("the second token =is", token2)
            if isinstance(token2, float):
                print("the second token =is", token2)
            if (isinstance(token1,str) and isinstance(token2, str)) or (isinstance(token1,str) and isinstance(token2, int)) or (isinstance(token1,str) and isinstance(token2, float)):

                result = self.add([token1,token2])
                print("NOW THE res IS :", result)
            return result
            op, value, tokens = item
            if item[0] == 'add':
                result = self.add(item[2])
                return (result)
        elif isinstance(item, list):
            print("NOW THE ITEM IS NOT basic:", item)
            return [self.process_item(sub_item) for sub_item in item]
        return item

    def evaluate_item(self, item):
        print("the evalut item :", item)
        return

    def method_decl(self, items):
        print("-------------------------Declare function", items)
        print("Fun name:", items[0])
        print("whar", items[1])
        print("body", items[2])

        self.types[items[0]] = ["object", items[0]]
        self.values[items[0]] = my_Object({"params": items[1],"body": items[2]}, types=["object", "function", items[0]]) #{"params": items[1], "return_type"=["float"],"body": items[2]}, types=["object", "function"]
        return('method_decl', self.types, self.values)

    def codeblock(self, items):
        print("-------------------------Declare codeblock", items)
        return items  #maybe this should return an object as well

    def returns(self, items):
        print("Into return", items)
        if isinstance(items[0][1], float):
            print("item is float", items)
            self.types["return_Value"] = ["object", "float"]
            self.values["return_Value"] = my_Object({"body": items, "value": float(items[0][1])}, types=["object", "float"])
            return ('returns', self.values["return_Value"])
        self.types["null"] = ["object"]
        return('returns', self.values["null"])

    def methodparams(self, items):
        print("Method params are", items)

        for item in items[0]:
            if "int" in str(item[0]):
                self.types[item[1]] = ["object", "int"]
                self.values[item[1]] = my_Object({"value": int(1)}, types=["object", "int"])
            elif "float" in str(item[0]):
                self.types[item[1]] = ["object", "float"]
                self.values[item[1]] = my_Object({"value": float(1)}, types=["object", "float"])
            print("Method params is", item[1])
        return items

    def paramdecl(self, items):
        print("paramdecl are", items)
        return items

    def sub(self, tokens):

        print_debug("In sub the tokens are", tokens)
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])

        print_debug("Thew operand are", operand1)
        print_debug("Thew operand are", operand2)

        operand1_value = operand1.fields["value"]
        print_debug("The 1t value is", operand1_value)
        operand2_value = operand2.fields["value"]
        print_debug("The 2nd value is", operand1_value)

        sub_result = operand1_value - operand2_value
        self.values[sub_result] = my_Object({"value": float(sub_result)}, types=["object", "float"])
        print_debug("The sub return is", self.values[sub_result])
        return sub_result

    def mul(self, tokens):
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])

        operand1_value = operand1.fields["value"] #operand1.value
        operand2_value = operand2.fields["value"]

        mul_result = operand1_value * operand2_value
        self.values[mul_result] = my_Object({"value": float(mul_result)}, types=["object", "float"])
        return mul_result

    def div(self, tokens):
        if tokens[1] == 0:
            raise ValueError("Division by zero")
        operand1 = self.calculate_expression(tokens[0])
        operand2 = self.calculate_expression(tokens[1])

        operand1_value = operand1.fields["value"]
        operand2_value = operand2.fields["value"]

        div_result = operand1_value / operand2_value
        self.values[div_result] = my_Object({"value": float(div_result)}, types=["object", "float"])
        return div_result

    def NAME(self, token):
        print("The Names are", token)
        return token.value

    def NUMBER(self, token):
        return float(token)

    def visit(self, node):
        if hasattr(node, 'data'):
            method_name = 'visit_' + node.data
        else:
            method_name = 'visit_' + "token"
        #print("Visiting  node:", node)
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        if hasattr(node, 'data'):
            print("Visiting generic node:", node.data)
        else:
            print("Visiting token", node)
        if hasattr(node, 'children'):
            for child in node.children:
                self.visit(child)