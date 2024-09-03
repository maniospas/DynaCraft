from lark import Lark
from dynacraft.grammar import grammar
from dynacraft.context import Context


def interpret(code):
    code = code.replace("\n", " ")
    tree = Lark(grammar, start='start', parser='earley').parse(code)
    Context().visit_topdown(tree)


if __name__ == "__main__":
    # input_str = ("""
    #     string x = 'Helloworld';
    #     print(x);
    # """)

    input_str = (""" 
                    string a = "hello21";
                    print(a);
                    """)

    interpret(input_str)