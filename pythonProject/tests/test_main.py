
import pytest
from main import interpret


# Define test case
def test_sub_result():
    # Input string
    input_str = "float x = 8.0 - 5.0;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    x = result[0]  # Assuming interpret() returns a dictionary

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 3

def test_add_result():
    # Input string
    input_str = "float y = 5.1 + 3.4;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    x = result[0]  # Assuming interpret() returns a dictionary

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 8.5
# #
def test_mull_result():
    # Input string
    input_str = "float m = 3.0 * 3.1;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    x = result[0]  # Assuming interpret() returns a dictionary

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 9.3
# #
def test_div_result():
    # Input string
    input_str = "float d = 12 / 2.5;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    x = result[0]  # Assuming interpret() returns a dictionary

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 4.8
# #
def test_reassignment_result():
    # Input string
    input_str = "float z; z = 10.0;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    z = result[0]  # Assuming interpret() returns a dictionary

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", z)
    assert z.value == 10
# #
# #
def test_sums_result():
    # Input string
    input_str = "float w = 5.0; float q = 13.3; float s; s = w + q + 1;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    w = result[0]  # Assuming interpret() returns a dictionary
    q = result[1]
    s = result[2]

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", w)
    assert w.value == 5

    print("The result is", q)
    assert q.value == 13.3

    print("The result is", s)
    assert s.value == 19.3
# #
# # def test_fun_return_result():
# #     # Input string
# #     input_str = "def test(){ float x = 5; float y = 6; float new = x + y; return new + x;} float a = test();"
# #
# #     # Parse input and interpret
# #     tree, result = interpret(input_str)
# #
# #     # Extract the value of x from the result
# #     x = result[1]  # Assuming interpret() returns a dictionary
# #
# #     # Assert that x equals 3
# #     #print("!!!!", result['x'] )
# #     print("The result is", x)
# #     assert x.value == 16
#
def test_fun_return_result():
    # Input string
    input_str = "def test(){ object o = object(); float x = 5.0; float y = 6.0; float o.new = x + y; return o;} test a = test(); float c = a.new;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    print("res",result)
    x = result[2]  # Assuming interpret() returns a dictionary

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 11
#
def test_fun_return_result_params():
    # Input string
    input_str = "def test(float x, float y){ object o = object(); float selfx = x; float selfy = y; float o.new = selfx + selfy; return o;} test a = test(1,2); float c = a.new;"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # Extract the value of x from the result
    print("res",result)
    x = result[2]  # Assuming interpret() returns a dictionary

    # Assert that x equals 3
    #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 3
#
#
def test_fun_straight_init_params():
    # Input string
    input_str = "def test(){ object o = object(); float x = 6.0; float y = 6.0; float o.new = x + y; return o;} float a = test().new; print_object(a);"

    # Parse input and interpret
    tree, result = interpret(input_str)

    # # Extract the value of x from the result
    print("res",result[1])
    x = result[1]  # Assuming interpret() returns a dictionary
    #
    # # Assert that x equals 3
    # #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 12
# #
# # def test_fun_return_with_params_result():
# #     # Input string
# #     input_str = "def test(float x, float y){ float selfx = x; float selfy = y; float selfz = selfx + selfy ; return selfz + 1;} float b = test(1,2);"
# #
# #     # Parse input and interpret
# #     tree, result = interpret(input_str)
# #
# #     # Extract the value of x from the result
# #     x = result[1]  # Assuming interpret() returns a dictionary
# #
# #     # Assert that x equals 3
# #     #print("!!!!", result['x'] )
# #     print("The result is", x)
# #     assert x.value == 4
# #
# # def test_object_result_result():
# #     # Input string
# #     input_str = "def test(float x, float y){ float selfx = x; float selfy = y; float selfz = selfx + selfy ; } test b = test(1,2); float c = b.selfz;"
# #
# #     # Parse input and interpret
# #     tree, result = interpret(input_str)
# #
# #     # Extract the value of x from the result
# #     x = result[2]  # Assuming interpret() returns a dictionary
# #
# #     # Assert that x equals 3
# #     #print("!!!!", result['x'] )
# #     print("The result is", x)
# #     assert x.value == 3
# #
# def test_if_result():
#     # Input string
#     input_str = "def retbool(){ ! return 0; } if retbool() { float x = 1.0; float y = x+2; } else { float x = 3.0; float y = x*2; } print_object(x); print_object(y);"
#
#     # Parse input and interpret
#     tree, result = interpret(input_str)
#     print("!@!!!!!!!!!!!!!!!!!!!!!", result)
#     print("!@!!!!!!!!!!!!!!!!!!!!!", result[2][0])
#     print("!@!!!!!!!!!!!!!!!!!!!!!", result)
#     # Extract the value of x from the result
#     x = result[2][0]  # Assuming interpret() returns a dictionary
#     y = result[3][0]
#     print("!@!!!!!!!!!!!!!!!!!!!!!",result)
#     # Assert that x equals 3
#     #print("!!!!", result['x'] )
#     print("The result is", x)
#     assert x.value == 3
#
#     print("The result is", y)
#     assert y.value == 6
# #
def test_while_result():
    # Input string
    input_str = "float i = 1.0; float y = 2.0;  while i<=3: { y = y*y; i=i+1; } print_object(y); print_object(i);"
    tree, result = interpret(input_str)
#
def test_same_name_fun_result():
    # Input string
    input_str = "def test(float x, float y){ object o = object(); float o.z = x + y ; return o;} def test(int x, int y){ object o = object(); float o.z = x * y ; return o;} test b = test(5, 6); float c = b.z; print_object(c);"
    # Parse input and interpret
    tree, result = interpret(input_str)

    # # Extract the value of x from the result
    print("res", result[3])
    x = result[3]  # Assuming interpret() returns a dictionary
    #
    # # Assert that x equals 3
    # #print("!!!!", result['x'] )
    print("The result is", x)
    assert x.value == 11

def test_fibbo_fun_result():
    # Input string
    input_str = "def fibbo(float x){ object o = object(); if x<=1: {float o.c = x;} else {float temp1 = x-1; float temp2 = x-2; float a = fibbo(temp1).c; float b = fibbo(temp2).c; float o.c = a+b;} return o;} float x = fibbo(9).c; print_object(x);"
    # Parse input and interpret
    tree, result = interpret(input_str)

    # # Extract the value of x from the result
    print("res", result[1])
    x = result[1]  # Assuming interpret() returns a dictionary
    #
    # # Assert that x equals 3
    # #print("!!!!", result['x'] )
    #print("The result is", x)
    assert x.value == 34

# Run the test
if __name__ == "__main__":
    pytest.main()