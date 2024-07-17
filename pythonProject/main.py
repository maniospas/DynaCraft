
print('hello world')

from lark import Lark
#from lark.tree import pydot__tree_to_png
from IPython.display import Image, display
from Grammar.grammar import parser
from Grammar.grammar import grammar
from OldContexts.oldTransformer import MyTransformer
from OldContexts.mainContext import Context
from MainContext.TopDownMainContextTest2 import TopDownContextTest2
from myLogger import print_expression_tree

# Example usage:
transformer = MyTransformer()

transformer = Context()

transformer = TopDownContextTest2()

parser = Lark(grammar, start='start', parser='earley')




def interpret(code):
    tree = parser.parse(code)
    result = transformer.visit_topdown(tree)
    return tree, result


# print("___________________Example N1____________________________")
# # Parse input
# input_str = "float x = 8 - 5;"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# display(Image(png_filename))
# res2 = test
# print("res", res2[0].value)

# Test the interpreter
# result = interpret(input_str);
# print(result);
#
# print("___________________Example N2____________________________")
# #
# # Parse input
# input_str = "float y = 5.1 + 3.4;"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
# #
# # # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
# #
# # # Display the PNG image directly in the notebook
# display(Image(png_filename))
#
# res2 = test
# print("res", res2[0].value)
#
# # Test the interpreter
# result = interpret(input_str);
# print(result);
#
# print("___________________Example N3____________________________")  ##to see again
# #
# # # Parse input
# input_str = "float z; z = 10.0;"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
# #
# # # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
# #
# # # Display the PNG image directly in the notebook
# display(Image(png_filename))
# #
# res2 = test
# print("res", res2[1].value)
# # Test the interpreter
# result = interpret(input_str);
# print(result);
#
# print("___________________Example N4____________________________")
# #
# # # Parse input
# input_str = "float w = 5; float q = 13.3; float s =  w + q + 1;"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
# #
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
# #
# # # Display the PNG image directly in the notebook
# display(Image(png_filename))
# #
#
# res2 = test
# print("res", res2[2].value)
# Test the interpreter
# result = interpret(input_str);
# print(result);
# #
# # print("___________________Example N5____________________________")
# #
# # # Parse input
# # input_str = "method(4,6);"
# # parse_tree = interpret(input_str)
# # print_expression_tree(parse_tree.pretty())
# #
# # # Convert the parse tree to a PNG image and save it to a file
# # png_filename = 'parse_tree.png'
# # pydot__tree_to_png(parse_tree, png_filename)
# #
# # # Display the PNG image directly in the notebook
# # display(Image(png_filename))
# #
# # # Test the interpreter
# # result = interpret(input_str);
# # print(result);
# #
# #
# print("___________________Example N6____________________________")
#
# # Parse input
# input_str = "int m = 3 * 3.1;"
# parse_tree = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# display(Image(png_filename))
# #
# # # Test the interpreter
# # result = interpret(input_str);
# # print(result);
# #
# print("___________________Example N7____________________________")
#
# # Parse input
# input_str = "int d = 12 / 2.5;"
# parse_tree = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# display(Image(png_filename))
# #
# # # Test the interpreter
# # result = interpret(input_str);
# # print(result);
#
# # print("___________________Example N8____________________________")
# #
# # # Parse input
# # input_str = "int d = 12 / 0;"
# # parse_tree = interpret(input_str)
# # print_expression_tree(parse_tree.pretty())
# #
# # # Convert the parse tree to a PNG image and save it to a file
# # png_filename = 'parse_tree.png'
# # pydot__tree_to_png(parse_tree, png_filename)
# #
# # # Display the PNG image directly in the notebook
# # display(Image(png_filename))
# #
# # # Test the interpreter
# # result = interpret(input_str);
# # print(result);
#
# print("___________________Example N9____________________________")
#
# # # Parse input
# input_str = "def test(){ object o = object(); float x = 5.0; float y = 6.0; float o.new = x + y; ! return o;} "
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
#pydot__tree_to_png(parse_tree, png_filename)

# Display the PNG image directly in the notebook
#display(Image(png_filename))

# res2 = test
# print(f"res: {res2[1]}")

# # Test the interpreter
# result = interpret(input_str);
# print(result);
#
# #
# print("___________________Example N10____________________________")
#
# # Parse input
# input_str = "def test(float x, float y){ object o = object(); float selfx = x; float selfy = y; float selfz = selfx + selfy ; object o.z = selfz + 1; return o.z;} float b = test(1,2); "
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# display(Image(png_filename))
#
# res2 = test
# print(f"res: {res2[0]}, {res2[1]}")
# #
# # # Test the interpreter
# # result = interpret(input_str);
# # print(result);


