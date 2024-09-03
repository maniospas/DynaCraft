from lark import Lark
from dynacraft.grammar import grammar
from dynacraft.context import Context


def interpret(code):
    code = code.replace("\n", " ")
    tree = Lark(grammar, start='start', parser='earley').parse(code)
    Context().visit_topdown(tree)


if __name__ == "__main__":
    # input_str = ("""
    #     def print(float x) {
    #         string message = "hello21";
    #         print(message);
    #     }
    #     float a = 1.0;
    #     print(a);
    #  """)
    #
    # input_str = ("""
    #     print("hello world!");
    #  """)
    #
    #
    # input_str = ("""
    #     int x = 1+2;
    #     print(x);
    #  """)
    #


    input_str = ("""
        int x = 1;
        string y = tostring(x);
        print(y);
     """)

    interpret(input_str)