import re
import os


def extract_and_filter_logs(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()

    filtered_data = []
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - INFO - (.*)$')
    code_snippet = []
    inside_code_block = False

    for line in data:
        if "No useful data" in line or "This log entry will go into a uniquely named file for this run" in line:
            continue

        match = pattern.match(line)
        if match:
            if inside_code_block:
                filtered_data.append("\n".join(code_snippet))
                filtered_data.append("-----")
                code_snippet = []
                inside_code_block = False
            filtered_data.append(match.group(1))
        else:
            if inside_code_block or line.strip():
                code_snippet.append(line.rstrip())
                inside_code_block = True

    if code_snippet:
        filtered_data.append("\n".join(code_snippet))
        filtered_data.append("-----")

    cleaned_data = []
    for line in filtered_data:
        if line.strip() and line.strip() != "-----":
            cleaned_data.append(line)
            cleaned_data.append("-----")

    if cleaned_data and cleaned_data[-1] == "-----":
        cleaned_data.pop()

    if os.path.exists(output_file):
        with open(output_file, 'a') as file:
            file.write('\n-----\n')
            file.write('\n'.join(cleaned_data))
    else:
        with open(output_file, 'w') as file:
            file.write('\n'.join(cleaned_data))

    print(f"Filtered logs saved to {output_file}")

# Specify the input log file and output text file
input_file = 'py_test.txt'
output_file = 'valid_py.txt'

# Run the extraction and filtering
extract_and_filter_logs(input_file, output_file)