# print("___________________Example N11____________________________")
#
# # Parse input
# input_str = "def test(float x, float y){ float selfx = x; float selfy = y; float selfz = selfx + selfy ; } test b = test(1,2); float c = b.selfz; print_object(c);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# display(Image(png_filename))
#
# res2 = test
# print(f"res: {res2[2]}")

# print("___________________Example N12____________________________")
#
# # # Parse input
# input_str = "def retbool(){ return 0 ; } if retbool() { float x = 1; float y = x+2; } else { float x = 3; float y = x*2; } print_object(x); print_object(y);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# # display(Image(png_filename))
# #
# res2 = test
# print(f"!!!!!!!!!!res: {res2[3][0]}")

# print("___________________Example N12____________________________")
#
# # Parse input
# input_str = "float i = 1; float y =2;  while i<=3: { y = y*y; i=i+1; } print_object(y); print_object(i);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# display(Image(png_filename))

# res2 = test

# # print("___________________Example N13____________________________")
# #
# # # Parse input
# input_str = "float a = 5.2; print_object(a); object c = object();"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
#
# # Convert the parse tree to a PNG image and save it to a file
# png_filename = 'parse_tree.png'
# pydot__tree_to_png(parse_tree, png_filename)
#
# # Display the PNG image directly in the notebook
# display(Image(png_filename))

# # print("___________________Example N13____________________________")
# #
# # # Parse input
#
# input_str = "def test(float x, float y){ object o = object(); float o.x = x; float o.y = y; float o.z = o.x + o.y ; ! return o;} float a = 5.0; test b = a.test(4.0); float c = b.z; print_object(c);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# Convert the parse tree to a PNG image and save it to a file
#png_filename = 'parse_tree.png'
#pydot__tree_to_png(parse_tree, png_filename)

# Display the PNG image directly in the notebook
#display(Image(png_filename))

# # print("___________________Example N14____________________________")
# #
# # # Parse input
#
# input_str = "def test(float x, float y){ object o = object(); float o.z = x + y ; ! return o;} def test(int x, int y){ object o = object(); float o.z = x * y ; ! return o;} test b = test(5, 6); float c = b.z; print_object(c);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# # print("___________________Example N15____________________________")
# #
# # # Parse input
#
# input_str = "float i = 1.0; float y = 2.0;  while i<=3: { y = y*y; i=i+1; } print_object(y); print_object(i); print_object(y);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# # print("___________________Example N15____________________________")
# #
# # # Parse input
#
# input_str = "def fibbo(){ object o = object(); float a = 0.0; float b = 1.0; float temp = 0.0; while temp<=33: { temp = a + b; a = b; b = temp; }  float o.i = temp; ! return o;} float x = fibbo().i; print_object(x);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# # print("___________________Example N15____________________________")
# #
# # # Parse input
#
# input_str = "def fibbo(float x){ object o = object(); if x<=1: {float o.c = x;} else {float temp1 =x-1; float temp2 =x-2; float a =fibbo(temp1,).c; float b = fibbo(temp2,).c; float o.c = a+b;} ! return o;} float x = fibbo(9,).c; print_object(x);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# # print("___________________Example N15____________________________")
# #
# # # Parse input
#
# input_str = "def fibbo(float x){ object o = object(); if x<=1: {float o.c = x;} else {float temp1 = x-1; float temp2 = x-2; float a = fibbo(temp1,).c; float b = fibbo(temp2,).c; float o.c = a+b;} ! return o;} float x = fibbo(9,).c; print_object(x);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())
# print(test[1])
# print("___________________Example N15____________________________")
#
# # Parse input
#
# input_str = "def test(float x, float y){ object o = object(); float o.z = x + y ; ! return o;} def test(int x, int y){ object o = object(); float o.z = x * y ; ! return o;} test b = test(5, 6); float c = b.z; print_object(c);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# # print("___________________Example N15____________________________")
# #
# # # Parse input
#
# input_str = "def vector(){ object o = object();  float o.x = 3.0; ! return o;} def vector3d(){ vector obj = vector(); float temp = obj.x + 1; obj.x = temp; float obj.y = 2.0 ;  ! return obj;} vector a = vector(); print_object(a); float c = a.o; vector b = vector3d(); float d = b.x; print_object(b);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# # print("___________________Example N15____________________________")
# #
# # # Parse input
#
# input_str = "def vector(){ object o = object();  float o.x = 3.0; ! return o;} def vector3d(){ vector obj = vector(); float temp = obj.x + 1; obj.x = temp; float obj.y = 2.0 ;  ! return obj;} vector a = vector(); print_object(a); vector b = vector3d(); print_object(b);"
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# print("___________________Example N15____________________________")
#
# # Parse input

