from Objects.mainObject import my_Object
from lark import Lark, Tree, Token
# class Helpers:
#
#     def Is_list_or_object(result, return_object):
#         print("is list or object", result)
#         if isinstance(result, my_Object):
#             ret_obj = result
#             return ret_obj
#         elif len(result) > 1:
#             ret_obj, obj = result
#             if return_object:
#                 return  obj
#             else:
#                 return ret_obj
#         else:
#             ret_obj = result
#             return ret_obj
#
#     def search_by_value(values, target_value):
#         for key in values:
#             print("key",key)
#             print("val",values[key])
#             if values[key] == target_value:
#                 return key  # Return the key corresponding to the target value
#                 #return 5
#         return None  # Return None if the value is not found
#
#     @staticmethod
#     def extract_info(tree):
#         data_type = None
#         name = None
#         if not isinstance(tree.children[1], Tree):
#             data_type = tree.children[0].data
#             name = tree.children[1].value
#             yield data_type, name
#         else:
#             for child in tree.children:
#                 if isinstance(child, Tree) and len(child.children) > 0:
#                     data_type = None
#                     name = None
#                     for sub_child in child.children:
#                         if isinstance(sub_child, Tree):
#                             if sub_child.data in ['float', 'int', 'string', 'object', 'var']:
#                                 data_type = sub_child.data
#                             elif sub_child.data == 'derived':
#                                 data_type = sub_child.children[0].value
#                         else:
#                             name = sub_child.value
#                     yield data_type, name
#
#     def extract_info_Old(self, tree):
#         # print("extract child", tree)
#         data_type = None
#         name = None
#         if not isinstance(tree.children[1], Tree):
#             # print("OK")
#             data_type = tree.children[0].data
#             name = tree.children[1].value
#             yield data_type, name
#         else:
#             for child in tree.children:
#                 # print("ok1", child)
#                 if isinstance(child, Tree) and len(child.children) > 0:
#                     # print("ok2", child)
#                     data_type = None
#                     name = None
#                     # if isinstance(child, Tree) :
#                     # print("NOW????",child.children)
#                     for sub_child in child.children:
#                         # print("ok3")
#                         if isinstance(sub_child, Tree) and not data_type:
#                             # print("ok4")
#                             data_type = sub_child.data
#                         else:
#                             # print("ok5")
#                             name = sub_child.value
#                     print(data_type)
#                     print(name)
#                     yield data_type, name

class Helpers:
    @staticmethod
    def Is_list_or_object(result, return_object):
        print("is list or object", result)
        if isinstance(result, my_Object):
            return result
        elif isinstance(result, list) and len(result) > 1:
            ret_obj, obj = result
            if return_object:
                return obj
            else:
                return ret_obj
        else:
            return result

    @staticmethod
    def search_by_value(values, target_value):
        for key, value in values.items():
            print("key", key)
            print("val", value)
            if value == target_value:
                return key  # Return the key corresponding to the target value
        return None  # Return None if the value is not found

    @staticmethod
    def extract_info(tree):
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
                        if isinstance(sub_child, Tree):
                            if sub_child.data in ['float', 'int', 'string', 'object', 'var']:
                                data_type = sub_child.data
                            elif sub_child.data == 'derived':
                                data_type = sub_child.children[0].value
                        else:
                            name = sub_child.value
                    yield data_type, name

    @staticmethod
    def extract_info_Old(tree):
        data_type = None
        name = None
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
                        if isinstance(sub_child, Tree) and not data_type:
                            data_type = sub_child.data
                        else:
                            name = sub_child.value
                    yield data_type, name