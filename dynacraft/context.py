from lark import Lark, Tree, Token
from lark.visitors import Interpreter
from myLogger import print_info
from dynacraft.support import builtins
from dynacraft.support.arithmetic import ContextFunctions
from dynacraft.support.core import ContextCore
from dynacraft.objects.object import Object
from dynacraft.helpers import helpers


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
                obj_name = tree.children[0].children[0].children[0]  # get object name since ree.children[0] is Tree('assignable', [Tree('simpleexpression', [Tree('assignable', [Token('NAME', 't')])]), Token('NAME', 'new')])
                obj_field = tree.children[1]  # get field name
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

    def start(self, node):
        return ContextCore.start(self, node)

    def statement(self, node):
        return ContextCore.statement(self, node)

    def semicolonstatements(self, node):
        return ContextCore.semicolonstatements(self, node)

    def basicstatement(self, node):
        return ContextCore.basicstatement(self, node)

    def assignment(self, node):
        result = []
        result.append(node.children[0])
        if result[0].data == "derived":
            var_type = self.visit(result[0])[-1] #get cast type
            temp = node.children[1]
            var_name = temp.children[0].value
            der_result = self.visit(result[0])
            for child in node.children[1:]:
                result.append(self.visit(child))
            res = helpers.Is_list_or_object(result[2], 1)
            self.values[var_name] = res
            if var_type == res.get_types()[-1]:
                pass #no downcast so no further changes
            elif var_type in res.get_types(): #downcast
                types = res.get_types()
                updated_types = types[:types.index(var_type) + 1]
                res.update_types(updated_types)
                added_fields_list = res.get_added_fields()

                fields_downcasted = [key for key, value in added_fields_list.items() if value != updated_types]
                for field in fields_downcasted:
                    res.make_field_private(field)
                res.original_types = types

            return self.values[var_name]
        else:
            for child in node.children[1:]:
                result.append(self.visit(child))
            res = helpers.Is_list_or_object(result[2], 0)
            if 'value' in result[1].fields:
                var_name = result[1].get_public_field("value")
                var_type = result[0].data
                if var_type in result[2].types:
                    self.values[var_name] = result[2]
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
                            sub_obj = obj.get_public_field(sub_child.value)
                            if sub_obj is None:
                                return Object() #subObject doesnt exist, for ecxample it may be private
                            return sub_obj
                        elif hasattr(builtins, sub_child):
                            # if sub_child in self.values.keys():
                            #     return sub_child
                            if sub_child in self.temp_funs:
                                return sub_child
                            self.temp_funs = sub_child
                            result = Object()
                            return sub_child
                        else:
                            var_name = sub_child.value
                            result = self.values[var_name]
                            if isinstance(self.values[var_name], list):
                                if "function" in self.values[var_name]:
                                    return var_name
                            return result
            else:
                if child.isdigit():
                    result_value = int(child)
                    result = Object({"value": result_value}, types=["object", "int"])
                elif child.count('.') == 1 and child.replace('.', '', 1).isdigit():
                    result_value = float(child)
                    result = Object({"value": result_value}, types=["object", "float"])
                elif child == "true" or child == "false":
                    result_value = child.value
                    result = Object({"value": result_value}, types=["object", "bool"])
                elif isinstance(child, str):
                    result_value = child.value.strip("'\"")
                    result = Object({"value": result_value}, types=["object", "string"])
                else:
                    result = self.visit(child)
            return result

    def assignable(self, node):
        if len(node.children) > 1:
            result = self.visit(node.children[0])
            var_name = helpers.search_by_value(self.values, result)
            sub_object = Object(types=["object"])
            existing_obj = self.values[var_name]
            if not existing_obj.get_public_field(node.children[1].value):
                existing_obj.set_added_fields(f"{node.children[1].value}", existing_obj.get_types())

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

    def methodcall_subroutine(self, node): #-->used for builtins, and builtins when only they have the correct overload, and methodcall recirsion
        if len(node.children) > 1:
            try:
                try:
                    if node.children[1].data == "listget":
                        obj = self.visit(node.children[1])  # --> return list object
                except:
                    pass # --> excpet since it may not be able to read nodes like it need for listget. Continue easue it is something else
                obj = self.values[node.children[1].value]
            except AttributeError as e:
                obj = self.visit(node.children[1])
                #return result
            except KeyError as e:
                if node.children[1].value.isdigit():
                    obj = Object({"value": node.children[1].value}, types=["object", "int"])
                elif isinstance(node.children[1].value, str):
                    try:
                        if (float(node.children[1].value)):
                            obj = Object({"value": node.children[1].value}, types=["object", "float"])
                    except:
                        if node.children[1].value == "true" or node.children[1].value == "false":
                            obj = Object({"value": node.children[1].value}, types=["object", "bool"])
                        else:
                            obj = Object({"value": node.children[1].value}, types=["object", "string"])
                else:
                    raise Exception(f"Invalid variable '{node.children[1].value}'")
            if not self.temp_funs:
                return Object()
            method_name = self.temp_funs.value
            if method_name:
                method_to_call = getattr(builtins, method_name, None)
                if method_to_call:
                    retObj = method_to_call(obj)
                else:
                    raise Exception(f"Method '{method_name}' does not exist in Function")
            if retObj is not None:
                return retObj
            else:
                return Object()
        else:
            method_name = self.temp_funs.value
            if method_name:
                method_to_call = getattr(builtins, method_name, None)
                if method_to_call:
                    return method_to_call()
                else:
                    raise Exception(f"Method '{method_name}' does not exist in Function")
            return Object()

    def methodcall(self, node):
        if len(node.children) > 1:
            param_list = node.children[1:]
        else:
            param_list = []

        result = self.visit(node.children[0])
        if isinstance(result, Object) and result.is_empty():
            return self.methodcall_subroutine(node)

        method_name = result
        newContext = Context(self)
        param_list_types = []
        for param in param_list:
            if param in self.values:
                if not self.values[param].original_types: #no downcast so ne need for original types
                    param_type = self.values[param].types
                else:
                    item = self.values[param]
                    param_type = item.original_types
                    #also upcast it
                    added_fields_list = item.get_added_fields()

                    fields_upcast = [key for key, value in added_fields_list.items() if value == param_type]
                    for field in fields_upcast:  #upcast the fields that were made private but now should be public
                        if item.get_private_field(field):
                            item.make_field_public(field)


            else:  # TODO: it is not clear what this is trying to achieve
                try:
                    param_type = param.type
                except: #no param.type when listget in function
                    return self.methodcall_subroutine(node)
                param_type = param.type
                if 'NUMBER' in param_type:
                    if param.isdigit():
                        param_type = 'int'
                    else :
                        param_type = 'float'
                elif 'BOOLEAN' in param_type:
                    param_type = 'bool'
                elif 'STRING' in param_type:
                    param_type = 'string'
                param_type = [param_type]
            param_list_types.append(param_type)

        method = None
        #try-except because without it if we try to call an inbuilt method, it doesnt find it. We need to call the subroutine
        try:
            for item in self.values[method_name][1:]:
                flat_list = [inner[0] for inner in item.fields["params"]]
                if all(any(u==v for v in param_type) for u, param_type in zip(flat_list, param_list_types)):
                #if all(u in param_type for u, param_type in zip(flat_list, param_list_types)):
                    method = item
        except:
            return self.methodcall_subroutine(node)

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

        if method is None: #--> eithet type mismatch or go into built ins
            return self.methodcall_subroutine(node)


        if method.fields["params"]:
            for index, param in enumerate(method.params):
                if param_list[index] in self.values:
                    try:
                        param_name = param[1]
                        #param_value = self.values[param_list[index]].get_public_field('value')
                        newContext.values[param_name] = self.values[param_list[index]]
                    except (IndexError, AttributeError, KeyError):
                        newContext.values[param[1]] = self.values[param_list[index]]
                        continue
                else:
                    if param_list[index].isdigit():
                        param_value = int(param_list[index])
                    else :
                        try:
                            param_value = float(param_list[index])
                        except:
                            param_value = param_list[index].strip('"') #string "" in case of string usage without variable declaration
                    # param_value = float(param_list[index])
                    param_type = param[0]
                    param_name = param[1]
                    newContext.values[param_name] = Object({"value": param_value}, types=["object", param_type])

        result = newContext.visit(method.body)
        if hasattr(result, "types"):
            result.types.append(method_name)
        else:
            result = Object(types=["object", "empty"])
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
        res = helpers.Is_list_or_object(result, 0)
        if res.value == "true":
            result = self.visit(node.children[1])
        else:
            try:
                result = self.visit(node.children[2])
            except:
                pass

    def while_statement(self, node):
        while self.visit(node.children[0]).value == 1:
            self.visit(node.children[1])

    def for_statement(self, node):

        if len(node.children[0].children) == 1: # if not sub object
            result = self.visit(node.children[0])
            listName = result.value
            list = self.values[listName]
        else:

            obj_item = self.visit(node.children[0].children[0])

            listName = node.children[0].children[1].value
            list = obj_item.get_public_field(listName)
            #list = self.values[listName]

        if 'list' in list.types:
            for key in list.public_fields:
                self.values["key"] = Object({"value": key}, types=["object", "int"])
                result = self.visit(node.children[1])
        else:
            raise ValueError("not a list")
        # listName = node.children[0].value
        # list = self.values[listName]
        # if 'list' in list.types:
        #     for key in list.public_fields:
        #         self.values["key"] = Object({"value": key}, types=["object", "int"])
        #         result = self.visit(node.children[1])
        #
        # else:
        #     raise ValueError("not a list")

    def extract_info(self, tree):
        if len(tree.children) <= 1:
            if tree.children[0].children[0].data == "derived":
                data_type = self.visit(tree.children[0].children[0])[-1]
            else:
                data_type = tree.children[0].children[0].data
            name = tree.children[0].children[1].value
            yield data_type, name
        else:
            for child in tree.children:
                if isinstance(child, Tree) and len(child.children) > 0:
                    data_type = None
                    name = None
                    for sub_child in child.children:
                        if isinstance(sub_child, Tree) and data_type is None:
                            if sub_child.data == "derived":
                                data_type = self.visit(sub_child)[-1]
                            else:
                                data_type = sub_child.data
                        elif isinstance(sub_child, Token):
                            name = sub_child.value
                    yield data_type, name

    def methodparams(self, node):
        param_result = []
        if node.children:
            for child in node.children:
                if isinstance(child, Tree) and child.children[0].data == "derived":  # param is method type. Only for derived since it works only for the methods
                    # for subchild in child.children:
                    var_type = child.children[0].children[0].value  # get method type
                    var_name = child.children[1].value  # get name
                    param_result.append([var_type, var_name])
                else:  # param is float etc
                    for var_type, var_name in self.extract_info(child):
                        if [var_type, var_name] not in param_result:
                            param_result.append([var_type, var_name])
        return param_result

    def listdecl(self,items):

        if len(items.children[2].children) >= 2:
            object_name = items.children[2].children[0].children[0].children[0].value
            if object_name not in self.values:
                raise Exception("Object not found")
            map_Name = items.children[2].children[1].value
        else:
            map_Name = items.children[2].children[0].value

        if items.children[1].data == "vartype":
            if items.children[0].data != items.children[3].data:
                raise Exception(
                    f"Key type mismatch expecting {items.children[0].data} but got {items.children[3].data}")
            if items.children[1] != items.children[4]:
                raise Exception(f"Type mismatch expecting {items.children[1]} but got {items.children[4]}")

            result = Object(types=["object", "list"], keyType=[items.children[0].data],
                            objType=[items.children[1].children], original_types=[])

        else:
            keyType_init = items.children[0].data
            if items.children[1].data == "derived":
                objType_init = items.children[1].children[0].value
            else:
                objType_init = items.children[1].data
            keyType = items.children[3].data

            if items.children[4].data == "derived":
                objType = items.children[4].children[0].value
            else:
                objType = items.children[4].data

            if keyType_init != keyType and objType_init != objType:
                raise ValueError("keyType_init does not match keyType and objType_init does not match objType")

            result = Object(types=["object", "list"], keyType=[keyType_init], objType=[objType_init], original_types=[])

        if len(items.children[2].children) >= 2:
            self.values[map_Name] = result
            self.values[object_name].set_public_field(map_Name, result)
            return result
        else:
            self.values[map_Name] = result
            return result


    def listadd(self,items):
        if len(items.children[0].children) >= 2 :  # --> we have obj
            object_name = items.children[0].children[0].children[0].children[0].value
            listName = items.children[0].children[1].value
            list = self.values[object_name].get_public_field(listName)

        else:   # --> we dont have obj
            listName = items.children[0].children[0].value
            list = self.values[listName]
        result = []
        for child in items.children[1:]:
            result.append(self.visit(child))
        try:
            item = self.values[listName]
        except:
            item = list

        if (result[0].get_types()[-1] != item.get_keyType()):  # ---> check if key is same type as defines
            raise Exception(
                f"key type mismatch. Key is of type {result[0].get_types()[-1]} but {list.get_keyType()} is expected ")

        # if self.values[listName].get_public_field("innerList"):
        if "simpleexpression" not in items.children[-1].data:  # --> this means we initiate inner list
            sub_key_type = items.children[-2].data
            sub_obj_type = items.children[-1].data
            if items.children[-1].data == "vartype":  # --> save object type based on existing sub sub list
                sub_obj_type = items.children[-1].children
            else:
                sub_obj_type = items.children[-1].data


            if list.public_fields:  # --> iterate if a layer has already be  defined
                for i in range(0,
                               len(items.children) - 4):  # --> iterate through the keys. List -1 is objtype. List -2 is ke type. List -3 is new key initialized
                    key = result[i].value
                    list = list.get_public_field(key)[0]

            new_list = Object(types=["object", "list"], keyType=[sub_key_type], objType=[sub_obj_type], original_types=[])

            list.add_public_field(result[-3].value, new_list)  # --> result[-3].value is the new key

            return
        elif len(items.children) == 3:  # --> this means we have listName, key and value
            # if result[0].value in item.public_fields:
            #     raise Exception("Key already exists")
            # else:
            listObjType = item.objType
            if not any(item_type in result[1].types for item_type in listObjType):
                raise Exception("invalid datatypes")
            else:
                item.add_public_field(result[0].value, result[1])
        elif len(items.children) > 3:

            list = item

            for i in range(0, len(items.children) - 3):  # --> iterate list with previous keys
                key = result[i].value
                list = list.get_public_field(key)[0]

            new_key = result[i + 1].value
            value_obj = result[-1]
            if new_key in list.public_fields:
                raise Exception("Key already exi sts")
            else:
                listObjType = list.objType
                if not any(item_type in result[i + 2].types for item_type in
                           listObjType):  # -> +2 for the new value while +1 was the new key
                    raise Exception("invalid datatypes")
                else:
                    list.add_public_field(new_key, value_obj)


    def listget(self,items):
        if len(items.children[0].children) >= 2:  # --> we have obj
            object_name = items.children[0].children[0].children[0].children[0].value
            listName = items.children[0].children[1].value
            try:
                if self.values[object_name].get_public_field(listName):
                    list = self.values[object_name].get_public_field(listName)
            except:
                raise Exception("list not found")
        else:       # --> we dont have obj
            listName = items.children[0].children[0].value
            list = self.values[listName]



        result_keys = []
        for child in items.children[1:]:
            result_keys.append(self.visit(child))
        for i in range(0, len(items.children) - 1):
            if 'list' in list.types:
                for key in list.public_fields:
                    if str(key) == str(result_keys[i].value):
                        list = list.get_public_field(key)[0]
                    else:
                        continue
            else:
                raise ValueError("not a list")
        return list

    def listremove(self,items):
        if len(items.children[0].children) >= 2:  # --> we have obj

            object_name = items.children[0].children[0].children[0].children[0].value
            listName = items.children[0].children[1].value
            try:
                if self.values[object_name].get_public_field(listName):
                    list = self.values[object_name].get_public_field(listName)
            except:
                raise Exception("list not found")
        else:       # --> we dont have obj
            listName = items.children[0].children[0].value
            list = self.values[listName]


        result_keys = []
        for child in items.children[1:]:
            result_keys.append(self.visit(child))

        for key in result_keys[:-1]:
            list = list.get_public_field(key.value)[0]

        if 'list' in list.types:
            removed_value = list.remove_public_field(result_keys[-1].value)
        else:
            raise ValueError("not a list")


        return list




    def paramdecl(self, items):
        return items

    def add(self, node):
        return ContextFunctions.add(self, node)

    def sub(self, node):
        return ContextFunctions.sub(self, node)

    def mul(self, node):
        return ContextFunctions.mul(self, node)

    def div(self, node):
        return ContextFunctions.div(self, node)

    def pow(self, node):
        return ContextFunctions.power(self, node)

    def smaller_equal_than(self, node):
        return ContextFunctions.smaller_equal_than(self, node)
    def smaller_than(self, node):
        return ContextFunctions.smaller_than(self, node)

    def bigger_equal_than(self, node):
        return ContextFunctions.bigger_equal_than(self, node)

    def bigger_than(self, node):
        return ContextFunctions.bigger_than(self, node)

    def equal(self, node):
        return ContextFunctions.equal(self, node)

    def not_equal(self, node):
        return ContextFunctions.not_equal(self, node)

    def derived(self, node):
        derived_name = node.children[0]
        result_derived = self.values[derived_name]
        return result_derived[1].types


    def BOOLEAN(self, token):
        return token.value
    def NAME(self, token):
        return token.value

    def NUMBER(self, token):
        return float(token)
    def STRING(self, token):
        return token.value