# input_str = ("def car(float x, float y){ object o = object(); float o.z = x + y ; ! return o;}  "
#              "def toyota(float x, float y){ car o = car(x,y);  float o.new = o.z * y ; ! return o;}"
#              "car b = car(5, 6); "
#              "float c = b.z; print_object(c);"
#              "car t = toyota(3, 2);"
#              "float d = t.new; print_object(d);"
#              )
# parse_tree, test = interpret(input_str)
# print_expression_tree(parse_tree.pretty())

# input_str = ("def employee(float a) {object o = object();float o.age = a;return o;}"
#              "def junior_employee(float a) {employee e = employee(a,);float e.bonus = 1000.0;float e.salary = 2000.0;return e;}"
#              "def senior_employee(float a, float months) {employee e = employee(a,);float e.bonus = 100.0;float e.extra_bonus = 1200.0 + months;float e.salary = 4000.0;return e;}"
#              "def calc_yearly_salary(junior_employee e) {object o = object();float o.yearly_salary = e.salary * 12 + e.bonus;return o;}"
#              "def calc_yearly_salary(senior_employee e) {object o = object();float o.yearly_salary = e.salary * 12 + e.extra_bonus + e.bonus;return o;}"
#              "employee eric = employee(22.0,);"
#              "junior_employee john = junior_employee(25.0,);"
#              "senior_employee jane = senior_employee(40.0, 10.0);"
#              "calc_yearly_salary john_salary = calc_yearly_salary(john,);");

# input_str = ("def employee(float a, float b) {object o = object();float o.age = a + b;return o;}"
#              "float a  = 22.0;"
#              "float b  = 12.0;"
#              "employee eric = employee(a, b);"
#              "float b = eric.age;"
#              "print_object(b);");
#
# input_str = ("def employee(float a, float b) {object o = object(); float o.age = a + b; return o;}"
#              "def getSum(float a, float b) {object o = object(); float o.sum = a + b; return o;}"
#              "float a  = 22.0;"
#              "float b  = 12.0;"
#              "float c = getSum(a, b).sum;"
#              "float d = 2.0;"
#              "employee eric = employee(c, d);"
#              "float f = eric.age;"
#              "print_object(f);");
#
# input_str = ("def employee(float a, float b) {object o = object(); float o.age = a + b; return o;}"
#              "def empSum(float b, employee a ) {object o = object(); float o.sum = a.age + b; return o;}"
#              "float a  = 22.0;"
#              "float b  = 12.0;"
#              "employee eric = employee(a, b);"
#              "empSum c = empSum(b, eric);");
#
# input_str = ("def employee(float a, float b) {object o = object(); float o.age = a + b; return o;}"
#              "def empSum(float b, employee a ) {object o = object(); float o.sum = a.age + b; return o;}"
#              "float a  = 22.0;"
#              "float b  = 12.0;"
#              "employee eric = employee(a, b);"
#              "float f = eric.age;"
#              "print_object(f);"
#              "empSum c = empSum(b, eric).sum;"
#              "print_object(c);");
#
# input_str = ("def human(float a, float b) {object o = object(); float o.age = a + b; return o;}"
#              "def employee(float a, float b ) { human h = human(a, b); float h.salary = 5.0 + b; return h;}"
#              "human eric = human(10, 21);"
#              "employee junior = employee(11.0, 10.0);"
#              "float test = junior.salary;"
#              "print_object(test);");

# input_str = ("def human(float a, float b) {object o = object(); float o.age = a + b; return o;}"
#              "def employee(float a, float b ) { human h = human(a, b); float h.salary = 5.0 + b; return h;}"
#              "human eric = human(10, 21);"
#              "human junior = employee(11.0, 10.0);"
#              "float test = junior.salary;"
#              "print_object(eric);");

# input_str = ("float a = 2.0 + 1.0; a = 5.0; print_object(a);");

if __name__ == "__main__":
    # Example input string
    input_str = ("def test(){ object o = object(); float x = 5.0; float y = 6.0; float o.sum = x + y; float o.te = x*y; return o;} "
                 "def test2(){ test t = test(); t.sum = 2.0;  float t.new = 3.0 + t.sum; return t;}"
                 "test2 t2= test2();"
                 "float c = t2.sum;"
                 "float d = t2.new;"
                 "print_object(c);"
                 "print_object(d);"
                 "test t= test();"
                 "float f = t.sum;"
                 "print_object(f);"
                 )

    # Interpret the input string
    parse_tree, test = interpret(input_str)

    # Print the parse tree
    print_expression_tree(parse_tree.pretty())

    # Print the test result
    print("test", test)