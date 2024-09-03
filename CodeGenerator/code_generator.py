import random
from tqdm import tqdm
import logging.config
import os

# Step 1: Specify the directory and check if it exists
log_directory = "log_files"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)  # Create the directory if it does not exist

# Step 2: Generate a unique filename for each run
#filename = f"testData.txt"
filename = f"testData_test.txt"
# Step 3: Configure logging to use the new file
logging.basicConfig(filename=filename, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('ExampleLogger')
logger.info("This log entry will go into a uniquely named file for this run.")

# reduce to 3 variables and 3 fun_names
variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'o', 'p']
free_variables = []

fun_names = ["fun1", "fun2", "fun3", "fun4", "fun5", "fun6", "fun7", "fun8", "fun9"]
operators = ['+', '-', '*', '/']
comparison_operators = ['==', '!=', '<', '<=', '>', '>=']

free_functions = []
used_variables = []
used_functions = ["object"]
code_lines = []



from lark import Lark
#from lark.tree import pydot__tree_to_png
from IPython.display import Image, display
from Grammar.grammar import parser
from Grammar.grammar import grammar
from OldContexts.oldTransformer import MyTransformer
from OldContexts.mainContext import Context
from MainContext.TopDownMainContextTest import TopDownContextTest
from myLogger import print_expression_tree

# Example usage:
transformer = MyTransformer()

transformer = Context()

transformer = TopDownContextTest()

parser = Lark(grammar, start='start', parser='earley')

def interpret(code):
    tree = parser.parse(code)
    result = transformer.visit_topdown(tree)
    return tree, result


def random_true_false():
    # choices = [False] * 9 + [True] * 1  # 8 False, 2 True
    return random.random() < 0.1

def init_float_var():
    variable = random.choice(free_variables)
    used_variables.append(variable)
    free_variables.remove(variable)
    random_float = round(random.uniform(0.1, 20.0), 3)
    expression = generate_random_expression(variable)
    initialization = f"float {variable} = {expression};"
    return initialization

def init_method_float_var(used_objects, local_free_variables,local_used_variables):
    variable = random.choice(local_free_variables)
    if(variable in used_objects):
        variable = f"{variable}.{random.choice(variables)}"
    random_float = round(random.uniform(0.1, 20.0), 3)
    expression = generate_method_random_expression(local_free_variables, local_used_variables, variable)
    initialization = f"float {variable} = {expression};"
    return initialization, variable

def init_object(exclude_obj = "fun_10"):
    obj_name = random.choice(variables)
    result = f"object {obj_name} = object(); "
    return result, obj_name

    # ##print("The used funs are", used_functions)
    # if not used_functions:
    #     return '', ''
    # filtered_functions = [func for func in used_functions if func != exclude_obj]
    # obj_name = random.choice(variables)
    # ##print("The exc obj is ", exclude_obj)
    # ##print("The filtered_functions  are", filtered_functions)
    # if not filtered_functions:
    #     result = f"object {obj_name} = object(); "
    #     return result, obj_name
    # object_type = random.choice(filtered_functions)
    # result = f"{object_type} {obj_name} = {object_type}(); "
    # return result, obj_name

def generate_comparisson():
    if not used_variables:
        return "";
    variable1 = random.choice(used_variables)
    variable2 = random.choice(used_variables)
    operator = random.choice(comparison_operators)

    result = f"{variable1}{operator}{variable2}"

    return result;
def generate_random_expression(variable_called = "x"):
    # Define possible operators
    # operators = ['+', '-', '*', '/']
    if not used_variables:
        expression = str(round(random.uniform(0.1, 20.0), 1))
        return expression
    # Determine the number of terms (between 1 and 5)
    num_terms = random.randint(1, 5)

    # Start building the expression with a random float or variable
    filtered_functions = [var for var in used_variables if var != variable_called]
    if not filtered_functions:
        expression = str(round(random.uniform(0.1, 20.0), 1))
        return expression
    expression = str(random.choice(filtered_functions))

    # Randomly decide to start with a float
    if random.choice([True, False]):
        expression = str(round(random.uniform(0.1, 20.0), 1))

    for _ in range(num_terms - 1):
        operator = random.choice(operators)
        # Choose to add either a variable or a float
        if random.choice([True, False]):
            filtered_functions = [var for var in used_variables if var != variable_called]
            if not filtered_functions:
                expression = str(round(random.uniform(0.1, 20.0), 1))
                return expression
            term = str(random.choice(filtered_functions))

        else:
            term = str(round(random.uniform(0.1, 20.0), 1))
        expression += f' {operator} {term}'

    return expression

