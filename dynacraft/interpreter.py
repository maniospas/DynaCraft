from lark import Lark, Tree
from dynacraft.grammar import grammar
from dynacraft.context import Context


def interpret(code):
    code = code.replace("\n", " ")
    tree = Lark(grammar, start='start', parser='lalr').parse(code)
    #print(tree.pretty())
    Context().visit_topdown(tree)
