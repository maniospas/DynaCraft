from lark import Interpreter
from lark import Tree
from Objects.mainObject import my_Object
from myLogger import print_debug
from myLogger import print_info

class TopDownContext(Interpreter):
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

    def statement(self, node):
        print("These are the statement items!!!!", node)
        for child in node.children:
            result = self.visit(child)
        print("Return from child:", result)
        print("Finally context values", self.values)
        #print("Finally context values", self.values["s"])
        return node

    def semicolonstatements(self, node):
        print("These are the semicolonstatements items", node)
        for child in node.children:
            result = self.visit(child)
        print("Return from child:", result)
        return result

    def basicstatement(self, node):
        print("These are the basicstatement items", node)
        for child in node.children:
            result = (self.visit(child))
        print("Return from child:", result)
        return result

    def assignment(self, node):
        result = []
        print("These are the assignment items", node)
        result.append(node.children[0]) # append 1st child which is assignment type
        # if result[0].data == "derived":
        #     print("!-!_!_!_!_!_It is an object init", result[0])
        #     der_result = self.visit(result[0])
        #     print("!-!_!_!_!_!_It is init", der_result)
        # else :
        #     print("!-!_!_!_!_!_It is NOT an object init", result[0])
        for child in node.children[1:]:
            print("The assignment child is", child)
            result.append(self.visit(child))

        print("Return from child:", result)
        var_type = result[0].data
        var_name = result[1]
        var_value = result[2]
        print(f"type: {var_type}, name: {var_name}, value: {var_value}")
        self.values[var_name] = my_Object({"value": float(var_value)}, types=["object", "float"])
        print_info(f"The saved item: {self.values[var_name]}")
        return node

    def reassignment(self, node):
        result = []
        print("These are the reassignment items", node)
        #result.append(node.children[0])  # append 1st child which is assignment type
        for child in node.children:
            print("The assignment child is", child)
            result.append(self.visit(child))
        var_name = result[0]
        var_value = result[1]
        print(f"result: {var_name}, {var_value}, {result}")
        if var_name in self.values:
              self.values[var_name].value = var_value
              print_info(f"The reassigned item: {self.values[var_name]}")
        else :
            raise ValueError("Variable {} has not been assigned before.".format(var_name))


    def evaluate_expression(self, operands):
        print("These are the evaluate_expression items", operands)
        return operands

    def var_decl(self, node):
        print("These are the var_decl items", node)
        result = []
        var_type = node.children[0] # append 1st child which is decl type
        var_name = node.children[1]  # append 2st child which is decl name
        self.values[var_name] = my_Object({}, types=["object", {var_type}])
        print_info(f"The declared saved item: {self.values[var_name]}")
        return node

    def expression(self, node):
        print("???????The expression is", node)
        for child in node.children:
            print("The expression child is", child)
            result = self.visit(child)
        return result

    def simpleexpression(self, node):
        print("???????The simple expression is", node)
        for child in node.children:
            print("The simpleexpression child is", child)
            if isinstance(child, Tree):
                if child.data == "methodcall":
                    result = self.visit(child)
                else:
                    for sub_child in child.children:
                        var_name = sub_child
                        var_type = self.values[var_name].types
                        print("The sub_child is", self.values[var_name].types)
                        if "function" in var_type:
                            return var_name                                         #if simple expression is of type function return its name instead of value
                        var_value = self.values[var_name].value
                        result = var_value
            else:
                print("x is not a Tree")
                if child.isdigit():
                    print("x is an integer")
                    result = int(child)
                elif child.count('.') == 1 and child.replace('.', '', 1).isdigit():
                    print("x is a float")
                    result = float(child)
                else :
                    print("The  child is NOT num", child)
                    result = self.visit(child)
        return result

    def assignable(self, node):
        print("The assignable are", node)
        for child in node.children:
            print("The assignable child is", child)
            result = child
        return result

    def add(self, node):
        print("add are", node)
        result = []
        for child in node.children:
            print("The add child is", child)
            result.append(self.visit(child))
        print("The add result is", result)
        add_result = result[0] + result[1]
        return add_result

    def calculate_expression(self, expr): #to return only object
        print_debug("The expression is", expr)
        return expr

    def methodcall(self, node):
        print("The methodcall is", node)

        if len(node.children) > 1:
            param_list = node.children[1:]
        else:
            param_list = []

        #for child in node.children[0]:    #only the first item is tree, the others are the params
        result = self.visit(node.children[0])

        print("The methodcall child is", result)
        method_name = result
        print("The method is", self.values[method_name])

        newContext = TopDownContext(self)
        index = 0
        if self.values[method_name].fields["params"] :
            for param in self.values[method_name].params: #SOS TO ADD TYPE CHECK
                param_type = param[0]
                param_name = param[1]
                newContext.values[param_name] = my_Object({"value": float(param_list[index])}, types=["object", param_type])
                index += 1
                print("The param is", param)
        result = newContext.visit(self.values[method_name].body)
        print("the method call return is:", result)
        return result

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

    def method_decl(self, node):
        print("-------------------------Declare function", node)
        print("Fun name:", node.children[0])
        print("whar", node.children[1])
        print("body", node.children[2])
        method_name = node.children[0]
        method_params = self.visit(node.children[1])   #visit declare params
        method_body = node.children[2]
        self.types[method_name] = ["object", method_name]
        #HOW CAN I GET RETURN VAL WITHOUT TRAVERSING THE TREE??????????!!!!!SOS
        self.values[method_name] = my_Object({"params": method_params,"body": method_body}, types=["object", "function", method_name]) #{"params": items[1], "return_type"=["float"],"body": items[2]}, types=["object", "function"]
        print_info(f"The saved method: {self.values[method_name]}")

    def codeblock(self, node):
        print("codeblock is", node)
        #newContext = TopDownContext(self)

        for child in node.children:
            print("The codeblock child is", child)
            result = self.visit(child)
        return result

    def returns(self, node):
        print("Into return", node)
        for child in node.children:
            print("The codeblock child is", child)
            result = (self.visit(child))
        print("return result", result)
        return result

    def extract_info(self, tree):
        for child in tree.children:
            if isinstance(child, Tree):
                data_type = None
                name = None
                for sub_child in child.children:
                    if isinstance(sub_child, Tree) and not data_type:
                        data_type = sub_child.data
                    else:
                        name = sub_child.value
                yield data_type, name

    def methodparams(self, node):
        param_result = []
        print("Method params are", node.children)
        if node.children:
            print("Method params are", node.children[0].children[0])
            for var_type, var_name in self.extract_info(node.children[0]):
                param_result.append([var_type, var_name])
                print("Data Type:", var_type)
                print("Name:", var_name)

        return param_result

    def paramdecl(self, items):
        print("________________________paramdecl are", items)
        return items

    def sub(self, node):
        print("sub are", node)
        result = []
        for child in node.children:
            print("The sub child is", child)
            result.append(self.visit(child))
        print("The sub result is", result)
        sub_result = result[0] - result[1]
        return sub_result

    def mul(self, node):
        print("mul are", node)
        result = []
        for child in node.children:
            print("The mul child is", child)
            result.append(self.visit(child))
        print("The mul result is", result)
        mul_result = result[0] * result[1]
        return mul_result

    def div(self, node):
        print("div are", node)
        result = []
        for child in node.children:
            print("The div child is", child)
            result.append(self.visit(child))
        print("The div result is", result)
        if result[1] == 0:
            raise ValueError("Division by zero")
        div_result = result[0] / result[1]
        return div_result

    def derived(self, node):
        print("???????????????????The derived tokens are", node.children[0])
        derived_name = node.children[0]
        print("The derived result is", self.values)
        result_derived = self.values[derived_name]
        print("The derived result is", result_derived)
        #return

    def NAME(self, token):
        print("The Names are", token)
        return token.value

    def NUMBER(self, token):
        return float(token)

    # def visit(self, node):
    #     if hasattr(node, 'data'):
    #         method_name = 'visit_' + node.data
    #     else:
    #         method_name = 'visit_' + "token"
    #     #print("Visiting  node:", node)
    #     method = getattr(self, method_name, self.generic_visit)
    #     return method(node)
    #
    # def generic_visit(self, node):
    #     if hasattr(node, 'data'):
    #         print("Visiting generic node:", node.data)
    #     else:
    #         print("Visiting token", node)
    #     if hasattr(node, 'children'):
    #         for child in node.children:
    #             self.visit(child)