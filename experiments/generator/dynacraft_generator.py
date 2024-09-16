import random

class DynaCraftGenerator:

    def __init__(self):
        # reduce to 3 variables and 3 fun_names
        self.variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'o', 'p']
        self.free_variables = []

        self.fun_names = ["fun1", "fun2", "fun3", "fun4", "fun5", "fun6", "fun7", "fun8", "fun9"]
        self.operators = ['+', '-', '*', '/']
        self.comparison_operators = ['==', '!=', '<', '<=', '>', '>=']

        self.free_functions = []
        self.used_variables = []
        self.used_functions = ["object"]
        self.code_lines = []


    def random_true_false(self):
        # choices = [False] * 9 + [True] * 1  # 8 False, 2 True
        return random.random() < 0.1

    def init_float_var(self):
        variable = random.choice(self.free_variables)
        self.used_variables.append(variable)
        self.free_variables.remove(variable)
        self.random_float = round(random.uniform(0.1, 20.0), 3)
        expression = self.generate_random_expression(variable)
        initialization = f"float {variable} = {expression};"
        return initialization

    def init_method_float_var(self, used_objects, local_free_variables,local_used_variables):
        variable = random.choice(local_free_variables)
        if(variable in used_objects):
            variable = f"{variable}.{random.choice(self.variables)}"
        random_float = round(random.uniform(0.1, 20.0), 3)
        expression = self.generate_method_random_expression(local_free_variables, local_used_variables, variable)
        initialization = f"float {variable} = {expression};"
        return initialization, variable

    def init_object(self, exclude_obj = "fun_10"):
        obj_name = random.choice(self.variables)
        result = f"object {obj_name} = object(); "
        return result, obj_name

    def generate_comparisson(self):
        if not self.used_variables:
            return ""
        variable1 = random.choice(self.used_variables)
        variable2 = random.choice(self.used_variables)
        operator = random.choice(self.comparison_operators)
        result = f"{variable1}{operator}{variable2}"
        return result

    def generate_random_expression(self, variable_called="x"):
        if not self.used_variables:
            expression = str(round(random.uniform(0.1, 20.0), 1))
            return expression
        # Determine the number of terms (between 1 and 5)
        num_terms = random.randint(1, 5)

        # Start building the expression with a random float or variable
        filtered_functions = [var for var in self.used_variables if var != variable_called]
        if not filtered_functions:
            expression = str(round(random.uniform(0.1, 20.0), 1))
            return expression
        expression = str(random.choice(filtered_functions))

        # Randomly decide to start with a float
        if random.choice([True, False]):
            expression = str(round(random.uniform(0.1, 20.0), 1))

        for _ in range(num_terms - 1):
            operator = random.choice(self.operators)
            # Choose to add either a variable or a float
            if random.choice([True, False]):
                filtered_functions = [var for var in self.used_variables if var != variable_called]
                if not filtered_functions:
                    expression = str(round(random.uniform(0.1, 20.0), 1))
                    return expression
                term = str(random.choice(filtered_functions))

            else:
                term = str(round(random.uniform(0.1, 20.0), 1))
            expression += f' {operator} {term}'

        return expression


    def generate_method_random_expression(self, local_free_variables, local_used_variables, variable_called="x"):
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
            operator = random.choice(self.operators)
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


    def generate_method_body(self, fun_name = "fun6"):
        method_lines = []
        used_objects = []
        local_used_variables = []
        local_free_variables = self.variables[:]

        result, used_name = self.method_switch_case(2, used_objects, fun_name)
        used_objects.append(used_name)
        method_lines.append(result)
        local_free_variables.remove(used_name)
        for _ in range(3):
            result, used_name = self.method_switch_case(1, used_objects, fun_name, local_free_variables, local_used_variables)
            local_free_variables.remove(used_name)
            local_used_variables.append(used_name)
            method_lines.append(result)

        return_var = random.choice(used_objects)
        return_line = f"return {return_var};"
        method_lines.append(return_line)
        return method_lines


    def generate_method(self):
        ##print(f"in method print funs are {free_functions}")
        method_name = random.choice(self.free_functions)
        self.used_functions.append(method_name)
        self.free_functions.remove(method_name)
        params = random.sample(self.variables, k=random.randint(1, 2))
        params_string = ", ".join(f"float {var}" for var in params)
        # method_body = generate_method_body()
        method_body = f"{' '.join(self.generate_method_body(method_name))}"
        result = f"def {method_name}({params_string}){{ {method_body} }}"

        return result


    def generate_methodcall(self):
        variable = random.choice(self.variables)
        if not self.used_functions:
            return ''
        method = random.choice(self.used_functions)

        method_call_str = self.method_call_helper(method)
        result = f"{method} {variable} = {method_call_str};"

        return result


    def method_call_helper(self, method):
        params = []

        param_num = random.randint(1, 2)
        for _ in range(param_num):
            if random.choice([True, False]):
                params.append(random.choice(self.variables))
            else:
                params.append(round(random.uniform(0.1, 20.0), 3))

        params_string = ", ".join(f"{param}" for param in params)

        method_call_str = f"{method}({params_string})"
        return method_call_str


    def generate_if_statement(self):
        if random.choice([True, False]):
            comparison = self.generate_comparisson()
        else:
            comparison = self.method_call_helper(random.choice(self.used_functions))
        body_lines1 = self.generate_method_body()
        codeblock1 = " ".join(f"{line}" for line in body_lines1)
        body_lines2 = self.generate_method_body()
        codeblock2 = " ".join(f"{line}" for line in body_lines2)

        result = f"if {comparison}: {{ {codeblock1} }} else {{ {codeblock2} }}"
        return result


    def while_statement(self):
        if random.choice([True, False]):
            comparison = self.generate_comparisson()
        else:
            comparison = self.method_call_helper(random.choice(self.fun_names))
        body_lines = self.generate_method_body()
        codeblock = " ".join(f"{line}" for line in body_lines)

        result = f"while {comparison}: {{ {codeblock} }}"
        return result


    def generic_switch_case(self, value):
        switcher = {
            1: self.init_float_var,
            2: self.generate_method,
            3: self.generate_methodcall,
            4: self.generate_if_statement,
            5: self.while_statement
        }
        return switcher.get(value)()

    def method_switch_case(self, value, used_objects, exlude_function="fun_10", local_free_varianbles=[], local_used_variables=[]):
        switcher = {
            1: lambda:self.init_method_float_var(used_objects, local_free_varianbles, local_used_variables),
            2: lambda:self.init_object(exlude_function),
            3:self.generate_if_statement,
            4:self.while_statement
        }
        return switcher.get(value)()
