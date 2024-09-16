from dynacraft.interpreter import interpret


if __name__ == "__main__":
    input_str = ("""
        def c1() {
            return 1.0;
        }
        def test(float x) {
            print("hello21");
        }
        def test(int x) {
            print("hello21");
        }
        def test(int x) {
            print("hello21");
        }
        c1 a = c1();
        test(a);
     """)
    interpret(input_str)