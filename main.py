from lark import Lark
from dynacraft.grammar import grammar
from dynacraft.context import Context


def interpret(code):
    code = code.replace("\n", " ")
    tree = Lark(grammar, start='start', parser='lalr').parse(code)
    Context().visit_topdown(tree)


if __name__ == "__main__":
    input_str = ("""
        def print(float x) {
            string message = "hello21";
            print(message);
        }
        float a = 1.0;
        print(a);
     """)
    #
    input_str = ("""

            def sum(int x, int y) {
                int z = x + y + 1;
                return z;
            }

            def sum(float x, float y) {
                float z = x + y;
                return z;
            }

            float a = sum(3, 5);
            print(a);
         """)
    #
    input_str = ("""



                def sum(float x, float y) {
                    float z = x + y;
                    return z;
                }

                def sum(float x, float y) {
                    float z = x + y + 1;
                    return z;
                }

                float a = sum(3.0, 5.0);
                print(a);
             """)
    #
    input_str = ("""
        print("B4T");
     """)
    # # #
    # # #
    input_str = ("""
        int x = 1+2;
        print(x);
     """)
    # # #
    input_str = ("""
            string x = "HELLO WORLD";
            print(x);
         """)
    # # #
    # # #
    input_str = ("""
        int x = 1;
        string y = tostring(x);
        print(y);
     """)
    # # #
    input_str = ("""
        def adder(float x, float y) {
            object result = object();
            float result.sum = x+y;
            return result;
        }
        adder result = adder(1, 2.0);
        print(result);
    """)
    # #
    input_str = ("""
        map[int, map[int, float]] test = map[int, map[int, float]]();
        test[1] = map[int, float];
        test[1][3] = 0.2;
        float result = test[1][3];
        print(test[1][3]);
    """)
    # #
    # #
    input_str = ("""
            object x = object();
            map[int, map[int, float]] x.test = map[int, map[int, float]]();
            x.test[1] = map[int, float];
            x.test[1][3] = 0.3;
            float result = x.test[1][3];
            print(x.test[1][3]);
            """)
    input_str = ("""
            map[int, map[int, map[int, float]]] test = map[int, map[int, map[int, float]]]();
            test[1] = map[int, map[int, float]];
            test[1][3] = map[int, float];
            test[1][3][4] = 0.2;
            float result = test[1][3][4];
            print(result);
        """)
    #
    #
    input_str = ("""
                map[int, map[int, map[int, float]]] test = map[int, map[int, map[int, float]]]();
                test[1] = map[int, map[int, float]];
                test[1][2] = map[int, float];
                test[1][2][1] = 4.0;
                float result = test[1][2][1];
                print(result);
            """)





    # ADD COMMENTS

    # NAME [ NAME ] = EXPR  -> set list item

    # input_str = ("""
    #         object x = object();
    #         map[string, float] x.test = map[string, float]();
    #         x.test["A"] = 1.0;
    #         float result = x.test["A"];
    #         print(result);
    #     """)
    # # #
    # input_str = ("""
    #             map[int, float] test = map[int, float]();
    #             test[1] = 1.0;
    #             float result = test[1];
    #             print(result);
    #         """)
    #
    # input_str = ("""
    #         def adder(float x, float y) {
    #             object result = object();
    #             float result.sum = x+y;
    #             return result;
    #         }
    #
    #         print(adder(1, 2.0));
    #     """)

    interpret(input_str)