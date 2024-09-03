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
    # input_str = ("""
    #     int x = 1;
    #     string y = tostring(x);
    #     print(y);
    #  """)

    # input_str = ("""
    #     def adder(float x, float y) {
    #         object result = object();
    #         float result.sum = x+y;
    #         return result;
    #     }
    #     adder result = adder(1, 2.0);
    #     print(result);
    # """)

    # input_str = ("""
    #     map[int, map[int, float]] test = map[int, map[int, float]]();
    #     test[1] = map[int, float];
    #     test[1][3] = 0.2;
    #     print(test[1][3]);
    # """)

    # ADD COMMENTS

    # NAME [ NAME ] = EXPR  -> set list item
    input_str = ("""
            object x = object();
            map[int, float] x.test = map[int, float]();
            x.test["A"] = 1.0;
            float result = find(x.test["A"]);
            print(result);
        """)

    interpret(input_str)