import re
import os


def extract_and_filter_logs(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()

    filtered_data = []
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - INFO - (.*)$')

    for line in data:
        if "No usefull data" in line or "This log entry will go into a uniquely named file for this run" in line:
            continue
        match = pattern.match(line)
        if match:
            filtered_data.append(match.group(1))

    # Remove empty lines and ensure no consecutive "-----" separators
    cleaned_data = []
    for line in filtered_data:
        if line.strip():  # Only add non-empty lines
            cleaned_data.append(line.strip())
            cleaned_data.append("-----")

    # Remove the last "-----" if it exists
    if cleaned_data and cleaned_data[-1] == "-----":
        cleaned_data.pop()

    # Check if the output file already exists
    if os.path.exists(output_file):
        with open(output_file, 'a') as file:
            file.write('\n-----\n')  # Add separator before appending new content
            file.write('\n'.join(cleaned_data))
    else:
        with open(output_file, 'w') as file:
            file.write('\n'.join(cleaned_data))

    print(f"Filtered logs saved to {output_file}")


# Specify the input log file and output text file
input_file = 'testData_test.txt'
output_file = 'valid_dc_test.txt'

# Run the extraction and filtering
extract_and_filter_logs(input_file, output_file)