from lark import Lark, Tree, Token
from lark.visitors import Interpreter
from myLogger import print_info
from dynacraft.support.builtins import Functions
from dynacraft.support.arithmetic import ContextFunctions
from dynacraft.support.core import ContextCore
from dynacraft.objects.object import Object
from dynacraft import helpers


class Context(Interpreter, ContextCore, ContextFunctions):
    def __init__(self, parent=None):
        self.parent = parent
        self.types = {}
        self.values = {}
        self.variables = {}
        self.temp_funs = []
        self.found_item = None
        self.default_flag = False  # Initialize the default_flag attribute

    def visit(self, tree: Tree):
        # Check for the default_flag and perform specific logic if needed
        if self.default_flag:
            self.default_flag = False
            if isinstance(tree, Tree):
                obj_name = tree.children[0].children[0].children[0] #get object name since ree.children[0] is Tree('assignable', [Tree('simpleexpression', [Tree('assignable', [Token('NAME', 't')])]), Token('NAME', 'new')])
                obj_field = tree.children[1] #get field name
                obj_new = self.values[obj_name]
                res_obj = obj_new.get_public_field(obj_field)
                return res_obj
            else:
                raise TypeError(f"Expected a Tree, got {type(tree).__name__}")

        # Call the appropriate method based on the tree's data
        if isinstance(tree, Tree):
            method = getattr(self, tree.data, None)
            if method is not None:
                return method(tree)
            else:
                return self._visit_tree(tree)
        else:
            return self._visit_tree(tree)

    def set(self, name, value):
        if name not in self.types:
            if self.parent is None:
                raise Exception("no such variable: " + name)
            return self.parent.set(name, value)
        for i in range(len(self.types[name])):
            if self.types[name][i] != value.types[name][i]:
                raise Exception("invalid datatypes")
        self.values[name] = value

    def assignment(self, node):
        result = []
        result.append(node.children[0])
        if result[0].data == "derived":
            temp = node.children[1]
            var_name = temp.children[0].value
            der_result = self.visit(result[0])
            for child in node.children[1:]:
                result.append(self.visit(child))
            res = helpers.is_list_or_object(result[2], 1)
            self.values[var_name] = res
            print_info(f"The saved item: {self.values[var_name]}")
            return self.values[var_name]
        else:
            for child in node.children[1:]:
                result.append(self.visit(child))
            res = helpers.is_list_or_object(result[2], 0)
            if 'value' in result[1].fields:
                var_name = result[1].get_public_field("value")
                var_type = result[0].data
                if var_type in result[2].types:
                    self.values[var_name] = result[2]
                    print_info(f"The saved item: {self.values[var_name]}")
                    return self.values[var_name]
                else:
                    raise ValueError("Invalid type")
            else:
                var_type = result[0].data
                if var_type in result[2].types:
                    index = result[2].types.index(var_type)
                    new_types_list = result[2].types[:index + 1]
                    result[1].fields['value'] = result[2].fields['value']
                    for key, value in result[2].public_fields.items():
                        result[1].set_public_field(key, value)
                    for key, value in result[2].private_fields.items():
                        result[1].set_private_field(key, value)
                    result[1].types = new_types_list
                    return result[1]
                else:
                    raise ValueError("Invalid type")

    def reassignment(self, node):
        result = []
        for child in node.children:
            if isinstance(child, Tree) and len(child.children) > 1 and child.data == 'assignable':
                self.default_flag = True
            else:
                self.default_flag = False
            result.append(self.visit(child))
        self.default_flag = False

        var_name = result[0].get_public_field('value')
        var_value = result[1].get_public_field('value')
        if var_name in self.values:
            already_assigned = set(self.values[var_name].types)
            to_assign = set(result[1].types)
            if already_assigned.issubset(to_assign):
                self.values[var_name].set_public_field('value', var_value)
                return self.values[var_name]
            else:
                raise ValueError("Invalid type for reassignment")
        elif isinstance(result[0], Object):
            result[0].set_public_field('value', result[1].get_public_field('value'))
        else:
            raise ValueError(f"Variable {var_name} has not been assigned before.")

    def evaluate_expression(self, operands):
        return operands

    # def var_decl(self, node):
    #     result = []
    #     var_type = node.children[0].data # append 1st child which is decl type
    #     var_name = node.children[1] # append 2st child which is decl name
    #     if var_type != "object":
    #         self.values[var_name] = my_Object({}, types=["object", var_type])
    #     else:
    #         self.values[var_name] = my_Object({}, types=["object"])
    #     return self.values[var_name]

    def var_decl(self, node):
        var_type = node.children[0].data  # First child is the declaration type
        var_name = node.children[1].value  # Second child is the declaration name

        if var_type != "object":
            new_var = Object(types=["object", var_type])
        else:
            new_var = Object(types=["object"])

        self.values[var_name] = new_var
        return new_var

    def expression(self, node):
        for child in node.children:
            result = self.visit(child)
        return result

    def simpleexpression(self, node):
        var_assign = ''
        var_object = ''
        for child in node.children:
            if isinstance(child, Tree):
                if child.data == "methodcall":
                    result = self.visit(child)
                else:
                    for sub_child in child.children:
                        if isinstance(sub_child, Tree):
                            if sub_child.children[0].data == "methodcall":
                                result = self.visit(sub_child.children[0])
                                var_object = result
                            else:
                                var_assign = (sub_child.children[0].children[0].value)
                                continue
                        elif var_object != '':
                            sub_obj = var_object.get_public_field(sub_child.value)
                            return sub_obj
                        elif var_assign != '':
                            value_list = self.values[var_assign].fields
                            obj = self.values[var_assign]
                            sub_obj = obj.get_initial_field(sub_child.value)
                            return sub_obj
                        elif hasattr(Functions, sub_child):
                            self.temp_funs = sub_child
                            result = Object()
                            return result
                        else:
                            var_name = sub_child.value
                            result = self.values[var_name]
                            if isinstance(self.values[var_name], list):
                                if "function" in self.values[var_name]:
                                    print("fun", self.values[var_name])
                                    return var_name
                            return result
            else:
                if child.isdigit():
                    result_value = int(child)
                    result = Object({"value": result_value}, types=["object", "int"])
                elif child.count('.') == 1 and child.replace('.', '', 1).isdigit():
                    result_value = float(child)
                    result = Object({"value": result_value}, types=["object", "float"])
                else:
                    result = self.visit(child)
            return result

    def assignable(self, node):
        if len(node.children) > 1 :
            result = self.visit(node.children[0])
            var_name = helpers.search_by_value(self.values, result)
            sub_object = Object(types=["object"])
            existing_obj = self.values[var_name]
            existing_obj.set_public_field(var_name, sub_object)
            existing_obj.set_public_field(f"{node.children[1].value}", sub_object)
            existing_obj.set_initial_field(var_name, sub_object)
            existing_obj.set_initial_field(f"{node.children[1].value}", sub_object)
            return sub_object
        else:
            for child in node.children:
                result_value = child.value
                result = Object({"value": result_value}, types=["object", "assignable"])
            return result

    def methodcall(self, node):
        if len(node.children) > 1:
            param_list = node.children[1:]
        else:
            param_list = []

        result = self.visit(node.children[0])
        if isinstance(result, Object) and result.is_empty():
            if len(node.children) > 1:
                obj = self.values[node.children[1].value]
                function_obj = Functions()
                method_name = self.temp_funs.value
                if method_name:
                    method_to_call = getattr(function_obj, method_name, None)
                    if method_to_call:
                        method_to_call(obj)
                    else:
                        print(f"Method '{method_name}' does not exist in Function")
                return Object()
            else:
                function_obj = Functions()
                method_name = self.temp_funs.value
                if method_name:
                    method_to_call = getattr(function_obj, method_name, None)
                    if method_to_call:
                        return method_to_call()
                    else:
                        print(f"Method '{method_name}' does not exist in Function")
                return Object()

        method_name = result
        newContext = Context(self)
        param_list_types = []

        for param in param_list:
            if param in self.values:
                param_type = self.values[param].types[1]
            else:
                param_type = param.type
                if 'NUMBER' in param_type:
                    param_type = 'float'
            param_list_types.append(param_type)

        for item in self.values[method_name][1:]:
            flat_list = [inner[0] for inner in item.fields["params"]]
            if flat_list == param_list_types:
                method = item

        for value in self.values:
            newContext.values[value] = []
            if isinstance(self.values[value], Object):
                obj = Object()
                obj.fields = self.values[value].fields
                obj.types = self.values[value].types
                newContext.values[value].append(obj)
            elif len(self.values[value]) > 1:
                newContext.values[value].append("function")
                for sub_item in self.values[value][1:]:
                    obj = Object()
                    obj.fields = sub_item.fields
                    obj.types = sub_item.types
                    newContext.values[value].append(obj)

        if method.fields["params"]:
            for index, param in enumerate(method.params):
                if param_list[index] in self.values:
                    try:
                        param_value = self.values[param_list[index]].get_public_field('value')
                    except (IndexError, AttributeError, KeyError):
                        newContext.values[param[1]] = self.values[param_list[index]]
                        continue
                else:
                    param_value = float(param_list[index])
                param_type = param[0]
                param_name = param[1]
                newContext.values[param_name] = Object({"value": param_value}, types=["object", param_type])

        result = newContext.visit(method.body)
        obj_result = Object(types=["object", "test"])
        for key, value in list(newContext.values.items())[2:]:
            obj_result.set_public_field(key, value)
        result.types.append(method_name)
        return result

    def method_decl(self, node):
        method_name = node.children[0].value
        method_params = self.visit(node.children[1])
        method_body = node.children[2]
        self.types[method_name] = ["object", method_name]

        param_types = [sublist[0] for sublist in method_params]
        method_obj = Object(
            {"param_types": param_types, "params": method_params, "body": method_body},
            types=["object", "function", method_name]
        )

        if method_name not in self.values:
            self.values[method_name] = ["function"]

        self.values[method_name].append(method_obj)

        return self.values[method_name]

    def codeblock(self, node):
        for child in node.children:
            result = self.visit(child)
        return result

    def returns(self, node):
        for child in node.children:
            result = self.visit(child)
        return result

    def if_statement(self, node):
        result = self.visit(node.children[0])
        res = helpers.is_list_or_object(result, 0)
        if res.value == 1:
            result = self.visit(node.children[1])
        else:
            result = self.visit(node.children[2])

    def while_statement(self, node):
        while self.visit(node.children[0]).value == 1:
            self.visit(node.children[1])

    def extract_info(self, tree):
        if not isinstance(tree.children[1], Tree):
            data_type = tree.children[0].data
            name = tree.children[1].value
            yield data_type, name
        else:
            for child in tree.children:
                if isinstance(child, Tree) and len(child.children) > 0:
                    data_type = None
                    name = None
                    for sub_child in child.children:
                        if isinstance(sub_child, Tree) and data_type is None:
                            data_type = sub_child.data
                        elif isinstance(sub_child, Token):
                            name = sub_child.value
                    yield data_type, name

    def methodparams(self, node):
        param_result = []
        if node.children:
            for child in node.children:
                for var_type, var_name in self.extract_info(child):
                    if [var_type, var_name] not in param_result:
                        param_result.append([var_type, var_name])
        return param_result

    def paramdecl(self, items):
        return items

    def derived(self, node):
        derived_name = node.children[0]
        result_derived = self.values[derived_name]

    def NAME(self, token):
        return token.value

    def NUMBER(self, token):
        return float(token)