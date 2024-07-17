from Objects.mainObject import my_Object
from lark import Lark, Tree, Token

# class LoopStatements():
#     def if_statement(self,node):
#         method = node.children[0]
#
#         newContext = TopDownContextTest(self)
#         result = newContext.visit(method)
#
#         if result.value == True:
#             statement_result = node.children[1] # statement_result is object
#         else :
#             statement_result = node.children[2] # statement_result is object
#
#         return statement_result

# class Helpers:
#     @staticmethod
#     def extract_info(node):
#         var_type = None
#         if isinstance(node, Tree):
#             if node.data == 'paramdecl':
#                 for child in node.children:
#                     if isinstance(child, Tree):
#                         if child.data in ['float', 'int', 'string', 'object', 'var']:
#                             # Basic type
#                             var_type = child.data
#                             var_name = child.children[0]
#                             yield var_type, var_name
#                         elif child.data == 'derived':
#                             # Derived type
#                             var_type = child.children[0]
#                             var_name = child.children[1]
#                             yield var_type, var_name
#                         else:
#                             # Nested paramdecl
#                             yield from Helpers.extract_info(child)
#                     elif isinstance(child, Token):
#                         # Token directly under paramdecl, usually the NAME
#                         var_name = child
#                         yield var_type, var_name

class Helpers:
    @staticmethod
    def extract_info(node):
        var_type = None
        if isinstance(node, Tree):
            if node.data == 'paramdecl':
                for child in node.children:
                    if isinstance(child, Tree):
                        if child.data in ['float', 'int', 'string', 'object', 'var']:
                            var_type = child.data
                            var_name = child.children[0]
                            yield var_type, var_name
                        elif child.data == 'derived':
                            var_type = child.children[0]
                            var_name = child.children[1]
                            yield var_type, var_name
                        else:
                            yield from Helpers.extract_info(child)
                    elif isinstance(child, Token):
                        var_name = child
                        yield var_type, var_name