def generate_method_random_expression( local_free_variables, local_used_variables, variable_called = "x"):
    # Define possible operators
    # operators = ['+', '-', '*', '/']
    if not local_used_variables:
        expression = str(round(random.uniform(0.1, 20.0), 1))
        return expression
    # Determine the number of terms (between 1 and 5)
    num_terms = random.randint(1, 5)

    # Start building the expression with a random float or variable
    expression = str(random.choice(local_used_variables))

    # Randomly decide to start with a float
    if random.choice([True, False]):
        expression = str(round(random.uniform(0.1, 20.0), 1))

    for _ in range(num_terms - 1):
        operator = random.choice(operators)
        # Choose to add either a variable or a float
        if random.choice([True, False]):
            temp_term = str(random.choice(local_used_variables))
            ##print("1",temp_term)
            ##print("2",variable_called)
            if temp_term ==  variable_called:
                continue
            term = temp_term
        else:
            term = str(round(random.uniform(0.1, 20.0), 1))
        expression += f' {operator} {term}'

    return expression
def generate_method_body(fun_name = "fun6"):
    method_lines = []
    used_objects = []
    local_used_variables = []
    local_free_variables = variables[:]

    result, used_name = method_switch_case(2, used_objects, fun_name)
    used_objects.append(used_name)
    method_lines.append(result)
    local_free_variables.remove(used_name)
    for _ in range(3):
        #random_int = random.randint(1, 2)
        result, used_name = method_switch_case(1, used_objects, fun_name, local_free_variables, local_used_variables)
        local_free_variables.remove(used_name)
        #if(random_int == 1):
            #used_objects.append(used_name)
        #if (random_int == 2):
        local_used_variables.append(used_name)

        method_lines.append(result)
        # if random_true_false():
        #     if_result = generate_if_statement()
        #     method_lines.append(if_result)
        # if random_true_false():
        #     while_result = while_statement()
        #     method_lines.append(while_result)

    return_var = random.choice(used_objects)
    return_line = f"return {return_var};"
    method_lines.append(return_line)
    return method_lines
    # if( used_objects and local_used_variables ):
    #     if random.choice([True, False]):
    #         return_var = random.choice(used_objects)
    #
    #         return_line = f"! return {return_var};"
    #         method_lines.append(return_line)
    #         return method_lines
    #
    #     return_var = random.choice(local_used_variables)
    #     return_line = f"! return {return_var};"
    #     method_lines.append(return_line)
    #     return method_lines
    #
    # elif  used_objects:
    #     return_var = random.choice(used_objects)
    #     return_line = f"! return {return_var};"
    #     method_lines.append(return_line)
    #     return method_lines
    #
    # else:
    #     return_var = random.choice(local_used_variables)
    #     return_line = f"! return {return_var};"
    #     method_lines.append(return_line)
    #     return method_lines

def generate_method():
    ##print(f"in method print funs are {free_functions}")
    method_name = random.choice(free_functions)
    used_functions.append(method_name)
    free_functions.remove(method_name)
    params = random.sample(variables, k=random.randint(1, 2))
    params_string = ", ".join(f"float {var}" for var in params)
    # method_body = generate_method_body()
    method_body = f"{' '.join(generate_method_body(method_name))}"
    result = f"def {method_name}({params_string}){{ {method_body} }}"

    return result

def generate_methodcall():
    variable = random.choice(variables)
    if not used_functions:
        return ''
    method = random.choice(used_functions)

    method_call_str = method_call_helper(method)
    result = f"{method} {variable} = {method_call_str};"

    return result

def method_call_helper(method):
    params = []

    param_num = random.randint(1, 2)
    for _ in range(param_num):
        if random.choice([True, False]):
            params.append(random.choice(variables))
        else:
            params.append(round(random.uniform(0.1, 20.0), 3))

    params_string = ", ".join(f"{param}" for param in params)

    method_call_str = f"{method}({params_string})"
    return method_call_str
