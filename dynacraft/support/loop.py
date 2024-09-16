from dynacraft import helpers
from lark import Tree, Token


def extract_info(node):
    var_type = None
    if isinstance(node, Tree):
        if node.data == 'paramdecl':
            for child in node.children:
                if isinstance(child, Tree):
                    if child.data in ['float', 'int', 'string', 'object', 'var', 'bool']:
                        var_type = child.data
                        var_name = child.children[0]
                        yield var_type, var_name
                    elif child.data == 'derived':
                        var_type = child.children[0]
                        var_name = child.children[1]
                        yield var_type, var_name
                    else:
                        yield from helpers.extract_info(child)
                elif isinstance(child, Token):
                    var_name = child
                    yield var_type, var_name