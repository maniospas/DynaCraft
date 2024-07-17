import random
from tqdm import tqdm
import logging.config
import os
import random
import string

# Configure logging
log_directory = "log_files"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
filename = f"py_test.txt"
logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('ExampleLogger')
logger.info("This log entry will go into a uniquely named file for this run.")

variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'o', 'p']

# def generate_random_variable_name(length=8):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(length))
#
# variables = [generate_random_variable_name() for _ in range(50)]

free_variables = []
fun_names = ["fun1", "fun2", "fun3", "fun4", "fun5", "fun6", "fun7", "fun8", "fun9"]
operators = ['+', '-', '*', '/']
comparison_operators = ['==', '!=', '<', '<=', '>', '>=']

free_functions = []
used_variables = []
used_functions = ["object"]
code_lines = []

def random_true_false():
    return random.random() < 0.1

def init_float_var():
    variable = random.choice(free_variables)
    used_variables.append(variable)
    free_variables.remove(variable)
    expression = generate_random_expression(variable)
    initialization = f"{variable} = {expression}"
    return initialization

def init_method_float_var(used_objects, local_free_variables, local_used_variables):
    variable = random.choice(local_free_variables)
    if variable in used_objects:
        variable = f"{variable}.{random.choice(variables)}"
    expression = generate_method_random_expression(local_free_variables, local_used_variables, variable)
    initialization = f"{variable} = {expression}"
    return initialization, variable

def init_object(exclude_obj="fun_10"):
    obj_name = random.choice(variables)
    result = f"{obj_name} = object()"
    return result, obj_name

def generate_comparisson():
    if not used_variables:
        return ""
    variable1 = random.choice(used_variables)
    variable2 = random.choice(used_variables)
    operator = random.choice(comparison_operators)
    result = f"{variable1} {operator} {variable2}"
    return result

def generate_random_expression(variable_called="x"):
    if not used_variables:
        expression = str(round(random.uniform(0.1, 20.0), 1))
        return expression
    num_terms = random.randint(1, 5)
    filtered_functions = [var for var in used_variables if var != variable_called]
    if not filtered_functions:
        expression = str(round(random.uniform(0.1, 20.0), 1))
        return expression
    expression = str(random.choice(filtered_functions))
    if random.choice([True, False]):
        expression = str(round(random.uniform(0.1, 20.0), 1))
    for _ in range(num_terms - 1):
        operator = random.choice(operators)
        if random.choice([True, False]):
            filtered_functions = [var for var in used_variables if var != variable_called]
            if not filtered_functions:
                expression = str(round(random.uniform(0.1, 20.0), 1))
                return expression
            term = str(random.choice(filtered_functions))
        else:
            term = str(round(random.uniform(0.1, 20.0), 1))
        expression += f" {operator} {term}"
    return expression

def generate_method_random_expression(local_free_variables, local_used_variables, variable_called="x"):
    if not local_used_variables:
        expression = str(round(random.uniform(0.1, 20.0), 1))
        return expression
    num_terms = random.randint(1, 5)
    expression = str(random.choice(local_used_variables))
    if random.choice([True, False]):
        expression = str(round(random.uniform(0.1, 20.0), 1))
    for _ in range(num_terms - 1):
        operator = random.choice(operators)
        if random.choice([True, False]):
            temp_term = str(random.choice(local_used_variables))
            if temp_term == variable_called:
                continue
            term = temp_term
        else:
            term = str(round(random.uniform(0.1, 20.0), 1))
        expression += f" {operator} {term}"
    return expression

def generate_method_body(fun_name="fun6"):
    method_lines = []
    used_objects = []
    local_used_variables = []
    local_free_variables = variables[:]
    result, used_name = method_switch_case(2, used_objects, fun_name)
    used_objects.append(used_name)
    method_lines.append(result)
    local_free_variables.remove(used_name)
    for _ in range(3):
        result, used_name = method_switch_case(1, used_objects, fun_name, local_free_variables, local_used_variables)
        local_free_variables.remove(used_name)
        local_used_variables.append(used_name)
        method_lines.append(result)
    return_var = random.choice(used_objects)
    return_line = f"return {return_var}"
    method_lines.append(return_line)
    return method_lines

def generate_method():
    method_name = random.choice(free_functions)
    used_functions.append(method_name)
    free_functions.remove(method_name)
    params = random.sample(variables, k=random.randint(1, 2))
    params_string = ", ".join(f"{var}" for var in params)
    method_body = "\n    ".join(generate_method_body(method_name))
    result = f"def {method_name}({params_string}):\n    {method_body}"
    return result

def generate_methodcall():
    variable = random.choice(variables)
    if not used_functions:
        return ''
    method = random.choice(used_functions)
    method_call_str = method_call_helper(method)
    result = f"{variable} = {method_call_str}"
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
    codeblock1 = "\n    ".join(body_lines1)
    body_lines2 = generate_method_body()
    codeblock2 = "\n    ".join(body_lines2)
    result = f"if {comparison}:\n    {codeblock1}\nelse:\n    {codeblock2}"
    return result

def while_statement():
    if random.choice([True, False]):
        comparison = generate_comparisson()
    else:
        comparison = method_call_helper(random.choice(fun_names))
    body_lines = generate_method_body()
    codeblock = "\n    ".join(body_lines)
    result = f"while {comparison}:\n    {codeblock}"
    return result

def generic_switch_case(value):
    switcher = {
        1: init_float_var,
        2: generate_method,
        3: generate_methodcall,
        4: generate_if_statement,
        5: while_statement
    }
    return switcher.get(value, "Default Case")()

def method_switch_case(value, used_objects, exclude_function="fun_10", local_free_variables=[], local_used_variables=[]):
    switcher = {
        1: lambda: init_method_float_var(used_objects, local_free_variables, local_used_variables),
        2: lambda: init_object(exclude_function),
        3: generate_if_statement,
        4: while_statement
    }
    return switcher.get(value, "Default Case")()

num_snippets = 200000
with tqdm(total=num_snippets, desc="Generating snippets") as pbar:
    for i in range(num_snippets):
        free_variables = variables[:]
        free_functions = fun_names[:]
        used_variables = []
        used_functions = ["object"]
        final_lines = []
        for _ in range(5):
            random_int = random.randint(1, 5)
            result = generic_switch_case(random_int)
            final_lines.append(result)
        final_code = "\n".join(final_lines)
        try:
            exec(final_code)
            logger.info(f"\n{final_code}")
            logger.info("\n-----")
        except Exception as e:
            logger.info("No useful data")
            # with open('invalid_py_test.txt', 'a') as invalid_file:
            #     invalid_file.write(final_code)
            #     invalid_file.write("\n-----\n")
        pbar.update(1)