def generate_if_statement():
    if random.choice([True, False]):
        comparison = generate_comparisson()
    else:
        comparison = method_call_helper(random.choice(used_functions))
    body_lines1 = generate_method_body()
    codeblock1 = " ".join(f"{line}" for line in body_lines1)
    body_lines2 = generate_method_body()
    codeblock2 = " ".join(f"{line}" for line in body_lines2)

    result = f"if {comparison}: {{ {codeblock1} }} else {{ {codeblock2} }}"
    return result;

def while_statement():
    if random.choice([True, False]):
        comparison = generate_comparisson()
    else:
        comparison = method_call_helper(random.choice(fun_names))
    body_lines = generate_method_body()
    codeblock = " ".join(f"{line}" for line in body_lines)

    result = f"while {comparison}: {{ {codeblock} }}"
    return result;
def generic_switch_case(value):
    switcher = {
        1: init_float_var,
        2: generate_method,
        3: generate_methodcall,
        4: generate_if_statement,
        5: while_statement
    }
    return switcher.get(value, "Default Case")()

def method_switch_case(value, used_objects, exlude_function = "fun_10", local_free_varianbles = [], local_used_variables = []):
    switcher = {
        1: lambda:init_method_float_var(used_objects, local_free_varianbles, local_used_variables),
        2: lambda:init_object(exlude_function),
        3:generate_if_statement,
        4:while_statement
    }
    return switcher.get(value, "Default Case")()

# def generate_code(num_expressions=5):
#     code_lines = []
#     for _ in range(num_expressions):
#         var = random.choice(variables)
#         expression = generate_random_expression(variables)
#         code_lines.append(f'float {var} = {expression};')
#     return code_lines

# for i in range(81, 91):
#     #print("-----")
#     for _ in range(10):
#         random_int = random.randint(1, 5)
#         # #print("Random Integer:", random_int)
#
#         result = generic_switch_case(random_int)
#         #print(result)

num_snippets = 200000
with tqdm(total=num_snippets, desc="Generating snippets") as pbar:
    for i in range(0, num_snippets):
        free_variables = variables[:]
        free_functions = fun_names[:]
        # #print(f"The free funs are {free_functions}")
        used_variables = []
        used_functions = ["object"]
        final_lines = ""
        # #print("-----")
        for _ in range(5):
            random_int = random.randint(1, 5)
            # #print("Random Integer:", random_int)

            result = generic_switch_case(random_int)

            # try:
            #     input_str = (result)
            #     parse_tree, test = interpret(input_str)
            #     logger.info(result)
            #     logger.info("\n-----")
            #     #print(1)  # Print 1 on successful execution
            # except Exception as e:
            #     ##print(f"An error occurred: {e}")
            #     #print(0)  # Print 0 on exception
            # #print(result)

            final_lines += result
        # #print("NOW !!!!")
        #print(final_lines)
        try:

            input_str = (final_lines)
            parse_tree, test = interpret(input_str)
            logger.info(final_lines)
            logger.info("\n-----")
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")  # Print 1 on successful execution
        except Exception as e:
            # #print(f"An error occurred: {e}")
            # #print(0)  # Print 0 on exception
            logger.info("No usefull data")
            with open('invalid_dc_test.txt', 'a') as invalid_file:
                invalid_file.write(final_lines)
                invalid_file.write("\n-----\n")
        pbar.update(1)
        #continue
##print(f"{code_lines}\n")


# num_snippets = 10000  # Adjust the number of snippets as needed
# with tqdm(total=num_snippets, desc="Generating snippets") as pbar:
#     for _ in range(num_snippets):
#         free_variables = variables[:]
#         free_functions = fun_names[:]
#         used_variables = []
#         used_functions = ["object"]
#         final_lines = ""
#
#         for _ in range(5):
#             random_int = random.randint(1, 5)
#             result = generic_switch_case(random_int)
#             final_lines += result
#
#         try:
#             input_str = final_lines
#             parse_tree, test = interpret(input_str)
#             with open('valid_dc2.txt', 'a') as valid_file:
#                 valid_file.write(final_lines)
#                 valid_file.write("\n-----\n")
#         except Exception as e:
#             # with open('invalid_dc.txt', 'a') as invalid_file:
#             #     invalid_file.write(final_lines)
#             #     invalid_file.write("\n-----\n")
#             logger.info("No usefull data")
#         pbar.update(1)

