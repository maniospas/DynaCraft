from dynacraft.objects.object import Object
from lark import Lark, Tree, Token

class helpers:
    @staticmethod
    def Is_list_or_object(result, return_object):
        if isinstance(result, Object):
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