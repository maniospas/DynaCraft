from tqdm import tqdm
import os, random
from dynacraft.interpreter import interpret
from experiments.generator.dynacraft_generator import DynaCraftGenerator


def generate_data(directory="synthetic_data", snippets=2000):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f"{directory}/valid.txt", "w") as valid:
        with open(f"{directory}/invalid.txt", "w") as invalid:
            for i in tqdm(range(0, snippets), desc="Generating snippets"):
                generator = DynaCraftGenerator();
                generator.free_variables = generator.variables[:]
                generator.free_functions = generator.fun_names[:]
                generator.used_variables = []
                generator.used_functions = ["object"]
                final_lines = ""
                for _ in range(5):
                    random_int = random.randint(1, 5)
                    result = generator.generic_switch_case(random_int)
                    final_lines += result
                try:
                    input_str = (final_lines)
                    interpret(input_str)
                    file = valid
                except Exception:
                    file = invalid

                file.write(final_lines)
                file.write("\n-----\n")

generate_data()