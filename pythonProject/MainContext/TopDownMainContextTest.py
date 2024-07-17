from lark import Interpreter
from lark import Lark, Tree, Token
from Objects.mainObject import my_Object
from myLogger import print_info
from MyLib.MainFunctions.BasicFunctions import Functions
from MainContext.subFiles.ContextFunctions import ContextFunctions as ContextFuns
from MainContext.subFiles.CoreStatements import CoreStatements
from MainContext.subFiles.Helpers.Helpers import  Helpers
class TopDownContextTest(Interpreter):
    def __init__(self, parent=None):
        self.parent = None
        self.types = {}  # {"x": "float"}
        self.values = {}
        self.variables = {}
        #self.varValues = {}
        self.temp_funs = []
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
        return CoreStatements.start(self, node)


    def statement(self, node):
        return CoreStatements.statement(self, node)

    def semicolonstatements(self, node):
        return CoreStatements.semicolonstatements(self, node)

    def basicstatement(self, node):
        return CoreStatements.basicstatement(self, node)

    def assignment(self, node):
        result = []
        print("These are the assignment items", node)
        result.append(node.children[0]) # append 1st child which is assignment type
        if result[0].data == "derived":
            temp = node.children[1]  # append 1st child which is var name
            #print("!-!_!_!_!_!_It is an object init", result[0])
            #print("!-!_!_!_!_!_VAR NAME", temp.children[0].value)
            var_name = temp.children[0].value
            der_result = self.visit(result[0])
            #print("The derived child is", der_result)
            for child in node.children[1:]:
                #print("The assignment child is", child)
                result.append(self.visit(child))

            res = Helpers.Is_list_or_object(result[2], 1)

            self.values[var_name] = res
            #print("the item name i s ", var_name)
            print_info(f"The saved item: {self.values[var_name]}")
            #del self.values["temp"]
            return self.values[var_name]
        else :
            #print("!-!_!_!_!_!_It is NOT an object init", result[0])
            for child in node.children[1:]:
                #print("The ASSignment child is", child)
                result.append(self.visit(child))
            #print("Return from assign 1 child:", result)
            #print("Return from assign o child:", result[0])
            #print("Return from assign 1 child:", result[1])
            #print("Return from assign 2 child:", result[2])
            #print("Return from assign 2 child types:", result[2].types)
            # if isinstance(result[2], my_Object):
            #     ret_obj = result[2]
            # elif len(result[2])>1 :
            #     ret_obj, obj = result[2]
            # else :
            #     ret_obj = result[2]

            res = Helpers.Is_list_or_object(result[2], 0)

            #ret_obj, obj = result[2]
            print("Return from res child:", res)
            #print("Return from assign 2 child:", obj)
            print("RES111",result[1])
            print("RES111", result[1].fields)
            if 'value' in result[1].fields:
                #print("what")
                var_name = result[1].value.value
                var_type = result[0].data
                print("res 2 types", result[2].types)
                print("res 2 types", result[2])
                #var_value = res.value
                if var_type  in result[2].types:
                    if 'value' in result[2].fields:
                        print("111111111111111111111111111111111111", var_name)
                        var_value = res.value
                        #print(f"type: {var_type}, name: {var_name}, value: {var_value}")
                        #self.values[var_name] = my_Object({"value": float(var_value)}, types=["object", var_type])
                        self.values[var_name] = result[2]
                        print_info(f"The saved item: {self.values[var_name]}")
                        return self.values[var_name]
                    elif var_type == "object":
                        print("22222222222222222222222222222222222222", var_name)
                        self.values[var_name] = my_Object(types=["object"])
                        print_info(f"The saved item: {self.values[var_name]}")
                        return self.values[var_name]
                    else:
                        print("3333333333333333333333333333333333333333",var_name)
                        print(f"type: {var_type}, name: {var_name}")
                        self.values[var_name] = my_Object(types=["object", var_type])
                        print_info(f"The saved item: {self.values[var_name]}")
                        return self.values[var_name]
                else:
                    raise ValueError("Invalid type")
            else:
                print("here we go", result[1])
                print("4444444444444444444444444444444",result[1])
                var_type = result[0].data
                print("4444444444444444444444444444444", var_type)
                print("res2", result[2].fields['value'])
                if var_type in result[2].types:
                    print(result[1].fields)
                    index = result[2].types.index(var_type)
                    new_types_list = result[2].types[:index+1]
                    #result[1].fields.append({'value': {result[2].fields['value']}})
                    result[1].fields['value'] = result[2].fields['value']
                    result[1].types = new_types_list
                    print(res)
                    print("==================Correct",result[1])
                    return result[1]
                else:
                    raise ValueError("Invalid type")


    def reassignment(self, node):
        result = []
        #print("These are the reassignment items", node)
        #result.append(node.children[0])  # append 1st child which is assignment type
        print("This",node.children[0])
        #result.append(node.children[0])  # append 1st child which is assignment type
        # if result[0].data == "assignable":
        #     temp = node.children[1]  # append 1st child which is var name
        #     print("!-!_!_!_!_!_It is an object reassign", result[0])
        #     # print("!-!_!_!_!_!_VAR NAME", temp.children[0].value)
        #     #print("!-!_!_!_!_!_VAR NAME", node.children[0].children[1])
        #     main_item = node.children[0].children[0].children[0].children[0].value
        #     sub_item = node.children[0].children[1]
        #
        #     item = self.values[main_item].fields[sub_item]
        #     #print("!-!_!_!_!_!_VAR NAME", item)
        #     print(node.children[1].children[0].children[0])
        #     if isinstance(node.children[1].children[0].children[0], Tree):
        #         assignable_name = node.children[1].children[0].children[0].children[0].value
        #         print("Oh", assignable_name)
        #         item.fields["value"] = self.values[assignable_name].value
        #     else:
        #         item.fields["value"] = node.children[1].children[0].children[0].value
        #
        #     return item
        # else:
        #     # print("!-!_!_!_!_!_It is NOT an object init", result[0])
        #     for child in node.children[1:]:
        #         # print("The ASSignment child is", child)
        #         result.append(self.visit(child))

        for child in node.children:
            #print("The assignment child is", child)
            result.append(self.visit(child))
        print(result)
        var_name = result[0].value
        var_value = result[1].value
        #print(f"result: {var_name}, {var_value}, {result}")
        if var_name in self.values:
            already_assigned = set(self.values[var_name].types)
            to_assign = set(result[1].types)
            if already_assigned.issubset(to_assign):
                self.values[var_name].fields['value'] = var_value
                #print_info(f"The reassigned item: {self.values[var_name]}")
                return self.values[var_name]
            else:
                print("???????")
        else :
            raise ValueError("Variable {} has not been assigned before.".format(var_name))


    def evaluate_expression(self, operands):
        #print("These are the evaluate_expression items", operands)
        return operands

    def var_decl(self, node):
        #print("These are the var_decl items", node)
        result = []
        var_type = node.children[0].data # append 1st child which is decl type
        var_name = node.children[1]  # append 2st child which is decl name
        if var_type != "object":
            self.values[var_name] = my_Object({}, types=["object", var_type])
        else:
            self.values[var_name] = my_Object({}, types=["object"])
        #print_info(f"The declared saved item: {self.values[var_name]}")
        return self.values[var_name]

    def expression(self, node):
       # print("???????The expression is", node)
        for child in node.children:
            #print("The expression child is", child)
            result = self.visit(child)
            #print("The expression is", result)
        return result

    def simpleexpression(self, node):
        #print("???????The simple expression is", node)
        var_assign = ''
        var_object = ''

        for child in node.children:
            print("The simpleexpression child is", node)
            print("The simpleexpression child is", child)
            if isinstance(child, Tree):
                print("The dara child is", child.children[0])
                print("The dara child is", child.children)
                if child.data == "methodcall":
                    print("################1")
                    result = self.visit(child)

                else:
                    print("###############2")
                    for sub_child in child.children:
                        print("-->the sub child is", sub_child)
                        if isinstance(sub_child, Tree):
                            print("__>>>>>>>>>>>>>", sub_child);
                            if sub_child.children[0].data == "methodcall" :
                                #print("innnnn", sub_child);
                                result = self.visit(sub_child.children[0])
                                var_object = result
                                #print("$$$$$$$$$$$$$$$$$$$$$$NOW THE RESUME",result);
                                #print("$$$$$$$$$$$$$$$$$$$$$$NOW THE RESUME", var_object.fields);
                                print(sub_child.children[0].children[0].children[0])
                                print(sub_child.children[0].children[0].children[0].children[0].value)
                            else:
                                #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!var assign", sub_child.children[0].children[0])
                                var_assign = (sub_child.children[0].children[0].value)
                                #print("the", var_assign)
                                #print_info("The sub simpleexpression child is", sub_child.children[0].children[0])
                                #print_info("The sub simpleexpression child is", var_assign)
                                continue;
                        #     if sub_child.data == "simpleexpression":
                        #         print("The sub simpleexpression child is", sub_child)
                        #         result = self.visit(sub_child)
                        elif var_object != '':
                            print("Now the sub", var_object)
                            sub_obj = var_object.fields[sub_child]
                            #print("Now the new obj", sub_obj)
                            return sub_obj
                        elif var_assign != '':
                            print("Now the sub", var_assign)
                            print("Now the obj", self.values)
                            print("Now the obj", self.values[var_assign].fields)
                            #print("Now the obj", sub_child)
                            #print("Now the obj222", self.values["a"].fields["new"])
                            value_list = self.values[var_assign].fields
                            #print("Now the test", self.values[var_assign])
                            obj = self.values[var_assign]
                            sub_obj = obj.fields[sub_child]
                            #print("Now the obj list", test.field)
                            #for value in value_list:
                                #print(type(value))
                                #print(value['new'])
                                #if sub_child in value:
                                    #return value["o"]
                            return sub_obj
                            #print("No result?")
                        elif hasattr(Functions, sub_child):
                            self.temp_funs = sub_child
                            #print("ok?!", self.temp_funs)
                            result = my_Object()
                            return result
                        else:
                            #print("in here?", sub_child)
                            #print(self.values)
                            var_name = sub_child.value
                            #print("type", self.values[var_name][0])
                            #var_type = self.values[var_name][0]
                            #print("The sub_child is", self.values[var_name].types)

                            if isinstance(self.values[var_name], list):
                                if "function" in self.values[var_name]:
                                    print("fun",self.values[var_name])
                                    return var_name
                                #if simple expression is of type function return its name instead of value
                            #var_value = self.values[var_name].value
                            result = self.values[var_name]
                            return result
            else:
                print("x is not a Tree")
                print("###############3")
                if child.isdigit():
                    #print("x is an integer")
                    result_value = int(child)
                    result = my_Object({"value": result_value}, types=["object", "int"])
                elif child.count('.') == 1 and child.replace('.', '', 1).isdigit():
                   # print("x is a float")
                    result_value = float(child)
                    result = my_Object({"value": result_value}, types=["object", "float"])

                else :
                    #print("The  child is NOT num", child)
                    result = self.visit(child)
            return result

    def assignable(self, node):
        #print("The assignable are", node)
        if len(node.children)>1:
            print(len(node.children))
            #print("node.children",node.children)
            result = self.visit(node.children[0])
            #print("the ret is",result)

            #print("node.children2", node.children[1])

            var_name = Helpers.search_by_value(self.values, result)
            #print("The name is", var_name)
            sub_object = my_Object({}, types=["object"])
            existing_obj = self.values[var_name]
            existing_obj.fields[var_name] = sub_object
            existing_obj.fields[f"{node.children[1]}"] = sub_object
            #print(result)
            #print("now?", self.values[var_name])
            return sub_object

        else:
            for child in node.children:
                #print("The assignable child is", child)
                result_value = child
                result = my_Object({"value": result_value}, types=["object", "assignable"])
                #print("The assignable result is", result)
            return result

    def methodcall(self, node):
        #print("The methodcall is", node)
        print("!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@The methodcall is", self.values)

        print("node children", node.children)
        if len(node.children) > 1:
            param_list = node.children[1:]
        else:
            param_list = []

        #for child in node.children[0]:    #only the first item is tree, the others are the params
        #print("HERE PRE?-2", node.children[0])
        result = self.visit(node.children[0])
        #print("0.5",result)

        #print("HERE PRE?-1")

        if isinstance(result, my_Object) and result.is_empty():
            if len(node.children) >1 :
                #print("!!!!!!!!!!!!!!!!!!!!", len(node.children))
                obj = self.values[node.children[1].value]
                print(self.temp_funs)
                #method_to_call = getattr(obj, self.temp_funs.value, True)
                function_obj = Functions()
                method_name = self.temp_funs.value
                if method_name:
                    method_to_call = getattr(function_obj, method_name, None)
                    #print(method_to_call)
                    if method_to_call:
                        method_to_call(obj)
                    else:
                        print(f"Method '{method_name}' does not exist in Function")
                else:
                    print("No method specified in temp_funs")
                #print("Result is an empty instance of my_Object", obj)
                return my_Object()
            else:
                #print("!!!!!!!!!!!!!!!!!!!!", len(node.children))
                function_obj = Functions()
                method_name = self.temp_funs.value
                if method_name:
                    method_to_call = getattr(function_obj, method_name, None)
                    #print(method_to_call)
                    if method_to_call:
                        return method_to_call()
                    else:
                        print(f"Method '{method_name}' does not exist in Function")
                else:
                    print("No method specified in temp_funs")
                #print("Result is an empty instance of my_Object", obj)
                return my_Object()
        #print("The methodcall child is", result)
        method_name = result
        #print("The method is", self.values[method_name])

        #print("HERE PRE?0")

        newContext = TopDownContextTest(self)
        index = 0;

        param_list_types = []
        print("paramlist check", param_list)
        for param in param_list:
            print("One of the params is", param)
            print("values ", self.values)
            print(param_list[index])
            print("list is", param_list[index].type)
            if param_list[index] in self.values:
                print("OK", self.values[param_list[index]].types[1])
                param_type = self.values[param_list[index]].types[1]
                #print("param", param_type[])
                #print("obj type", param_type)
            else:
                print("NOT OK", param_list[index].type)
                param_type = param_list[index].type
                #print("type", param_type)
                if 'NUMBER' in param_type:
                    param_type = 'float'
            param_list_types.append(param_type)
            index += 1

        index = 0;
        print("types", param_list_types)
        for item in self.values[method_name][1:]:
            print(item)
            flat_list = [inner[0] for inner in item.fields["params"]]
            print("fun params", flat_list)
            print(param_list_types)
            if flat_list == param_list_types:
                #print("OKKK")
                method = item

        for value in self.values:
            newContext.values[value] = []
            #print("val now", value)
            #print("val now",self.values[value])
            if isinstance(self.values[value], my_Object):
                #print("int")
                obj = my_Object()
                obj.fields = self.values[value].fields
                obj.types = self.values[value].types
                newContext.values[value].append(obj)
            elif len(self.values[value]) >1:
                #print("000000")
                newContext.values[value].append("function")
                for sub_item in self.values[value][1:]:
                    obj = my_Object();
                    obj.fields = sub_item.fields
                    obj.types = sub_item.types
                    newContext.values[value].append(obj)
            else:
                print("!!!!!!!!")

        print("Into params")
        print(method.fields["params"])
        if method.fields["params"] :
            for param in method.params: #SOS TO ADD TYPE CHECK
                print("The param is ", param)
                if param_list[index] in self.values:
                    try:
                        print("ok", self.values[param_list[index]])
                        print("ok", self.values[param_list[index]].fields["value"])
                        param_value = self.values[param_list[index]].value
                    except (IndexError, AttributeError, KeyError) as e:
                        print("good", param)
                        print("good", param[1])
                        print("good", self.values[param_list[index]])
                        newContext.values[param[1]] = self.values[param_list[index]]
                        print(newContext.values[param[1]])
                        index += 1
                        continue;
                else :
                    param_value = float(param_list[index])
                #print("The param is ", param_list[index])
                param_type = param[0]
                param_name = param[1]
                newContext.values[param_name] = my_Object({"value": param_value}, types=["object", param_type])
                index += 1
                print("The new vals are", newContext.values)
                print("The new vals are", newContext.values["a"])
                #print("The param is", param)
        #print("!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@the Into the method call")
        print("HERE PRE?",method.body)
        result = newContext.visit(method.body)
        #print("3", result)
        #print("!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@the result", result)
        # if result.fields['value']:
        #     print(result)
        #     return result
        #print("!!!!!!!!!!!!!!!!!!!!!!!!_________________________________!!!!!!!!!!!!!!!!!!")
        obj_result = my_Object({}, types=["object", "test"])
        for key, value in list(newContext.values.items())[2:]:
            #print(f":{key}, :{value}",)
            var_name = key
            #print("-->", str(var_name))
            #self.values["temp"].fields.append({item: newContext.values[item]})
            obj_result.fields[var_name] = newContext.values[key]
            #obj_result.fields.append({f"{var_name}" : newContext.values[key]})  #????????????????????????????????
            #obj_result.fields[index] = newContext.values[key]
            #print("the method call NOWWW return values are:", obj_result.fields)
        #print("the method call return values are:", obj_result.fields)
        #print("the method call return is:", result)
        #print("the obj is:", obj_result)
        #print("the res is:", result)
        #return [result, obj_result]
        #print("1",result.fields["new"])
        #print("2",obj_result)
        result.types.append(method_name)
        print("------------------the method call result", result)
        return result;

    def method_decl(self, node):
        print("-------------------------Declare function", node)
        #print("Fun name:", node.children[0].value)
        print("whar", node.children[1])
        #print("body", node.children[2])
        method_name = node.children[0].value
        print("node ", node.children[1])
        method_params = self.visit(node.children[1])   #visit declare params
        for param in method_params:
            print("the param is", param)
        print("method params", method_params)
        method_body = node.children[2]
        self.types[method_name] = ["object", method_name]
        #HOW CAN I GET RETURN VAL WITHOUT TRAVERSING THE TREE??????????!!!!!SOS
        param_types = [sublist[0] for sublist in method_params]
        #print("&&&&&&&&&The param types are", param_types)
        if method_name not in self.values:
            self.values[method_name] = []
            self.values[method_name].append("function")
        self.values[method_name].append(my_Object({"param_types": param_types, "params": method_params,"body": method_body}, types=["object", "function", method_name]))
        #self.values[method_name] = my_Object({"param_types": param_types, "params": method_params,"body": method_body}, types=["object", "function", method_name])
        #print_info(f"The saved method: {self.values[method_name]}")
        return self.values[method_name]

    def codeblock(self, node):
        #print("codeblock is", node)
        #newContext = TopDownContext(self)

        for child in node.children:
            print("The codeblock child is", child)
            result = self.visit(child)
        print("return from codeblock", result)
        return result

    def returns(self, node):
        print("!_!__!_______Into return", node)
        for child in node.children:
            #print("The codeblock child is", child)
            result = (self.visit(child))
        print("return result", result)
        return result

    def if_statement(self, node): ## to check data type
        #print("HOLLAAAAAAAAAAAAAAA", node)
        #for child in node.children :
            #print(child)
        result = self.visit(node.children[0])
        #print("child res", result)
        res = Helpers.Is_list_or_object(result, 0)
        #print("child res", res)
        if res.value == 1: ##if object is my_bool and value == true
            result = self.visit(node.children[1])
        else:
            result = self.visit(node.children[2])
        #print("______________________The res are",result)
        #print(self.values)

    def while_statement(self, node): ## to check data type
        #print("HOLLAAAAAAAAAAAAAAA", node)
        for child in node.children :
            print("CHILEDDDDDDDDDD",child)
        print("the chile", node.children[0])
        # while self.visit(node.children[0]).value == 1 :
        #     self.visit(node.children[1])
        #     print("RET",self.visit(node.children[0]))
        #     print("TRUE")
        self.visit(node.children[0])
        #result = self.visit(node.children[0])
        #print("child res", result)


    def extract_info(self, tree):
        #print("extract child", tree)
        data_type = None
        name = None
        if not isinstance(tree.children[1], Tree):
            #print("OK")
            data_type = tree.children[0].data
            name = tree.children[1].value
            yield data_type, name
        else:
            for child in tree.children:
                #print("ok1", child)
                if isinstance(child, Tree) and len(child.children)>0:
                    #print("ok2", child)
                    data_type = None
                    name = None
                #if isinstance(child, Tree) :
                    #print("NOW????",child.children)
                    for sub_child in child.children:
                        #print("ok3")
                        if isinstance(sub_child, Tree) and not data_type:
                            #print("ok4")
                            data_type = sub_child.data
                        else:
                            #print("ok5")
                            name = sub_child.value
                    print(data_type)
                    print(name)
                    yield data_type, name
        #     else:
        #         if not data_type:
        #             data_type = child.data
        #         else:
        #             name = child.value
        # #print(data_type)
        # #print(name)
        #     yield data_type, name

    def methodparams(self, node):
        param_result = []
        print("Method params are", node.children)
        if node.children:
            print("child methodparams is ", node.children)
            print(node.children[0])
            for var_type, var_name in self.extract_info(node.children[0]):
                print(var_type)
                print(var_name)
                if var_name not in param_result:
                    param_result.append([var_type, var_name])
                    #print("Data Type:", var_type)
                    #print("Name:", var_name)
        #print("finally the params", param_result)
        return param_result

    def methodparams(self, node):
        param_result = []
        print("Method params are", node.children)
        if node.children:
            print("Child methodparams are", node.children)
            for child in node.children:
                for var_type, var_name in Helpers.extract_info(child):
                    print("Var type:", var_type)
                    print("Var name:", var_name)
                    if [var_type, var_name] not in param_result:
                        param_result.append([var_type, var_name])
        return param_result

    def paramdecl(self, items):
        print("________________________paramdecl are", items)
        return items

    def add(self, node):
        return ContextFuns.add(self, node)

    def sub(self, node):
        return ContextFuns.sub(self, node)

    def mul(self, node):
        return ContextFuns.mul(self, node)

    def div(self, node):
        return ContextFuns.div(self, node)

    def smaller_than(self, node):
        print("!!!!!!!!!!!!!!!!!!!!",node)
        return ContextFuns.smaller_than(self, node)

    def derived(self, node):
        #print("???????????????????The derived tokens are", node.children[0])
        derived_name = node.children[0]
        #print("The derived result is", self.values)
        result_derived = self.values[derived_name]
        #print("The derived result is", result_derived)
        #return

    def NAME(self, token):
        #print("The Names are", token)
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