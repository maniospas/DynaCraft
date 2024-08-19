from lark import Lark
from dynacraft.grammar import grammar
from dynacraft.context import Context


def interpret(code):
    code = code.replace("\n", " ")
    tree = Lark(grammar, start='start', parser='earley').parse(code)
    Context().visit_topdown(tree)


if __name__ == "__main__":
    input_str = ("""
        int x = 1;
        print(z);
    """)
    interpret(input_str)