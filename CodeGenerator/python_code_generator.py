import random
import concurrent.futures
from tqdm import tqdm

# Define possible variables and functions
variables = ["x", "y", "z", "a", "b", "c"]
functions = ["func1", "func2", "func3"]
operators = ['+', '-', '*', '/']
comparison_operators = ['==', '!=', '<', '<=', '>', '>=']

def init_variable():
    var_name = random.choice(variables)
    value = round(random.uniform(0.1, 20.0), 3)
    return f"{var_name} = {value}"

def simple_calculation():
    var1 = random.choice(variables)
    var2 = random.choice(variables)
    operator = random.choice(operators)
    return f"{var1} = {var1} {operator} {var2}"

def simple_function():
    func_name = random.choice(functions)
    params = random.sample(variables, k=random.randint(1, 2))
    params_str = ", ".join(params)
    body_line1 = init_variable()
    body_line2 = simple_calculation()
    return f"def {func_name}({params_str}):\n    {body_line1}\n    {body_line2}"

def if_statement():
    var1 = random.choice(variables)
    var2 = random.choice(variables)
    operator = random.choice(comparison_operators)
    condition = f"{var1} {operator} {var2}"
    body_line1 = init_variable()
    body_line2 = simple_calculation()
    return f"if {condition}:\n    {body_line1}\nelse:\n    {body_line2}"

def while_loop():
    var = random.choice(variables)
    threshold = round(random.uniform(0.1, 20.0), 3)
    body_line = simple_calculation()
    return f"while {var} < {threshold}:\n    {body_line}"

def random_code_snippet():
    snippets = [init_variable, simple_calculation, simple_function, if_statement, while_loop]
    num_lines = 0
    snippet_lines = []
    while num_lines < 4 or num_lines > 5:
        snippet_lines = []
        num_lines = 0
        while num_lines < 4:
            snippet_func = random.choice(snippets)
            snippet = snippet_func()
            if '\n' in snippet:
                lines = snippet.split('\n')
                num_lines += 1  # Counting the function as 1 line
            else:
                lines = [snippet]
                num_lines += 1
            snippet_lines.extend(lines)
    return "\n".join(snippet_lines)

def is_valid_python_code(code):
    try:
        exec(code, {})
        return True
    except Exception:
        return False

def generate_snippet():
    snippet = random_code_snippet()
    if is_valid_python_code(snippet):
        return snippet, 'valid'
    else:
        return snippet, 'invalid'

def main():
    valid_snippets = []
    invalid_snippets = []

    num_snippets = 100  # Adjust the number of snippets as needed

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(generate_snippet): i for i in range(num_snippets)}
        for future in tqdm(concurrent.futures.as_completed(futures, timeout=5), total=num_snippets, desc="Generating snippets"):  # Set a timeout for each future
            try:
                snippet, validity = future.result(timeout=5)
                if validity == 'valid':
                    valid_snippets.append(snippet)
                else:
                    invalid_snippets.append(snippet)
            except concurrent.futures.TimeoutError:
                print("A snippet generation task timed out.")
            except Exception as e:
                print(f"An error occurred: {e}")

    # Append valid snippets to file
    with open('valid_snippets_test.txt', 'a') as valid_file:
        for snippet in valid_snippets:
            valid_file.write(snippet)
            valid_file.write("\n-----\n")

    # #Append invalid snippets to file
    # with open('invalid_snippets_test.txt', 'a') as invalid_file:
    #     for snippet in invalid_snippets:
    #         invalid_file.write(snippet)
    #         invalid_file.write("\n-----\n")

if __name__ == "__main__":
    main()
