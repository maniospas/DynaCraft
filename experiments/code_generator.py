from tqdm import tqdm
import os, random
from experiments.generator.python_generator import PythonGenerator as Generator


def generate_data(directory="synthetic_data", snippets=2000):
    if not os.path.exists(directory):
        os.makedirs(directory)
    count_valid = 0
    count_invalid = 0
    with open(f"{directory}/valid.txt", "w") as valid:
        with open(f"{directory}/invalid.txt", "w") as invalid:
            for _ in tqdm(range(0, snippets), desc="Generating snippets"):
                generator = Generator()
                generator.free_variables = generator.variables[:]
                generator.free_functions = generator.fun_names[:]
                generator.used_variables = []
                generator.used_functions = ["object"]
                final_lines = ""
                for _ in range(5):
                    random_int = random.randint(1, 5)
                    result = generator.generic_switch_case(random_int)
                    final_lines += result + "\n"
                try:
                    # print("___________________________________________________________")
                    # print(final_lines)
                    input_str = (final_lines)
                    generator.interpret(input_str)
                    file = valid
                    count_valid += 1
                except (Exception, RuntimeError):
                    file = invalid
                    if count_invalid > 2*count_invalid:  # reduce file writes for invalid (speed up generation)
                        continue
                    count_invalid += 1

                file.write(final_lines)
                file.write("\n-----\n")

generate_data("synthetic_data"+Generator.__name__)